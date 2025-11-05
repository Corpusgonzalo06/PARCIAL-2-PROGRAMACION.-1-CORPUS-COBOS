#funciones_auxiliares.py
import random
from palabras import PALABRAS_POR_NIVEL
def mostrar_encabezado_de_juego():
    print()
    print()
    print("BIENVENIDO A 'ADIVINA EL JUEGO'.")
    print("==============================")
    print("🔥 DESCUBRÍ LA PALABRA 🎯")
    print("==> Objetivo: formar palabras correctas con las letras disponibles.\n")


def mostrar_encabezado_de_nivel(nivel):
    print(f"\n========== NIVEL {nivel} ==========")


def obtener_palabras_del_nivel(nivel):
    if nivel in PALABRAS_POR_NIVEL:
        palabras = PALABRAS_POR_NIVEL[nivel]
    else:
        palabras = []
    return palabras


def preparar_palabra_desordenada(palabra):
    letras = []
    i = 0
    while i < len(palabra):
        letras += [palabra[i]]
        i = i + 1

    # Mezclar manualmente
    n = len(letras)
    i = 0
    while i < n:
        aleatorio = random.randint(0, n - 1)
        temporal = letras[i]
        letras[i] = letras[aleatorio]
        letras[aleatorio] = temporal
        i = i + 1

    return letras


def mostrar_letras(letras):
    print("\n🔠 Letras disponibles:")
    i = 0
    while i < len(letras):
        print(letras[i], end=" ")
        i = i + 1
    print("\n------------------------------")