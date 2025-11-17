from usuarios import guardar_usuarios
from estadisticas import inicializar_estadisticas

def registrar_usuario(usuarios: dict, ruta: str) -> dict:
    resultado = usuarios
    nombre = input("Ingrese su nombre de usuario: ")
    usuario_existe = False

    for usuario_actual in usuarios:
        if usuario_actual == nombre:
            usuario_existe = True
            break

    if usuario_existe:
        print("⚠️ El usuario ya existe.")
    else:
        contraseña = input("Ingrese su contraseña: ")
        usuarios[nombre] = {"contraseña": contraseña}
        inicializar_estadisticas(usuarios[nombre])
        guardar_usuarios(usuarios, ruta)
        print(f"✅ Usuario {nombre} registrado correctamente.")
        resultado = usuarios

    return resultado


def iniciar_sesion(usuarios: dict) -> str | None:
    nombre_usuario = None
    nombre = input("Ingrese su nombre de usuario: ")
    usuario_encontrado = False

    for usuario_actual in usuarios:
        if usuario_actual == nombre:
            usuario_encontrado = True
            break

    if not usuario_encontrado:
        print("❌ Usuario no encontrado.")
    else:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[nombre]["contraseña"] != contraseña:
            print("❌ Contraseña incorrecta.")
        else:
            inicializar_estadisticas(usuarios[nombre])
            print("✅ Inicio de sesión exitoso.")
            nombre_usuario = nombre
            
    return nombre_usuario
