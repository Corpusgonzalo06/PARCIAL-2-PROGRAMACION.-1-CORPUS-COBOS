def leer_archivo(ruta_archivo: str) -> list:
    """
    Lee un archivo de texto y devuelve todas sus líneas.

    PARAMETROS:
    - ruta_archivo (str): Ruta del archivo a leer.

    RETORNA:
    - list: Lista con todas las líneas del archivo.
            Si el archivo no existe, retorna una lista vacía.
    """
    lineas = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo: {ruta_archivo}")
    return lineas


def separar_por_comas(linea: str) -> dict:
    """
    Separa una línea de texto usando comas como delimitador.

    La función recorre caracter por caracter y arma una lista con las columnas
    encontradas y la cantidad total de columnas procesadas.

    Parámetros:
        linea (str): Línea de texto a separar por comas.

    Retorna:
        dict: Diccionario con dos claves:
            - "valores": Lista de columnas encontradas (str).
            - "total_columnas": Cantidad de columnas procesadas (int).
    """
    lista_columnas = []
    columna_actual = ""
    total_columnas = 0

    for caracter in linea:
        if caracter == "," or caracter == "\n":
            if len(lista_columnas) == total_columnas:
                lista_columnas += [""]
            lista_columnas[total_columnas] = columna_actual
            total_columnas += 1
            columna_actual = ""
        else:
            columna_actual += caracter

    resultado = {
        "valores": lista_columnas,
        "total_columnas": total_columnas
    }

    return resultado


def cargar_fila_en_diccionario(diccionario_categorias: dict, columnas: list, cantidad_columnas: int) -> dict:
    """
    Carga una fila procesada dentro del diccionario de categorías.

    La primera columna representa la categoría, y las restantes son palabras
    asociadas a esa categoría.

    PARAMETROS:
    - diccionario_categorias (dict): Diccionario donde se guardarán los datos.
    - columnas (list): Lista con la categoría y las palabras leídas.
    - cantidad_columnas (int): Cantidad total de columnas extraídas.

    RETORNA:
    - dict: Diccionario actualizado con la categoría y sus palabras.
    """
    if cantidad_columnas < 2:
        retorno = diccionario_categorias  # fila inválida

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

    retorno =  diccionario_categorias
    return diccionario_categorias


def cargar_palabras_por_categoria(ruta_archivo: str = "partidas.csv") -> dict:
    """
    Carga un archivo CSV y construye un diccionario donde cada categoría
    está asociada a una lista de palabras.

    El archivo debe tener el formato:
        categoria, palabra1, palabra2, ...

    PARAMETROS:
    - ruta_archivo : Ruta del archivo CSV. Por defecto "partidas.csv".

    RETORNA:
    - dict: Diccionario con la estructura.
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
            resultado = separar_por_comas(linea_actual)
            columnas = resultado["columnas"]
            cantidad_columnas = resultado["cantidad"]

            diccionario_categorias = cargar_fila_en_diccionario(
                diccionario_categorias,
                columnas,
                cantidad_columnas
            )

        indice_linea += 1

    return diccionario_categorias
