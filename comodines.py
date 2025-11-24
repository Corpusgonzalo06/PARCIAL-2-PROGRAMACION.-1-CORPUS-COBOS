from mis_funciones import *

# ===========================
# FUNCIONES DE COMODINES
# ===========================


def revelar_palabras(lista_palabras: list) -> None:
    """
    Esta función muestra por pantalla todas las palabras posibles.

    PARÁMETROS:
        lista_palabras (list): Lista que contiene todas las palabras válidas del nivel.

    RETORNO:
        None: No retorna nada, solo imprime en pantalla.
    """
    texto = ""
    i = 0
    while i < len(lista_palabras):
        texto = texto + lista_palabras[i]
        if i < len(lista_palabras) - 1:
            texto = texto + ", "
        i += 1

    print("💡 Las palabras posibles eran: " + texto)


def eliminar_restricciones(vidas: int) -> int:
    """
    Esta función informa que no se descontará vida en el próximo intento.
    Devuelve la misma cantidad de vidas sin modificarlas.

    PARÁMETROS:
        vidas (int): Cantidad de vidas actuales del jugador.

    RETORNO:
        int: Las vidas sin modificar.
    """
    print("🚀 Restricciones eliminadas. Tenés un intento libre sin perder vida.")
    vidas_actualizadas = vidas
    return vidas_actualizadas


def dar_pista_extra(palabra_base: str) -> None:
    """
    Esta función muestra como pista la primera letra de la palabra base.

    PARÁMETROS:
        palabra_base (str): La palabra principal del nivel.

    RETORNO:
        None: Solo imprime la pista.
    """
    letra = palabra_base[0]
    letra_minuscula = convertir_a_minusculas(letra)
    print("🕵️ Pista extra: Una palabra empieza con '" + letra_minuscula + "'")


def usar_comodin(opcion: int, palabra_base: str, lista_palabras: list, vidas: int) -> int:
    """
    Esta función ejecuta el comodín correspondiente al número elegido.

    PARÁMETROS:
        opcion (int): Número identificador del comodín.
        palabra_base (str): Palabra principal del nivel.
        lista_palabras (list): Lista de palabras válidas.
        vidas (int): Cantidad de vidas del jugador antes de usar el comodín.

    RETORNO:
        int: Cantidad de vidas luego de aplicar el comodín.
    """
    vidas_actualizadas = vidas

    if opcion == 1:
        revelar_palabras(lista_palabras)

    elif opcion == 2:
        vidas_actualizadas = eliminar_restricciones(vidas)

    elif opcion == 3:
        dar_pista_extra(palabra_base)

    else:
        print("⚠️ Comodín desconocido")

    return vidas_actualizadas


def validar_uso_comodin(texto_inicial: str) -> bool:
    """
    Esta función valida si el usuario desea usar un comodín,
    aceptando únicamente las respuestas "si" o "no".

    PARÁMETROS:
        texto_inicial (str): Texto ingresado inicialmente por el usuario.

    RETORNO:
        bool: True si desea usar un comodín, False si no.
    """
    usar_bandera = False
    respuesta_valida = False
    texto = convertir_a_minusculas(texto_inicial)

    while respuesta_valida == False:

        if texto == "si":
            usar_bandera = True
            respuesta_valida = True

        elif texto == "no":
            usar_bandera = False
            respuesta_valida = True

        else:
            print("Por favor, ingresá 'si' o 'no'.")
            texto = convertir_a_minusculas(input("¿Querés usar un comodín? (si/no): "))

    return usar_bandera 


def obtener_comodines_disponibles(comodines_jugador: dict) -> list:
    """
    Esta función obtiene los nombres de los comodines que aún están disponibles.

    PARÁMETROS:
        comodines_jugador (dict): Diccionario donde cada clave es un comodín
                                  y el valor es True (disponible) o False (usado).

    RETORNO:
        list: Lista con los nombres de los comodines que están disponibles.
    """
    disponibles = []

    for nombre in comodines_jugador:
        if comodines_jugador[nombre] == True:
            disponibles = agregar_elemento(disponibles, nombre)

    return disponibles


