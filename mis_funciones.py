
import random
from palabras import *

def convertir_a_minusculas(palabra: str) -> str:
    """
    Convierte una palabra completa a minúsculas usando códigos ASCII.

    Parámetros:
        palabra (str): Palabra a convertir.

    Retorna:
        str: Palabra convertida a minúsculas.
    """
    resultado = ""
    i = 0
    while i < len(palabra):
        letra = palabra[i]
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            resultado = resultado + chr(codigo + 32)
        else:
            resultado = resultado + letra
        i += 1
    return resultado




def crear_mi_separador(texto: str, separador: str) -> list:
    """
    Separa un texto en palabras usando un carácter separador.

    Parámetros:
        texto (str): Texto a separar.
        separador (str): Carácter que define dónde cortar el texto.

    Retorna:
        list: Lista con las palabras resultantes.
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






def agregar_elemento(lista: list, elemento) -> list:
    """
    Devuelve una nueva lista con el elemento agregado al final

    Parámetros:
        lista (list): Lista original.
        elemento: Elemento a agregar.

    Retorna:
        list: Nueva lista con el elemento agregado.
    """
    nueva = []
    i = 0
    while i < len(lista):
        nueva = nueva + [lista[i]]
        i += 1
    nueva = nueva + [elemento]
    return nueva




def convertir_a_entero(texto: str) -> int:
    """
    Convierte un texto numérico a entero.
    """
    numero = 0                            
    i = 0                                 

    while i < len(texto):                  
        digito = ord(texto[i]) - ord('0')  
                                           

        numero = numero * 10 + digito     
                                           

        i += 1                             

    return numero                        







def convertir_a_entero(texto: str) -> int:
    """
    Convierte un texto numérico a su valor entero equivalente usando código ASCII.

    Parámetros:
        texto (str): Cadena formada por dígitos ('0' a '9') que representan un número.

    Retorna:
        int: El número entero obtenido al interpretar todos los caracteres del texto.
    """

    numero = 0                         
    i = 0                                

    while i < len(texto):                 
        digito = ord(texto[i]) - ord('0')   

        numero = numero * 10 + digito      
                                           

        i += 1                             
    return numero




def seleccionar_palabra_y_lista(diccionario: dict) -> tuple:
    """
    Selecciona aleatoriamente una palabra y su lista asociada
    de un diccionario.

    Parámetros:
        diccionario (dict): Diccionario con palabras como claves y listas como valores.

    Retorna:
        tuple: Tupla con la palabra seleccionada (str) y su lista (list).
    """
    claves = []
    for clave in diccionario:
        claves += [clave]

    longitud = 0
    for i in claves:
        longitud += 1

    indice_aleatorio = random.randint(0, longitud - 1)
    palabra = claves[indice_aleatorio]
    lista = diccionario[palabra]

    return palabra, lista


def limpiar_texto(texto: str) -> str:
    """
    Elimina espacios al inicio y al final de un texto


    Parámetros:
        texto (str): Texto a limpiar.

    Retorna:
        str: Texto limpio sin espacios al inicio ni al final.
    """
    longitud = 0
    for i in texto:
        longitud += 1

    inicio = 0
    while inicio < longitud and texto[inicio] == " ":
        inicio += 1

    fin = longitud - 1
    while fin >= 0 and texto[fin] == " ":
        fin -= 1

    limpio = ""
    indice = inicio
    while indice <= fin:
        limpio += texto[indice]
        indice += 1

    return limpio








def desordenar_letras(palabra: str, dificultad: int = 2) -> str:
    """
    Devuelve la palabra con sus letras desordenadas según la dificultad.

    Parámetros:
        palabra (str): Palabra a desordenar.
        dificultad (int): Nivel de desorden (cantidad de pasadas). Default=2

    Retorna:
        str: Palabra con letras desordenadas.
    """
    lista_letras = []
    for letra in palabra:
        lista_letras = agregar_elemento(lista_letras, letra)

    longitud = 0
    for _ in lista_letras:
        longitud += 1

    for i in range(dificultad):
        for j in range(longitud):
            r = random.randint(0, longitud - 1)
            lista_letras[i], lista_letras[r] = lista_letras[r], lista_letras[i]

    desordenada = ""
    indice = 0
    while indice < longitud:
        desordenada += lista_letras[indice]
        indice += 1

    return desordenada
