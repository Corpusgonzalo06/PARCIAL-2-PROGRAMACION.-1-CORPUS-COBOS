from mis_funciones import *

def revelar_palabra(palabra_correcta: str) -> None:
    """
    Muestra en pantalla la palabra correcta.

    PARAMETROS:
    palabra_correcta (str): Palabra que se debe mostrar.

    DEVUELVE:
    None: Solo imprime la palabra, no retorna valor.
    """
    print("💡 La palabra correcta era: " + palabra_correcta)


def eliminar_restricciones(vidas: int) -> int:
    """
    Permite al jugador tener un intento libre sin perder vida.

    PARAMETROS:
    vidas (int): Cantidad actual de vidas del jugador.

    DEVUELVE:
    int: Cantidad de vidas sin cambios.
    """
    print("🚀 Restricciones eliminadas. Tenés un intento libre sin perder vida.")
    return vidas


def dar_pista_extra(palabra_correcta: str) -> None:
    """
    Muestra una pista extra indicando la primera letra de la palabra.

    PARAMETROS:
    palabra_correcta (str): Palabra de la cual se obtiene la pista.

    DEVUELVE:
    None: Solo imprime la pista, no retorna valor.
    """
    primera_letra = palabra_correcta[0]
    letra_minuscula = convertir_a_minusculas(primera_letra)
    print(f"🕵️ Pista extra: la palabra empieza con '{letra_minuscula}'")


def usar_comodin(opcion: int, palabra_correcta: str, vidas: int) -> int:
    """
    Ejecuta la acción del comodín seleccionado.

    PARAMETROS:
    opcion (int): Número del comodín elegido.
    palabra_correcta (str): Palabra correcta de la partida.
    vidas (int): Cantidad actual de vidas.

    DEVUELVE:
    int: Cantidad actual de vidas tras usar el comodín.
    """
    match opcion:
        case 1:
            revelar_palabra(palabra_correcta)
        case 2:
            vidas = eliminar_restricciones(vidas)
        case 3:
            dar_pista_extra(palabra_correcta)
        case _:
            print("⚠️ Comodín desconocido")
    return vidas


def preguntar_uso_comodin() -> bool:
    """
    Pregunta al jugador si desea usar un comodín.

    DEVUELVE:
    bool: True si desea usar, False si no.
    """
    usar = input("¿Querés usar un comodín? (s/n): ")
    resultado = False
    if usar == "s":
        resultado = True
    return resultado


def obtener_comodines_disponibles(comodines_jugador: dict) -> list:
    """
    Obtiene la lista de comodines que todavía están disponibles.

    PARAMETROS:
    comodines_jugador (dict): Diccionario con los comodines y su disponibilidad.

    DEVUELVE:
    list: Lista con los nombres de los comodines disponibles.
    """
    disponibles = []
    for nombre in comodines_jugador:
        if comodines_jugador[nombre] == True:
            disponibles
