

def leer_archivo(ruta_archivo: str) -> list:
    """
    Lee un archivo y devuelve todas sus líneas.
    """
    lineas = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo: {ruta_archivo}")
    return lineas


def separar_por_comas(linea: str) -> tuple:
    """
    Recibe una línea y la separa en columnas sin usar split().
    Devuelve una lista de columnas y la cantidad de columnas.
    """
    columnas = []             # lista de palabras/columnas
    texto_actual = ""         # acumula caracteres hasta la coma
    cantidad_columnas = 0     # contador de columnas agregadas

    for caracter in linea:
        if caracter == "," or caracter == "\n":
            if len(columnas) == cantidad_columnas:
                columnas += [""]
            columnas[cantidad_columnas] = texto_actual
            cantidad_columnas += 1
            texto_actual = ""
        else:
            texto_actual += caracter

    return columnas, cantidad_columnas


def cargar_fila_en_diccionario(diccionario_categorias: dict, columnas: list, cantidad_columnas: int) -> dict:
    """
    Agrega las palabras de una fila al diccionario.
    columnas[0] = categoría
    columnas[1..n] = palabras
    """
    if cantidad_columnas < 2:
        return diccionario_categorias  # fila inválida

    categoria = columnas[0]

    # Verificar si la categoría ya existe manualmente
    existe_categoria = False
    for clave in diccionario_categorias:
        if clave == categoria:
            existe_categoria = True
            break

    if not existe_categoria:
        diccionario_categorias[categoria] = []

    indice = 1
    while indice < cantidad_columnas:
        palabra = columnas[indice]
        if palabra != "":
            diccionario_categorias[categoria] += [palabra]
        indice += 1

    return diccionario_categorias



def cargar_palabras_por_categoria(ruta_archivo: str = "partidas.csv") -> dict:
    """
    Carga palabras desde un archivo CSV (categoría, palabra1, palabra2, ...).
    Retorna un diccionario: {categoria: [palabra1, palabra2, ...]}
    """
    diccionario_categorias = {}
    lineas = leer_archivo(ruta_archivo)

    es_primera_linea = True
    indice_linea = 0

    while indice_linea < len(lineas):
        linea_actual = lineas[indice_linea]

        if es_primera_linea:
            es_primera_linea = False
        else:
            columnas, cantidad_columnas = separar_por_comas(linea_actual)
            diccionario_categorias = cargar_fila_en_diccionario(diccionario_categorias, columnas, cantidad_columnas)

        indice_linea += 1

    return diccionario_categorias
