ISO_CODE = "es"
TEST_DATA = [
    # Basic punctuation
    "Hola mundo.| ¿Cómo estás?| Bien, gracias.",
    "¿Cuál es tu nombre?| Me llamo Carlos.",
    "¿Viste la película anoche?.| Sí, fue increíble.| ¡Me encantó!| La actuación fue excelente.",

    # Abbreviations
    "El Sr. García llegó ayer.| La Sra. López también.",
    "La Profe. María dio una conferencia.",
    "El Lcdo. Pérez y el Mag. Torres son amigos.",
    "D. José y Dña. María son los dueños.",
    "El Cmdte. Rodríguez saludó al Cnel. Díaz.",
    "Véase la pág. 55 del libro.",
    "Vea el cap. 3 en el t. II de la obra.",
    "El art. 4 y el nro. 8 son clave.",
    "Se les pidió a los niños que leyeran los párrf. 5 y 6 del art. 4 de la constitución.",
    "Consulte el párr. 5 para más información.",
    "Llama al dir. general al tel. 555-1234.",
    "Compré pan, leche, etc. para la cena.",
    "La temperatura del motor alcanzó los 120,5 °C.| Afortunadamente, el sistema siguió funcionando.",
    "La ruta mide 10 km.| Después comienza el sendero.",
    "Lea p. ej. el capítulo 5.",
    "La reunión es el lun. 15 de enero.",
    "Nació el 5 de abr. de 1990.",
    "El presidente de los EE. UU. visitó Europa.",
    "Las FF.AA. emitieron un comunicado oficial.",
    "Murió en el 44 a. C. en Roma.",
    "Nació en el 63 a. C. y murió en el 14 d. C.| Fue emperador.",
    "Vivió del 100 a.C. al 44 d.C. en Roma.",
    "Murió en el 149 a. C.| Fue enterrado en Roma.",
    "El departamento de RR.HH. aprobó las vacaciones.",
    "La empresa Rodríguez y Cía. firmó el contrato junto con la Asoc. Internacional de Comercio.",
    "Trabaja en la Asoc.| Mañana tiene una reunión.",
    "Tomó la palabra el Excmo. Sr. Alcalde de la ciudad.",
    "La cooperativa agrícola está en el pol. ind. del Puerto.",
    "Fdo.: El director general.",
    "La iglesia de Ntra. Sra. de la Asunción está al doblar la esquina.",

    # Structural headings
    "Capítulo 1. El comienzo.| Estaba oscuro afuera. | Nada se movía.",
    "Parte II. Introducción.| El sistema comienza aquí. | La inicialización sigue.",
    "El informe fue completado.| Capítulo 3. Análisis de resultados.",

    # Addresses & Locations
    "Vive en la av. Siempre Viva.",
    "Viven en la c. Mayor, 12.",
    "El accidente fue en la cra. 50 con cll. 100.",
    "Dobla en la transv. 3 y sigue por la diag. 5.",
    "La casa está en la urb. Las Rosas, mz. A, lt. 15 del asent. Humano.",
    "El apartamento está en la c/ de Quevedo núm. 20, blq. B, esc. 2. ",
    "La mujer vive en el 2º A.| Tiene dos perros grandes.",

    # Common Starters after abbreviations
    "Llegó el Sr. Por suerte trajo el paquete.",
    "Fui a la Cra. Para ver el desfile.",
    "Llegó el Sr. García.| Como no estaba, se fue.",

    # Parentheses and quotes
    "El problema —¿y quién lo iba a decir?— fue resuelto rápido.",
    "La decisión —¡increíblemente difícil!— cambió todo.",
    'Él preguntó: "¿Estás listo?"| Respondí que sí.',
    'Ella dijo: "No estoy segura."| Luego se fue.',
    "Mi hermano (que es mayor que yo) vive en el extranjero.",

    # Pronoun heuristic (Ud./Vd.)
    "Me dirijo a Ud., Marco, para saludarlo.",
    "Me dirijo a Ud.| Mañana le enviaré el paquete.",
    "Se lo di a Uds.| Ellos lo confirmaron.",
    "Pregunté por Vds.| Lamentablemente no estaban.",
    "Me dirijo a Ud.| ¿Cuándo me enviará el paquete?",
    "Espero que Ud. comprenda el problema.",

    # Ellipsis
    "El proyecto estaba casi terminado... pero encontramos un problema.",
]
