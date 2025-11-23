# partidas.py
import csv
import random

# ===========================
# FUNCIONES AUXILIARES
# ===========================

# Contar elementos de una lista sin usar len()
def contar(lista):
    longitud = 0
    for _ in lista:
        longitud += 1
    return longitud

# Elegir elementos aleatorios de una lista sin repetir
def elegir_aleatorios(lista, lista_len, cantidad):
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

# Mezclar lista usando índices
def mezclar_lista(lista):
    lista_len = contar(lista)
    for i in range(lista_len):
        j = random.randint(0, lista_len-1)
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
    return lista

# Agregar palabras a nivel sin retornar índices ni usar append
def agregar_palabras_al_nivel(nivel, palabras_disponibles, palabras_por_categoria):
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

# Cargar palabras por categoría desde CSV
def cargar_palabras_por_categoria(ruta_archivo="partidas.csv"):
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

# Generar nivel aleatorio
def generar_nivel_aleatorio(diccionario_palabras, cant_categorias=4, palabras_por_categoria=4):
    nivel = []

    # Convertir diccionario a lista de categorías
    categorias = []
    categorias_len = 0
    for clave in diccionario_palabras:
        if len(categorias) == categorias_len:
            categorias += [""]
        categorias[categorias_len] = clave
        categorias_len += 1

    # Elegir categorías aleatorias
    categorias_elegidas = elegir_aleatorios(categorias, categorias_len, cant_categorias)

    # Agregar palabras de cada categoría al nivel
    for i in range(cant_categorias):
        categoria = categorias_elegidas[i]
        palabras_disponibles = diccionario_palabras[categoria]
        agregar_palabras_al_nivel(nivel, palabras_disponibles, palabras_por_categoria)

    # Mezclar palabras del nivel
    nivel = mezclar_lista(nivel)
    return nivel
