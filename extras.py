# extras.py

def mostrar_letras(lista_letras):
    """
    Muestra las letras desordenadas de forma visual.
    Sin usar join().
    """
    print("\n🔠 Letras disponibles:")


    texto = ""
    for i in range(len(lista_letras)):
        texto = texto + lista_letras[i]
        if i < len(lista_letras) - 1:
            texto = texto + " | "

    print(texto)
    print("------------------------------")


def mostrar_resumen_nivel(nivel, puntaje, vidas_restantes):
    """
    Muestra un resumen del nivel al finalizarlo.
    Sin usar time.sleep().
    """
    print("\n--------------------------------------")
    print("🏁 Fin del Nivel", nivel)
    print("⭐ Puntaje acumulado:", puntaje)
    print("❤️ Vidas restantes:", vidas_restantes)
    print("--------------------------------------")

    
    input("Presioná ENTER para continuar...")
