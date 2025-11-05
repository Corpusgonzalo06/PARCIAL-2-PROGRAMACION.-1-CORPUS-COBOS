#funciones_auxiliares.py
import random
from palabras import PALABRAS_POR_NIVEL

def mostrar_encabezado_de_juego() ->None:
    """
    Muestra en pantalla el encabezado de bienvenida y la explicación del objetivo del juego.

    PARAMETRO:
    Ninguno

    DEVUELVE:
    None: No devuelve ningún valor, solo imprime el encabezado en pantalla.
    """
    print()
    print()
    print("BIENVENIDO A 'ADIVINA EL JUEGO'.")
    print("==============================")
    print("🔥 DESCUBRÍ LA PALABRA 🎯")
    print("==> Objetivo: formar palabras correctas con las letras disponibles.\n")


def mostrar_encabezado_de_nivel(nivel: int) -> None:
    """
    Muestra en pantalla el encabezado del nivel actual.

    PARAMETROS:
    nivel (int): Número del nivel que se está jugando.

    DEVUELVE:
    None: No devuelve ningún valor, solo imprime el encabezado en pantalla.
    """
    print(f"\n========== NIVEL {nivel} ==========")

def obtener_palabras_del_nivel(nivel: int) -> list:
    """
    Obtiene las palabras que corresponden a un nivel específico del juego.

    PARAMETROS:
    nivel (int): Número del nivel del que se quieren obtener las palabras.

    DEVUELVE:
    list: Lista con las palabras del nivel. Si el nivel no existe, devuelve una lista vacía.
    """
    if nivel in PALABRAS_POR_NIVEL:
        palabras = PALABRAS_POR_NIVEL[nivel]
    else:
        palabras = []
    return palabras


def preparar_palabra_desordenada(palabra: str) -> list:
    """
    Toma una palabra y devuelve sus letras en orden aleatorio (desordenadas).

    PARAMETROS:
    palabra (str): Palabra que se quiere desordenar.

    DEVUELVE:
    (list): Lista con las letras de la palabra mezcladas en orden aleatorio.
    """
    letras = []
    i = 0
    while i < len(palabra):
        letras += [palabra[i]]
        i = i + 1

    n = len(letras)
    i = 0
    while i < n:
        aleatorio = random.randint(0, n - 1)
        temporal = letras[i]
        letras[i] = letras[aleatorio]
        letras[aleatorio] = temporal
        i = i + 1

    return letras

def mostrar_letras(letras: list) -> None:
    """
    Muestra en pantalla las letras disponibles de la lista, separadas por espacio.

    Parámetros:
    letras (list): Lista de letras a mostrar.

    Devuelve:
    (None): No devuelve ningún valor, solo imprime las letras en pantalla.
    """
    print("\n🔠 Letras disponibles:")
    i = 0
    while i < len(letras):
        print(letras[i], end=" ")
        i = i + 1
    print("\n------------------------------")
