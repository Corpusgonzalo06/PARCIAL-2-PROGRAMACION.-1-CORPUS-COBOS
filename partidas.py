import csv
import random

# ===========================
# FUNCIONES AUXILIARES
# ===========================

def contar(lista: list) -> int:
    """
    Cuenta la cantidad de elementos de una lista sin usar len().

    Parámetros:
        lista (list): Lista cuyos elementos se quieren contar.

    Retorna:
        int: Número de elementos de la lista.
    """
    longitud = 0
    for i in lista:
        longitud += 1
    return longitud


def elegir_aleatorios(lista: list, lista_len: int, cantidad: int) -> list:
    """
    Elige elementos aleatorios de una lista sin repetir.

    Parámetros:
        lista (list): Lista de donde se extraen los elementos.
        lista_len (int): Longitud de la lista.
        cantidad (int): Número de elementos a seleccionar.

    Retorna:
        list: Lista con los elementos elegidos aleatoriamente.
    """
    elegidos = []
    elegidos_len = 0
    while elegidos_len < cantidad:
        indice = random.randint(0, lista_len-1)
        elemento = lista[indice]

        existe = False
        for i in range(elegidos_len):
            if elegidos[i] == elemento:
                existe = True
                break

        if not existe:
            if len(elegidos) == elegidos_len:
                elegidos += [""]
            elegidos[elegidos_len] = elemento
            elegidos_len += 1
    return elegidos


def mezclar_lista(lista: list) -> list:
    """
    Mezcla los elementos de una lista usando índices aleatorios.

    Parámetros:
        lista (list): Lista a mezclar.

    Retorna:
        list: Lista con los elementos mezclados.
    """
    lista_len = contar(lista)
    for i in range(lista_len):
        j = random.randint(0, lista_len-1)
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
    return lista


def agregar_palabras_al_nivel(nivel: list, palabras_disponibles: list, palabras_por_categoria: int) -> None:
    """
    Agrega palabras de una categoría a un nivel sin retornar índices ni usar append.

    Parámetros:
        nivel (list): Lista donde se agregan las palabras del nivel.
        palabras_disponibles (list): Lista de palabras disponibles para la categoría.
        palabras_por_categoria (int): Cantidad de palabras a agregar de la categoría.

    Retorna:
        None
    """
    palabras_len = contar(palabras_disponibles)
    cantidad = palabras_por_categoria
    if cantidad > palabras_len:
        cantidad = palabras_len

    palabras_elegidas = elegir_aleatorios(palabras_disponibles, palabras_len, cantidad)

    for i in range(cantidad):
        nivel_len = contar(nivel)
        if len(nivel) == nivel_len:
            nivel += [""]
        nivel[nivel_len] = palabras_elegidas[i]


# ===========================
# FUNCIONES PRINCIPALES
# ===========================

def cargar_palabras_por_categoria(ruta_archivo: str = "partidas.csv") -> dict:
    """
    Carga palabras desde un archivo CSV organizadas por categoría.

    Parámetros:
        ruta_archivo (str): Ruta del archivo CSV con las palabras.

    Retorna:
        dict: Diccionario con categorías como claves y listas de palabras como valores.
    """
    categorias = {}
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            primera_fila = True
            for fila in lector:
                if primera_fila:
                    primera_fila = False
                    continue
                if contar(fila) < 2:
                    continue
                categoria = fila[0]
                palabra = fila[1]

                if categoria not in categorias:
                    categorias[categoria] = []
                    categorias[categoria + "_indice"] = 0

                indice = categorias[categoria + "_indice"]
                if len(categorias[categoria]) == indice:
                    categorias[categoria] += [""]
                categorias[categoria][indice] = palabra
                categorias[categoria + "_indice"] = indice + 1

        # Limpiar índices auxiliares
        claves_a_borrar = []
        for clave in categorias:
            if clave.endswith("_indice"):
                claves_a_borrar += [clave]
        for clave in claves_a_borrar:
            del categorias[clave]

    except FileNotFoundError:
        print("⚠️ No se encontró el archivo:", ruta_archivo)

    return categorias


def generar_nivel_aleatorio(diccionario_palabras: dict, cant_categorias: int = 4, palabras_por_categoria: int = 4) -> list:
    """
    Genera un nivel con palabras aleatorias de diferentes categorías.

    Parámetros:
        diccionario_palabras (dict): Diccionario con categorías y palabras.
        cant_categorias (int): Cantidad de categorías a incluir en el nivel.
        palabras_por_categoria (int): Cantidad de palabras por categoría.

    Retorna:
        list: Lista con las palabras seleccionadas y mezcladas para el nivel.
    """
    nivel = []

    categorias = []
    categorias_len = 0
    for clave in diccionario_palabras:
        if len(categorias) == categorias_len:
            categorias += [""]
        categorias[categorias_len] = clave
        categorias_len += 1

    categorias_elegidas = elegir_aleatorios(categorias, categorias_len, cant_categorias)

    for i in range(cant_categorias):
        categoria = categorias_elegidas[i]
        palabras_disponibles = diccionario_palabras[categoria]
        agregar_palabras_al_nivel(nivel, palabras_disponibles, palabras_por_categoria)

    nivel = mezclar_lista(nivel)
    return nivel
