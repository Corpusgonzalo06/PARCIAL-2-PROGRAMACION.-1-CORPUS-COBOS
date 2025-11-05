#validaciones.py
from palabras import PALABRAS_POR_NIVEL

def validar_palabra_ingresada(palabra_ingresada, palabra_correcta):
    """
    Verifica si la palabra ingresada coincide con la palabra correcta.

    PARAMETROS:
    palabra_ingresada (str): Palabra escrita por el jugador.
    palabra_correcta (str): Palabra que se espera adivinar.

    DEVUELVE:
    bool: True si coinciden, False si no o si la entrada está vacía.
    """
    resultado = False
    vacia = True

    for i in range(len(palabra_ingresada)):
        if palabra_ingresada[i] != " " and palabra_ingresada[i] != "\n" and palabra_ingresada[i] != "\t":
            vacia = False

    if vacia:
        print("⚠️ No ingresaste ninguna palabra.")
    else:
        if palabra_ingresada == palabra_correcta:
            resultado = True
        else:
            resultado = False

    return resultado


def convertir_a_minusculas(palabra):
    """
    Convierte todas las letras de una palabra a minúsculas.

    PARAMETROS:
    palabra (str): Palabra a convertir.

    DEVUELVE:
    str: Palabra con todas sus letras en minúsculas.
    """
    resultado = ""
    for letra in palabra:
        codigo = ord(letra)
        if codigo >= 65 and codigo <= 90:
            letra_minuscula = chr(codigo + 32)
            resultado = resultado + letra_minuscula
        else:
            resultado = resultado + letra
    return resultado


def copiar_lista(lista_original):
    """
    Crea una copia de una lista.

    PARAMETROS:
    lista_original (list): Lista que se quiere copiar.

    DEVUELVE:
    list: Nueva lista con los mismos elementos de la original.
    """
    nueva_lista = []
    for elemento in lista_original:
        nueva_lista = nueva_lista + [elemento]
    return nueva_lista


def validar_letras_usadas(palabra_ingresada, letras_disponibles):
    """
    Verifica que todas las letras de la palabra ingresada estén disponibles en la lista de letras.

    PARAMETROS:
    palabra_ingresada (str): Palabra que el jugador escribió.
    letras_disponibles (list): Lista de letras que se pueden usar.

    DEVUELVE:
    bool: True si todas las letras están disponibles, False si alguna no lo está.
    """
    palabra_valida = True
    palabra_minuscula = convertir_a_minusculas(palabra_ingresada)
    letras_copia = copiar_lista(letras_disponibles)

    i = 0
    while i < len(palabra_minuscula) and palabra_valida:
        letra_actual = palabra_minuscula[i]
        letra_encontrada = False

        j = 0
        while j < len(letras_copia) and not letra_encontrada:
            if letra_actual == letras_copia[j]:
                letras_copia[j] = "✔"
                letra_encontrada = True
            j += 1

        if not letra_encontrada:
            print("⚠️ La letra", letra_actual, "no está disponible.")
            palabra_valida = False

        i += 1

    return palabra_valida
