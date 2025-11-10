def crear_mi_separador(texto: str, separador: str) -> list:
    """
    Separa un texto en palabras usando un carácter separador.

    PARAMETROS:
    texto (str) -> Texto a separar.
    separador (str) -> Carácter que define dónde cortar el texto.

    DEVUELVE:
    list -> Lista con las palabras resultantes.
    """
    resultado = []
    palabra = ""
    i = 0
    while i < len(texto):
        if texto[i] == separador:
            resultado = resultado + [palabra]
            palabra = ""
        else:
            palabra = palabra + texto[i]
        i += 1
    resultado = resultado + [palabra]
    return resultado


def convertir_lista_a_minusculas(lista: list) -> list:
    """
    Convierte todas las letras de una lista a minúsculas usando códigos ASCII.

    PARAMETROS:
    lista (list) -> Lista de caracteres (str) que se quieren convertir.

    DEVUELVE:
    list -> Nueva lista con los mismos caracteres pero en minúscula.
    """
    resultado = []
    i = 0
    while i < len(lista):
        letra = lista[i]
        codigo = ord(letra)
        if codigo >= 65 and codigo <= 90:
            resultado = resultado + [chr(codigo + 32)]
        else:
            resultado = resultado + [letra]
        i += 1
    return resultado


def convertir_a_minusculas(palabra: str) -> str:
    """
    Convierte una palabra completa a minúsculas usando códigos ASCII.

    PARAMETROS:
    palabra (str) -> Palabra que se quiere convertir.

    DEVUELVE:
    str -> Palabra convertida a minúsculas.
    """
    resultado = ""
    i = 0
    while i < len(palabra):
        letra = palabra[i]
        codigo = ord(letra)
        if codigo >= 65 and codigo <= 90:
            resultado = resultado + chr(codigo + 32)
        else:
            resultado = resultado + letra
        i += 1
    return resultado


def copiar_lista(lista_original: list) -> list:
    """
    Crea una copia de una lista sin usar métodos de Python.

    PARAMETROS:
    lista_original (list) -> Lista que se desea copiar.

    DEVUELVE:
    list -> Nueva lista con los mismos elementos que la original.
    """
    nueva_lista = []
    i = 0
    while i < len(lista_original):
        nueva_lista = nueva_lista + [lista_original[i]]
        i += 1
    return nueva_lista
