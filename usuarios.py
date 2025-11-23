# usuarios.py
import json

# ===========================
# FUNCIONES DE USUARIOS
# ===========================

def cargar_usuarios(ruta):
    """
    Carga los usuarios desde un archivo JSON.
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


def guardar_usuarios(usuario_actual, ruta):
    """
    Guarda o actualiza un usuario sin borrar los demás.
    usuario_actual = dict con una sola clave: { "gonza": {...} }
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