def mostrar_comodines(disponibles: list) -> None:
    """
    Esta función muestra en pantalla los comodines disponibles,
    numerados en orden.

    PARÁMETROS:
        disponibles (list): Lista con los nombres de los comodines disponibles.

    RETORNO:
        None: Solo imprime la lista.
    """
    print("\n🎁 Comodines disponibles:")
    i = 0
    numero = 1
    while i < len(disponibles):
        print(f"{numero}. {disponibles[i]}")

        numero += 1
        i += 1


def es_numero_valido(texto: str) -> bool:
    """
    Esta función determina si un texto contiene únicamente dígitos.

    PARÁMETROS:
        texto (str): Texto ingresado para validar.

    RETORNO:
        bool: True si todos los caracteres son dígitos, False en caso contrario.
    """
    valido = True

    if len(texto) == 0:
        valido = False

    i = 0
    while valido == True and i < len(texto):
        if texto[i] < '0' or texto[i] > '9':
            valido = False
        i += 1

    return valido


def leer_opcion_numerica(texto: str) -> int:
    """
    Esta función convierte un texto numérico a entero.
    Si el texto no es válido, devuelve None.

    PARÁMETROS:
        texto (str): Texto que representa un número entero.

    RETORNO:
        int | None: El número entero convertido, o None si no era válido.
    """
    resultado = None
    es_val = es_numero_valido(texto)

    if es_val == True:
        resultado = convertir_a_entero(texto)

    return resultado


def manejar_comodines(comodines_jugador: dict, palabra_base: str, lista_palabras: list, vidas_actuales: int) -> int:
    """
    Esta función controla toda la lógica del uso de comodines:
    pregunta al jugador, muestra los disponibles y ejecuta el elegido.

    PARÁMETROS:
        comodines_jugador (dict): Diccionario con el estado de cada comodín.
        palabra_base (str): Palabra principal del nivel.
        lista_palabras (list): Lista de todas las palabras válidas.
        vidas_actuales (int): Cantidad actual de vidas del jugador.

    RETORNO:
        int: Vidas actualizadas luego del uso del comodín (si se usó).
    """

    resultado = vidas_actuales

    usar = validar_uso_comodin(input("¿Querés usar un comodín? (si/no): "))

    if usar == True:

        disponibles = obtener_comodines_disponibles(comodines_jugador)

        if len(disponibles) > 0:

            mostrar_comodines(disponibles)

            opcion_txt = input("Elegí un comodín: ")
            opcion = leer_opcion_numerica(opcion_txt)

            valido = True
            cantidad = len(disponibles)

            if opcion == None:
                print("⚠️ Entrada inválida.")
                valido = False
            elif opcion < 1 or opcion > cantidad:
                print("⚠️ Ese número no corresponde a ningún comodín.")
                valido = False

            if valido == True:
                nombre = disponibles[opcion - 1]
                comodines_jugador[nombre] = False

                if nombre == "revelar_palabras":
                    opcion_comodin = 1
                elif nombre == "eliminar_restricciones":
                    opcion_comodin = 2
                elif nombre == "pista_extra":
                    opcion_comodin = 3
                else:
                    opcion_comodin = 0

                resultado = usar_comodin(opcion_comodin, palabra_base, lista_palabras, resultado)

        else:
            print("⚠️ No te quedan comodines disponibles.")

    return resultado


def crear_comodines_iniciales(valor=True):
    """
    Esta función crea el diccionario que contiene los comodines iniciales.

    PARÁMETROS:
        valor (bool): Valor inicial de cada comodín (True = disponible).

    RETORNO:
        dict: Diccionario con los nombres de los comodines y su disponibilidad.
    """
    revelar_palabras = valor
    eliminar_restricciones = valor
    pista_extra = valor

    comodines = {
        "revelar_palabras": revelar_palabras,
        "eliminar_restricciones": eliminar_restricciones,
        "pista_extra": pista_extra
    }

    return comodines
