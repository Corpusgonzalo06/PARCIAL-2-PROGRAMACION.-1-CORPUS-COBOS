#logica_juego.py
from funciones_auxiliares import *
from validaciones import *


def jugar_partida(palabra_correcta: str, vidas: int, puntaje: int) -> tuple:
    """
 Juega una partida para adivinar la palabra y actualiza puntaje y vidas.


    PARAMETROS:
    palabra_correcta (str): La palabra que el jugador debe adivinar.
    vidas (int): Cantidad de vidas disponibles al inicio de la partida.
    puntaje (int): Puntaje acumulado antes de comenzar la partida.

    DEVUELVE:
    tuple: (puntaje_actualizado, vidas_restantes) luego de la partida.
    """
    letras = preparar_palabra_desordenada(palabra_correcta)
    mostrar_letras(letras)

    acierto = False
    puntos = 0

    while vidas > 0 and not acierto:
        intento = input("✏️ Ingresá una palabra: ")
        palabra_valida = validar_palabra_ingresada(intento, palabra_correcta)

        if palabra_valida:
            puntos = len(intento)
            puntaje = puntaje + puntos
            print("✅ ¡Correcto! Ganaste", puntos, "puntos.")
            acierto = True
        else:
            vidas = vidas - 1
            print("❌ Incorrecto. Te quedan", vidas, "vidas.")

    return puntaje, vidas



def jugar_nivel(nivel: int, vidas_totales: int, puntaje: int, reinicios: int) -> tuple:
    """
    Juega todas las partidas de un nivel y actualiza puntaje, vidas y estado del nivel.

    PARAMETROS:
    nivel (int): Número del nivel.
    vidas_totales (int): Vidas disponibles al iniciar el nivel.
    puntaje (int): Puntaje acumulado antes del nivel.
    reinicios (int): Cantidad de reinicios disponibles si se pierden todas las vidas.

    DEVUELVE:
    tuple: (puntaje_actualizado, reinicios_restantes, nivel_superado)
    """
    mostrar_encabezado_de_nivel(nivel)
    palabras = obtener_palabras_del_nivel(nivel)
    nivel_superado = False
    vidas = vidas_totales
    partidas = 0

    if len(palabras) == 0:
        print("⚠️ No hay palabras cargadas para el nivel", nivel)
    else:
        while partidas < 3 and vidas > 0:
            print("\n👉 Partida", partidas + 1, "de 3")
            indice = random.randint(0, len(palabras) - 1)
            palabra = palabras[indice]
            puntaje, vidas = jugar_partida(palabra, vidas, puntaje)

            if vidas > 0:
                partidas = partidas + 1

        if vidas > 0:
            print("\n🎉 ¡Nivel", nivel, "superado! Puntaje:", puntaje)
            nivel_superado = True
        else:
            print("\n💀 Perdiste todas las vidas.")
            reinicios = reinicios - 1
            if reinicios > 0:
                print("🔁 Reiniciando nivel... Reinicios restantes:", reinicios)
            else:
                print("🚫 Fin del juego. Puntaje final:", puntaje)

    return puntaje, reinicios, nivel_superado


def iniciar_juego(vidas: int = 3) -> None: #parametro opcional / por defecto
    """
    Inicia el juego completo, manejando niveles, vidas, reinicios y puntaje.

    PARAMETROS:
    vidas (int): cantidad de vidas iniciales, por defecto 3

    DEVUELVE:
    None: No devuelve ningún valor, solo ejecuta el flujo completo del juego.
    """
    reinicios = 2
    nivel = 1
    puntaje = 0
    continuar = True

    mostrar_encabezado_de_juego()

    while nivel <= 5 and reinicios >= 0 and continuar:
        puntaje, reinicios, nivel_superado = jugar_nivel(nivel, vidas, puntaje, reinicios)

        if nivel_superado:
            nivel = nivel + 1
        else:
            if reinicios < 0:
                continuar = False

    if nivel > 5:
        print("\n🏆 ¡FELICIDADES! Completaste los 5 niveles.")

    print("Puntaje final:", puntaje)

