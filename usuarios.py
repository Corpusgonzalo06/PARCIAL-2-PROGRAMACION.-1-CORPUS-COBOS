import json


def cargar_usuarios(ruta: str) -> dict:
    """
    Carga los usuarios desde un archivo JSON.

    PARAMETROS:
    ruta (str) -> Ruta del archivo JSON donde se almacenan los usuarios.

    DEVUELVE:
    dict -> Diccionario con los usuarios. 
    Si el archivo no existe o está vacío, devuelve un diccionario vacío.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = {}
    return usuarios


def guardar_usuarios(usuarios: dict, ruta: str) -> None:
    """
    Guarda los usuarios en un archivo JSON.

    PARAMETROS:
    usuarios (dict) -> Diccionario con los datos de los usuarios a guardar.
    ruta (str) -> Ruta del archivo JSON donde se guardarán los usuarios.

    DEVUELVE:
    None -> No devuelve ningún valor, solo realiza la acción de guardar los datos
            en el archivo indicado.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
