import re

from yasbd.rules.base import Rules
from yasbd.utils.trie import build_optimized_pattern


# fmt: off
class EsRules(Rules):


    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        # Social / Professional
        "sr", "sra", "srta", "d", "dña", "dra", "lic", "pdte",
        "prof", "arq", "abg", "mag", "lcdo", "dr", "mtr", "mgtr",
        "ldo", "lcda", "lda", "ing"

        # Military / Religious
        "cap", "cmdte", "tte", "subtte", "hno", "hnos", "pbro", 
        "cmdt", "cmte", "almte", "cnel", "col", "gral",

        # Noble / Royal
        "aa", "mm", "rr", "ss", "excmo", "ilmo"
    }

    # Case-sensitive pattern matching would cover the supress ones
    REFERENCE_ABBRVS = (Rules.REFERENCE_ABBRVS - {"no", "nos", "para"}) | {
        "pág", "núm", "nro", "dir", "t", "trad", "asoc", "aprox",
        "cf", "incl", "cía", "s", "párrf", "párr", "pg", "p", 
        "apdo", "art", "cap", "ed", "edit", "trad", 
        "vol", "pról", "v"
    }

    CORP_ENTITY_ABBRVS = Rules.CORP_ENTITY_ABBRVS | {
        "asoc", "cía", "admón", "ayto", "bibl", "coop", "del", "soc", "sdad"
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Artículo", "Anexo", "Capítulo", "Sección", "Subsección",
        "Unidad", "Módulo", "División",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS - {"ave"} | {
        "ej", "p. ej", "vid", "cll", "cra", "diag", "transv", "mz", "mza", 
        "lt", "urb", "asent", "dpto", "prov", "mnpio", "conj", "edif",
        "ofic", "av", "avd", "pso", "ctra", "pl", "blvr", "avda", "atte", "fdo", "c", "cdad", "ntra", "ntro", "pol. ind", "rbla", "tlfno", "tel", "tlf",  "blq", "esc",
    }

    DATE_ABBRVS = Rules.DATE_ABBRVS | {
        "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", 
        "oct", "nov", "dic", "lun" , "mar" ,"mié", "miér", "jue", 
        "vie", "sáb", "dom"
    }

    COMMON_SENT_STARTERS = {
        # Articles
        "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas",

        # Pronouns
        "Allí", "Aquel", "Aquella", "Aquellas", "Aquellos",
        "Aquí", "Cual", "Cuales", "Cuanto", "Ella", "Ellas",
        "Ellos", "Esa", "Esas", "Ese", "Esos", "Esta", "Estas",
        "Este", "Estos", "Nosotros", "Quien", "Quienes", "Tú",
        "Usted", "Vosotros", "Yo", "Él", "Allá", "Acá",

        # Inverted punctuation (always start a new sentence in Spanish)
        "¿", "¡",

        # Adverbs & Transitions
        "Actualmente", "Además", "Afortunadamente", "Ahora",
        "Anoche", "Anteriormente", "Antes", "Antiguamente",
        "Así que", "Aunque", "Ayer", "Aún", "Casi",
        "Consecuentemente", "Después", "Entonces", "Finalmente",
        "Generalmente", "Hoy", "Incluso", "Inmediatamente",
        "Jamás", "Lamentablemente", "Luego", "Mañana", "Mejor",
        "Menos", "Mientras", "Más", "Normalmente", "Nunca",
        "Ojalá", "Peor", "Pero", "Posteriormente",
        "Previamente", "Primero", "Probablemente", "Pronto",
        "Próximamente", "Quizá", "Quizás", "Realmente",
        "Segundo", "Seguramente", "Siempre", "Simultáneamente",
        "Sin embargo", "Solamente", "Solo", "Subsiguientemente",
        "Sucesivamente", "Tal vez", "También", "Tampoco",
        "Tarde", "Temprano", "Tercero", "Todavía", "Ya",
        "Últimamente", "Último", "Por una parte", "Por otra parte", 
        "Porque"

        # Question words
        "Cuál", "Cuándo", "Cuánto", "Cómo", "Dónde", "Por qué", 
        "Quién", "Qué",
    }

    # fmt: on
    @classmethod
    def _compile_regex_dynamically(cls):
        """Override base regex compilation to fix pronouns/ref abbrvs behavior."""
        super()._compile_regex_dynamically()


        # Ud./Uds./Vd./Vds. heuristic
        # Don't split if the next word is NOT a common starter (assumes it's a proper name).
        # Resolves the ambiguity "Ud. Marco" vs "Ud. Mañana".
        cls.MID_SENTENCE_FINDER_LST.extend([
            re.compile(rf"""
                \b(?i:{build_optimized_pattern({"ud", "uds", "vd", "vds"})})\.
                (?!\s+(?:{cls.COMMON_STARTERS_PATTERN})\b)
            """, re.X),

            # Dotted geographic pairs with optional whitespace (EE. UU., EE.UU., FF. AA.)
            # Only protect the first pair so a following sentence still splits.
            re.compile(r"\b[A-Z]{2}\.(?=\s*[A-Z]{1,2}\.)"),

            # In Spanish/Portuguese, these reference abbreviationsare are case-sensitve.
            # re.compile(r"(?:Nos?|Para)\.(?=\s*(\d+|\w))")
            
            # Whitespace separated abbreviations (a. C., d. C.)
            re.compile(r"\b[a-z]{1}\.(?=\s[A-Z]{1}\.)\B"),
        ])
