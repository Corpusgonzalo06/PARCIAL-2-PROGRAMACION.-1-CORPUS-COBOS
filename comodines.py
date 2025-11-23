from mis_funciones import *

# ===========================
# FUNCIONES DE COMODINES
# ===========================


def revelar_palabra(lista_palabras: list) -> None:
    """
    Muestra por pantalla todas las palabras posibles sin usar join().
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
    Devuelve la cantidad de vidas sin modificarlas, pero mostrando el mensaje.
    """
    print("🚀 Restricciones eliminadas. Tenés un intento libre sin perder vida.")
    vidas_actualizadas = vidas
    return vidas_actualizadas


def dar_pista_extra(palabra_base: str) -> None:
    """
    Muestra la primera letra como pista, convertida a minúsculas.
    """
    letra = palabra_base[0]
    letra_minuscula = convertir_a_minusculas(letra)
    print("🕵️ Pista extra: la palabra empieza con '" + letra_minuscula + "'")


def usar_comodin(opcion: int, palabra_base: str, lista_palabras: list, vidas: int) -> int:
    """
    Ejecuta el comodín elegido y devuelve la cantidad de vidas resultante.
    """
    vidas_actualizadas = vidas

    if opcion == 1:
        revelar_palabra(lista_palabras)

    elif opcion == 2:
        vidas_actualizadas = eliminar_restricciones(vidas)

    elif opcion == 3:
        dar_pista_extra(palabra_base)

    else:
        print("⚠️ Comodín desconocido")

    return vidas_actualizadas


def validar_uso_comodin(texto_inicial: str) -> bool:
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
    disponibles = []

    for nombre in comodines_jugador:
        if comodines_jugador[nombre] == True:
            disponibles = agregar_elemento(disponibles, nombre)

    return disponibles


def mostrar_comodines(disponibles: list) -> None:
    """
    Muestra los comodines disponibles numerados.
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
    Verifica si un texto está compuesto solo por dígitos.
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
    Devuelve un entero válido o None si no es numérico.
    """
    resultado = None
    es_val = es_numero_valido(texto)

    if es_val == True:
        resultado = convertir_a_entero(texto)

    return resultado



def manejar_comodines(comodines_jugador: dict, palabra_base: str, lista_palabras: list, vidas_actuales: int) -> int:
    """
    Maneja el uso de comodines durante la partida.
    Devuelve la cantidad de vidas actualizada con un único return.
    """

    resultado = vidas_actuales  # guardamos el valor final que vamos a retornar

    usar = validar_uso_comodin(input("¿Querés usar un comodín? (si/no): "))

    if usar == True:

        disponibles = obtener_comodines_disponibles(comodines_jugador)

        if len(disponibles) > 0:

            mostrar_comodines(disponibles)

            opcion_txt = input("Elegí un comodín: ")
            opcion = leer_opcion_numerica(opcion_txt)

            valido = True
            cantidad = len(disponibles)

            if opcion is None:
                print("⚠️ Entrada inválida.")
                valido = False
            elif opcion < 1 or opcion > cantidad:
                print("⚠️ Ese número no corresponde a ningún comodín.")
                valido = False

            if valido == True:
                nombre = disponibles[opcion - 1]
                comodines_jugador[nombre] = False
                resultado = usar_comodin(opcion, palabra_base, lista_palabras, resultado)

        else:
            print("⚠️ No te quedan comodines disponibles.")

    return resultado