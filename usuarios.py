import json

# ===========================
# FUNCIONES DE USUARIOS
# ===========================

def cargar_usuarios(ruta: str) -> dict:
    """
    Carga los usuarios desde un archivo JSON.

    Parámetros:
        ruta (str): Ruta del archivo JSON que contiene los usuarios.

    Retorna:
        dict: Diccionario con los usuarios cargados. 
              Devuelve un diccionario vacío si el archivo no existe o está corrupto.
    """
    usuarios = {}

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

    except FileNotFoundError:
        print("⚠️ Archivo de usuarios no encontrado. Se creará uno nuevo al guardar.")
    except json.JSONDecodeError:
        print("⚠️ Archivo de usuarios vacío o corrupto. Se creará uno nuevo al guardar.")
    except Exception as error:
        print(f"⚠️ Error inesperado al cargar usuarios: {error}")

    return usuarios


def guardar_usuarios(usuario_actual: dict, ruta: str) -> None:
    """
    Guarda o actualiza un usuario sin borrar los demás.

    Parámetros:
        usuario_actual (dict): Diccionario con un solo usuario. Ejemplo: {"gonza": {...}}
        ruta (str): Ruta del archivo JSON donde se guardan los usuarios.

    Retorna:
        None
    """
    try:
        # 1️⃣ Cargar todos los usuarios existentes
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                todos_usuarios = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            todos_usuarios = {}

        # 2️⃣ Actualizar solo el usuario que viene
        todos_usuarios.update(usuario_actual)

        # 3️⃣ Guardar todo de nuevo
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(todos_usuarios, archivo, indent=4, ensure_ascii=False)

    except Exception as error:
        print(f"⚠️ No se pudo guardar el archivo: {error}")


def inicializar_datos_usuario(usuario: dict) -> dict:
    """
    Inicializa las estadísticas y datos de un usuario.

    Parámetros:
        usuario (dict): Diccionario del usuario donde se agregarán los datos.

    Retorna:
        dict: Usuario actualizado con los datos inicializados.
    """
    datos = {
        "palabras_acertadas": 0,
        "palabras_erradas": 0,
        "puntos": 0,
        "errores_totales_juego": 0,
        "tiempo_total_juego": 0,
        "partidas_jugadas": 0,
        "victorias": 0,
        "derrotas": 0
    }

    for clave in datos:
        usuario[clave] = datos[clave]

    return usuario
