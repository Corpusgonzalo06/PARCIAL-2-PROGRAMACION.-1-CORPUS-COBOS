from usuarios import guardar_usuarios

def inicializar_estadisticas(usuario_data: dict) -> None:
    """
    Se asegura de que un usuario tenga todas las estadísticas necesarias.
    
    PARAMETROS:
    usuario_data (dict) -> Diccionario que contiene los datos de un usuario.
    
    DEVUELVE:
    None -> Modifica directamente el diccionario usuario_data agregando
            estadísticas faltantes con valor inicial 0.
    """
    claves_necesarias = {
        "partidas_jugadas": 0,
        "palabras_acertadas": 0,
        "palabras_erradas": 0,
        "victorias": 0,
        "derrotas": 0,
        "puntos": 0
    }

    for clave_necesaria in claves_necesarias:
        clave_existe = False
        for clave_usuario in usuario_data:
            if clave_usuario == clave_necesaria:
                clave_existe = True
                break
        if clave_existe == False:
            usuario_data[clave_necesaria] = claves_necesarias[clave_necesaria]


def registrar_usuario(usuarios: dict, ruta: str) -> dict:
    """
    Permite registrar un nuevo usuario. Si el usuario no existe,
    se crea su registro con contraseña y estadísticas iniciales.
    
    PARAMETROS:
    usuarios (dict) -> Diccionario con todos los usuarios existentes.
    ruta (str) -> Ruta del archivo JSON donde se guardarán los usuarios.
    
    DEVUELVE:
    dict -> Diccionario actualizado de usuarios, incluyendo el nuevo usuario si se creó.
    """
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
    """
    Permite a un usuario iniciar sesión verificando su nombre y contraseña.
    
    PARAMETROS:
    usuarios (dict) -> Diccionario con todos los usuarios existentes.
    
    DEVUELVE:
    str -> Nombre del usuario si la sesión fue exitosa.
    None -> Si el usuario no existe o la contraseña es incorrecta.
    """
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
