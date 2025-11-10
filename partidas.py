
import csv
import random

def cargar_palabras_por_categoria(ruta_archivo: str = "partidas.csv") -> dict:
    """
    Carga palabras desde un archivo CSV agrupadas por categoría.

    PARAMETROS:
    ruta_archivo (str) -> Ruta del archivo CSV donde se encuentran las palabras.

    DEVUELVE:
    dict -> Diccionario con las categorías como claves y listas de palabras como valores.
            Si el archivo no existe, devuelve un diccionario vacío.
    """
    categorias = {}
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            primera_fila = True
            for fila in lector_csv:
                if primera_fila:
                    primera_fila = False
                    continue
                categoria = fila[0]
                palabra = fila[1]
                if categoria not in categorias:
                    categorias[categoria] = []
                categorias[categoria] += [palabra]
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo partidas.csv")
    return categorias


def generar_nivel_aleatorio(diccionario_palabras: dict, cant_categorias: int = 4, palabras_por_categoria: int = 4) -> list:
    """
    Genera una lista de palabras aleatorias para un nivel de juego, seleccionando
    categorías y palabras de manera que no se repitan.

    PARAMETROS:
    diccionario_palabras (dict) -> Diccionario {categoria: [palabras]}.
    cant_categorias (int) -> Cantidad de categorías a seleccionar para el nivel.
    palabras_por_categoria (int) -> Cantidad de palabras a elegir por categoría.

    DEVUELVE:
    list -> Lista de palabras seleccionadas aleatoriamente para el nivel.
    None -> Si no hay suficientes categorías disponibles para generar el nivel.
    """
    categorias = []
    for clave in diccionario_palabras:
        categorias += [clave]

    if len(categorias) < cant_categorias:
        print("⚠️ No hay suficientes categorías para generar el nivel.")
        return None

    categorias_elegidas = []
    while len(categorias_elegidas) < cant_categorias:
        numero = random.randint(0, len(categorias) - 1)
        categoria = categorias[numero]
        if categoria not in categorias_elegidas:
            categorias_elegidas += [categoria]

    nivel = []
    for categoria in categorias_elegidas:
        palabras = diccionario_palabras[categoria]
        cantidad = 0
        while cantidad < palabras_por_categoria and cantidad < len(palabras):
            numero = random.randint(0, len(palabras) - 1)
            palabra = palabras[numero]
            if palabra not in nivel:
                nivel += [palabra]
            cantidad += 1

    i = 0
    while i < len(nivel):
        j = random.randint(0, len(nivel) - 1)
        palabra_temporal = nivel[i]
        nivel[i] = nivel[j]
        nivel[j] = palabra_temporal
        i += 1

    return nivel
