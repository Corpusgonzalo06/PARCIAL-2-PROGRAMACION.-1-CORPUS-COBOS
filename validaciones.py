# validaciones.py
from palabras import PALABRAS_POR_NIVEL
from mis_funciones import * 

def validar_palabra_ingresada(palabra_ingresada: str, palabra_correcta: str) -> bool:
    """
    Verifica si la palabra ingresada coincide con la palabra correcta,
    sin diferenciar mayúsculas/minúsculas.

    PARAMETROS:
    palabra_ingresada (str): Palabra escrita por el jugador.
    palabra_correcta (str): Palabra que se espera adivinar.

    DEVUELVE:
    bool: True si coinciden, False si no o si la entrada está vacía.
    """
    resultado = False
    vacia = True

    # Verificar si la palabra ingresada no está vacía
    for i in range(len(palabra_ingresada)):
        if palabra_ingresada[i] != " " and palabra_ingresada[i] != "\n" and palabra_ingresada[i] != "\t":
            vacia = False

    if vacia:
        print("⚠️ No ingresaste ninguna palabra.")
    else:
        # Convertimos ambas palabras a minúsculas antes de comparar
        if convertir_a_minusculas(palabra_ingresada) == convertir_a_minusculas(palabra_correcta):
            resultado = True
        else:
            resultado = False

    return resultado


def validar_letras_usadas(palabra_ingresada: str, letras_disponibles: list) -> bool:
    """
    Verifica que todas las letras de la palabra ingresada estén disponibles en la lista de letras,
    sin diferenciar mayúsculas/minúsculas.

    PARAMETROS:
    palabra_ingresada (str): Palabra que el jugador escribió.
    letras_disponibles (list): Lista de letras que se pueden usar.

    DEVUELVE:
    bool: True si todas las letras están disponibles, False si alguna no lo está.
    """
    palabra_valida = True
    palabra_minuscula = convertir_a_minusculas(palabra_ingresada)
    letras_copia = convertir_lista_a_minusculas(letras_disponibles)

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
