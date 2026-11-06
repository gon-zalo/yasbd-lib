ISO_CODE = "es"
TEST_DATA = [
    # Basic punctuation
    "Hola mundo.| ¿Cómo estás?| Bien, gracias.",
    "¿Cuál es tu nombre?| Me llamo Carlos.",
    "¿Viste la película anoche?.| Sí, fue increíble.| ¡Me encantó!| La actuación fue excelente.",

    # Abbreviations
    "El Sr. García llegó ayer.| La Sra. López también.",
    "La Prof. María dio una conferencia.",
    "El Lcdo. Pérez y el Mag. Torres son amigos.",
    "D. José y Dña. María son los dueños.",
    "El Cmdte. Rodríguez saludó al Cnel. Díaz.",
    "Véase la pág. 55 del libro.",
    "Vea el cap. 3 en el t. II de la obra.",
    "El art. 4 y el nro. 8 son clave.",
    "Se le pidió a los niños que leyeran los párrf. 5 y 6 del art. 4 de la constitución.",
    "Consulte el párr. 5 para más información.",
    "Llama al dir. general al tel. 555-1234.",
    "Compré pan, leche, etc. para la cena.",
    "La temperatura del motor alcanzó los 120,5 °C.| Afortunadamente, el sistema siguió funcionando.",
    "Lea, p. ej., el capítulo 5.",
    "La reunión es el lun. 15 de enero.",
    "Nació el 5 de abr. de 1990.",
    "El presidente de los EE. UU. visitó Europa.",
    "Las FF.AA. emitieron un comunicado oficial.",
    "El departamento de RR.HH. aprobó las vacaciones.",
    "La empresa Rodríguez y Cía. firmó el contrato junto con la Asoc. Internacional de Comercio.",
    "Trabaja en la Asoc.| Mañana tiene una reunión.",

    # structural headings
    "Capítulo 1. El comienzo.| Estaba oscuro afuera. | Nada se movía.",
    "Parte II. Introducción.| El sistema comienza aquí. | La inicialización sigue.",
    "El informe fue completado.| Capítulo 3. Análisis de resultados.",

    # Addresses & Locations
    "Vive en la av. de la Mancha.",
    "Viven en la c. Mayor, 12.",
    "El accidente fue en la ctra. 37.",
    "Dobla en la transv. 3 y sigue por la diag. 5.",
    "La casa está en la urb. Las Rosas, c/ de Quevedo núm. 20, blq. B, esc. 2. ",

    # Common Starters after abbreviations
    "Llegó el Sr. Por suerte trajo el paquete.",
    "Llegó el Sr. García.| Como no estaba, se fue.",

    # Parentheses and quotes
    "El problema —¿y quién lo iba a decir?— fue resuelto rápido.",
    "La decisión —¡increíblemente difícil!— cambió todo.",
    "Mi hermano (que es mayor que yo) vive en el extranjero.",
    'Él preguntó: "¿Estás listo?"| Respondí que sí.',
    'Ella dijo: "No estoy segura."| Luego se fue.',

    # Pronoun heuristic (Ud./Vd.)
    "Me dirijo a Ud., Marco, para saludarlo.",
    "Me dirijo a Ud.| Mañana le enviaré el paquete.",
    "Se lo di a Uds.| Ellos lo confirmaron.",
    "Pregunté por Vds.| Lamentablemente no estaban.",
    "Me dirijo a Ud.| ¿Cuándo me enviará el paquete?",
    "Espero que Ud. comprenda el problema.",

    # Ellipsis
    "El proyecto estaba casi terminado... pero encontramos un problema.",

    # Additions after correction and expansion of rules
    "Tomó la palabra el Excmo. Sr. Alcalde de la ciudad.",
    "La mujer vive en el 2º A.| Tiene dos perros grandes.", # error
    "El Imperio romano cayó en el 476 d. C. según los historiadores.",
    "La ciudad se fundó en el siglo III a. C. en el sur peninsular.", # error
    "La empresa Teleservicio S. A. y su filial Telemóvil S. L. firmaron el acuerdo.",
    "La cooperativa agrícola, Coop. del Sur, está en el pol. ind. Norte.",
    "Fdo.: El director general.",
    "P. D.: No olvides llamar al tlfno. de emergencias en caso de duda.",
    "La iglesia de Ntra. Sra. de la Asunción está al doblar la esquina."
]