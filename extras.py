# extras.py
def mostrar_letras(lista_letras):
    """
    Muestra en pantalla las letras de la lista separadas por "|".

    Parámetros:
    lista_letras (list): Lista de letras a mostrar.

    Devuelve:
    None: No devuelve ningún valor, solo imprime las letras en pantalla.
    """
    print("\n🔠 Letras disponibles:")

    texto = ""
    for i in range(len(lista_letras)):
        texto += lista_letras[i]
        if i < len(lista_letras) - 1:
            texto += " | "

    print(texto)
    print("------------------------------")

def mostrar_resumen_nivel(nivel, puntaje, vidas_restantes):
    """
    Muestra en pantalla un resumen del nivel con puntaje y vidas restantes.

    Parámetros:
    nivel (int): Número del nivel finalizado.
    puntaje (int): Puntaje acumulado hasta el momento.
    vidas_restantes (int): Cantidad de vidas que le quedan al jugador.

    Devuelve:
    None: No devuelve ningún valor, solo muestra la información en pantalla.
    """
    print("\n--------------------------------------")
    print("🏁 Fin del Nivel", nivel)
    print("⭐ Puntaje acumulado:", puntaje)
    print("❤️ Vidas restantes:", vidas_restantes)
    print("--------------------------------------")

    input("Presioná ENTER para continuar...")
