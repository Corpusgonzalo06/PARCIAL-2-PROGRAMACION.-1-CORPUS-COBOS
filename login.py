from usuarios import guardar_usuarios
from estadisticas import inicializar_estadisticas

def registrar_usuario(usuarios: dict, ruta: str) -> dict:
    nombre = input("Ingrese su nombre de usuario: ").strip()

    if nombre in usuarios:
        print("⚠️ El usuario ya existe.")
        return usuarios

    contraseña = input("Ingrese su contraseña: ").strip()

    usuarios[nombre] = {
        "contraseña": contraseña
    }

    # Inicializo estadísticas de manera segura
    inicializar_estadisticas(usuarios[nombre])
    guardar_usuarios(usuarios, ruta)

    print(f"✅ Usuario {nombre} registrado correctamente.")
    return usuarios


def iniciar_sesion(usuarios: dict) -> tuple:
    nombre = input("Ingrese su nombre de usuario: ").strip()

    if not nombre or nombre not in usuarios:
        print("❌ Usuario no encontrado.")
        return None, None

    contraseña = input("Ingrese su contraseña: ").strip()

    if usuarios[nombre]["contraseña"] != contraseña:
        print("❌ Contraseña incorrecta.")
        return None, None

    # Inicializo estadísticas solo si no existen para no sobreescribir datos
    if "puntos" not in usuarios[nombre]:
        inicializar_estadisticas(usuarios[nombre])

    usuario = usuarios[nombre]
    print("✅ Inicio de sesión exitoso.")
    return usuario, nombre
