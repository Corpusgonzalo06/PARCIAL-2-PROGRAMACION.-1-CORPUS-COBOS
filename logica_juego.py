#logica_juego.py
from funciones_auxiliares import *
from validaciones import *


def jugar_partida(palabra_correcta, vidas, puntaje):
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


def jugar_nivel(nivel, vidas_totales, puntaje, reinicios):
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


def iniciar_juego():
    vidas = 3
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
