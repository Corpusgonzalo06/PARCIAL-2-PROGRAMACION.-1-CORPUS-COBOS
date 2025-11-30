##########################
# FUNCIONES DE PUNTAJE
##########################
import time
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
        None
    """
    usuario["palabras_acertadas"] += 1
    usuario["puntos"] += puntos


def sumar_error(usuario: dict) -> None:
    """
    Registra un error cometido por el usuario al fallar una palabra.

    PARÁMETROS:
        usuario (dict): Diccionario que contiene los datos del usuario.

    RETORNO:
        None
    """
    usuario["palabras_erradas"] += 1


##########################
# FUNCIONES DE RACHAS Y TURNO
##########################

def calcular_puntos_turno(intento: str, racha: int, tiempo_respuesta: float) -> int:
    """
    Calcula los puntos de un turno, sumando bonus por racha.

    PARÁMETROS:
        intento (str): Palabra ingresada por el jugador.
        racha (int): Racha actual de aciertos.
        tiempo_respuesta (float): Tiempo que tardó el jugador en responder.

    RETORNO:
        int: Puntos obtenidos en el turno.
    """
    puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)
    if racha >= 2:
        puntos += 2
    return puntos


def actualizar_racha(racha: int) -> int:
    """
    Incrementa la racha de aciertos.

    PARÁMETROS:
        racha (int): Racha actual.

    RETORNO:
        int: Nueva racha incrementada.
    """
    return racha + 1


def procesar_error_turno(estado_juego: dict, usuario: dict) -> int:
    """
    Procesa un error en el turno: resta vidas y reinicia racha.

    PARÁMETROS:
        estado_juego (dict): Estado actual del juego.
        usuario (dict): Datos del usuario.

    RETORNO:
        int: Racha reiniciada a 0.
    """
    estado_juego["vidas"] -= 1
    racha = 0
    sumar_error(usuario)
    print(f"❌ Incorrecto! Vidas restantes: {estado_juego['vidas']}")
    return racha

def aplicar_puntos(usuario: dict, estado_juego: dict, puntos: int) -> None:
    """
    Descripción:
        Suma los puntos obtenidos en el turno al puntaje total del juego
        y también registra esos puntos en los datos del usuario.

    Parámetros:
        usuario (dict): Diccionario del usuario donde se acumulan los puntos ganados.
        estado_juego (dict): Estado actual del juego, donde se actualiza el puntaje total.
        puntos (int): Cantidad de puntos obtenidos en el intento.

    Retorno:
        None: No retorna ningún valor porque solo actualiza los puntajes
        dentro del usuario y del estado del juego.
    """
    estado_juego["puntaje"] += puntos
    sumar_puntos_por_acierto(usuario, puntos)



def calcular_puntos(intento: str, racha: int) -> int:
    """
    Descripción:
        Calcula los puntos del intento actual usando la palabra ingresada.
        Si el jugador lleva una racha de 2 o más aciertos, se suman puntos extra.

    Parámetros:
        intento (str): Palabra ingresada por el jugador.
        racha (int): Racha de aciertos consecutivos antes del intento.

    Retorno:
        int: Devuelve la cantidad de puntos obtenidos en el intento.
    """
    puntos = calcular_puntos_por_palabra(intento, time.time())
    if racha >= 2:
        puntos += 2
    return puntos

def calcular_puntos(intento: str, racha: int) -> int:
    """
    Descripción:
        Calcula los puntos del intento actual usando la palabra ingresada.
        Si el jugador lleva una racha de 2 o más aciertos, se suman puntos extra.

    Parámetros:
        intento (str): Palabra ingresada por el jugador.
        racha (int): Racha de aciertos consecutivos antes del intento.

    Retorno:
        int: Devuelve la cantidad de puntos obtenidos en el intento.
    """
    puntos = calcular_puntos_por_palabra(intento, time.time())
    if racha >= 2:
        puntos += 2
    return puntos

def actualizar_racha(racha: int) -> int:
    """
    Descripción:
        Aumenta en 1 la racha actual de aciertos.

    Parámetros:
        racha (int): Número actual de aciertos consecutivos.

    Retorno:
        int: Devuelve la racha actualizada después del acierto.
    """
    racha = racha + 1
    return racha


def calcular_puntos_turno(intento: str, racha: int, tiempo_respuesta: float) -> int:
    """
    Descripción:
        Calcula los puntos obtenidos en un turno considerando la palabra ingresada,
        el tiempo de respuesta y la racha actual de aciertos. A partir de 2 de racha,
        se aplican puntos adicionales.

    Parámetros:
        intento (str): Palabra ingresada por el jugador.
        racha (int): Racha de aciertos consecutivos antes del intento.
        tiempo_respuesta (float): Tiempo exacto del intento, usado para el cálculo de puntos.

    Retorno:
        int: Devuelve los puntos conseguidos en el turno.
    """
    puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)
    if racha >= 2:
        puntos += 2
    return puntos
