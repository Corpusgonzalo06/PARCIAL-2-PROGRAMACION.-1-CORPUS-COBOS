##########################
# FUNCIONES DE PUNTAJE
##########################

def calcular_puntos_por_palabra(palabra: str, tiempo_respuesta: float) -> int:
    """
    Calcula los puntos obtenidos según la palabra ingresada y el tiempo de respuesta.

    PARÁMETROS:
        palabra (str): Palabra ingresada por el usuario.
        tiempo_respuesta (float): Tiempo en segundos que tardó el usuario en responder.

    RETORNO:
        int: Cantidad total de puntos otorgados por la palabra.
    """
    puntos = len(palabra)

    if len(palabra) > 4:
        puntos += 2

    if tiempo_respuesta < 5:
        puntos += 3
    elif tiempo_respuesta < 10:
        puntos += 1

    return puntos


def sumar_puntos_por_acierto(usuario: dict, puntos: int) -> None:
    """
    Suma los puntos obtenidos por un acierto y actualiza las estadísticas del usuario.

    PARÁMETROS:
        usuario (dict): Diccionario que contiene los datos del usuario.
        puntos (int): Cantidad de puntos ganados por la palabra acertada.

    RETORNO:
        None: No retorna nada. Solo modifica los datos del usuario.
    """
    usuario["palabras_acertadas"] += 1
    usuario["puntos"] += puntos


def sumar_error(usuario: dict) -> None:
    """
    Registra un error cometido por el usuario al fallar una palabra.

    PARÁMETROS:
        usuario (dict): Diccionario que contiene los datos del usuario.

    RETORNO:
        None: No retorna nada, solo actualiza el contador de errores del usuario.
    """
    usuario["palabras_erradas"] += 1
