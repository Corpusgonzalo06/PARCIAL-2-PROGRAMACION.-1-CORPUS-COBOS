#validaciones.py
from palabras import PALABRAS_POR_NIVEL


def validar_palabra_ingresada(palabra_ingresada, palabra_correcta):
    """
    Compara las palabras sin diferenciar mayúsculas/minúsculas,
    sin usar métodos de string y con un solo return.
    """
    es_valida = True
    vacia = True

    # Verificar si está vacía
    i = 0
    while i < len(palabra_ingresada):
        if palabra_ingresada[i] != " " and palabra_ingresada[i] != "\n" and palabra_ingresada[i] != "\t":
            vacia = False
        i = i + 1

    if vacia:
        print("⚠️ No ingresaste ninguna palabra.")
        es_valida = False

    # Comparar carácter por carácter (sin importar mayúsculas/minúsculas)
    if len(palabra_ingresada) != len(palabra_correcta):
        es_valida = False
    else:
        i = 0
        while i < len(palabra_ingresada):
            letra1 = palabra_ingresada[i]
            letra2 = palabra_correcta[i]

            # Pasar a mayúsculas si es minúscula (ASCII)
            if "a" <= letra1 <= "z":
                letra1 = chr(ord(letra1) - 32)
            if "a" <= letra2 <= "z":
                letra2 = chr(ord(letra2) - 32)

            if letra1 != letra2:
                es_valida = False
            i = i + 1

    return es_valida


def convertir_a_minusculas(palabra):
    """
    Convierte manualmente una palabra a minúsculas sin usar .lower().
    """
    resultado = ""
    for letra in palabra:
        codigo = ord(letra)  # obtiene el código ASCII
        if codigo >= 65 and codigo <= 90:  # rango de letras mayúsculas (A-Z)
            letra_minuscula = chr(codigo + 32)  # convierte a minúscula
            resultado = resultado + letra_minuscula
        else:
            resultado = resultado + letra
    return resultado

def validar_palabra_ingresada(palabra_ingresada, palabra_correcta):
    """
    Verifica si la palabra ingresada es igual a la palabra correcta.
    Retorna True si es correcta, False si no lo es.
    """
    resultado = False
    vacia = True

    # Recorremos con índice
    for i in range(len(palabra_ingresada)):
        if palabra_ingresada[i] != " " and palabra_ingresada[i] != "\n" and palabra_ingresada[i] != "\t":
            vacia = False

    # Verificamos si está vacía o no
    if vacia:
        print("⚠️ No ingresaste ninguna palabra.")
    else:
        if palabra_ingresada == palabra_correcta:
            resultado = True
        else:
            resultado = False

    return resultado


def copiar_lista(lista_original):
    """
    Crea una copia de una lista sin usar .copy().
    """
    nueva_lista = []
    for elemento in lista_original:
        nueva_lista = nueva_lista + [elemento]
    return nueva_lista

def validar_letras_usadas(palabra_ingresada, letras_disponibles):
    """
    Verifica si la palabra ingresada solo usa letras disponibles.
    Lógica simple, sin métodos ni múltiples returns.
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
