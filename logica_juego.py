import random
from usuarios import guardar_usuarios
from extras import *
from mis_funciones import *
from validaciones import *
from funciones_auxiliares import *
from partidas import *
import comodines


# ================= FUNCIONES DE PALABRAS =================

def obtener_palabras_del_nivel(nivel: int) -> list:
    """
    Devuelve una lista de palabras aleatorias para un nivel determinado.
    
    PARAMETROS:
    nivel (int) -> Número de nivel actual del juego.
    
    DEVUELVE:
    list -> Lista de palabras seleccionadas para el nivel.
    """
    palabras_por_categoria = cargar_palabras_por_categoria("palabras.csv")
    palabras_nivel = generar_nivel_aleatorio(palabras_por_categoria, 4, 4)
    return palabras_nivel


def obtener_palabra_aleatoria(palabras: list) -> str:
    """
    Devuelve una palabra aleatoria de una lista dada.
    
    PARAMETROS:
    palabras (list) -> Lista de palabras disponibles.
    
    DEVUELVE:
    str -> Una palabra elegida al azar.
    """
    lista_copia = copiar_lista(palabras)
    indice = random.randint(0, len(lista_copia) - 1)
    return lista_copia[indice]


# ================= FUNCIONES DE PALABRA =================

def pedir_y_validar_palabra(palabra_correcta: str) -> bool:
    """
    Pide al jugador una palabra y la valida contra la palabra correcta.
    
    PARAMETROS:
    palabra_correcta (str) -> Palabra que se espera que ingrese el jugador.
    
    DEVUELVE:
    bool -> True si la palabra ingresada es correcta, False en caso contrario.
    """
    intento = input("📝 Ingresá una palabra: ")
    intento = convertir_a_minusculas(intento)
    palabra_correcta_minus = convertir_a_minusculas(palabra_correcta)
    return validar_palabra_ingresada(intento, palabra_correcta_minus)


# ================= FUNCIONES DE PARTIDA =================

def jugar_partida(palabra_correcta: str, vidas: int, puntaje: int, comodines_jugador: dict) -> tuple:
    """
    Maneja una partida completa de una palabra, incluyendo comodines y vidas.
    
    PARAMETROS:
    palabra_correcta (str) -> Palabra a adivinar.
    vidas (int) -> Cantidad de vidas actuales del jugador.
    puntaje (int) -> Puntaje actual del jugador.
    comodines_jugador (dict) -> Diccionario con los comodines disponibles.
    
    DEVUELVE:
    tuple -> (puntaje_actual (int), vidas_actuales (int))
    """
    letras = preparar_palabra_desordenada(palabra_correcta)
    mostrar_letras(letras)

    acierto = False
    puntos = 0
    vidas_actuales = vidas
    puntaje_actual = puntaje

    while vidas_actuales > 0 and not acierto:
        vidas_actuales = comodines.manejar_comodines(comodines_jugador, palabra_correcta, vidas_actuales)
        palabra_valida = pedir_y_validar_palabra(palabra_correcta)

        if palabra_valida:
            puntos = 0
            i = 0
            while i < len(palabra_correcta):
                puntos += 1
                i += 1
            puntaje_actual += puntos
            print("✅ ¡Correcto! Ganaste " + str(puntos) + " puntos.")
            acierto = True
        else:
            vidas_actuales -= 1
            print("❌ ¡Incorrecto! Te quedan " + str(vidas_actuales) + " vidas.")

    return puntaje_actual, vidas_actuales


# ================= FUNCIONES DE NIVEL =================

def jugar_nivel(nivel: int, vidas_totales: int, puntaje: int, reinicios: int, comodines_jugador: dict) -> tuple:
    """
    Maneja todas las partidas de un nivel, controlando vidas, puntaje y reinicios.
    
    PARAMETROS:
    nivel (int) -> Número de nivel actual.
    vidas_totales (int) -> Cantidad de vidas iniciales.
    puntaje (int) -> Puntaje acumulado.
    reinicios (int) -> Cantidad de reinicios disponibles.
    comodines_jugador (dict) -> Diccionario con comodines disponibles.
    
    DEVUELVE:
    tuple -> (puntaje_actual (int), reinicios (int), nivel_superado (bool))
    """
    mostrar_encabezado_de_nivel(nivel)
    palabras = obtener_palabras_del_nivel(nivel)
    nivel_superado = False
    vidas_actuales = vidas_totales
    puntaje_actual = puntaje
    partidas = 0

    if len(palabras) == 0:
        print("⚠️ No hay palabras cargadas para el nivel " + str(nivel) + ".")
        return puntaje_actual, reinicios, nivel_superado

    while partidas < 3 and vidas_actuales > 0:
        print("\n🏆 Partida " + str(partidas + 1) + " de 3")
        palabra = obtener_palabra_aleatoria(palabras)
        puntaje_actual, vidas_actuales = jugar_partida(palabra, vidas_actuales, puntaje_actual, comodines_jugador)
        if vidas_actuales > 0:
            partidas += 1

    if vidas_actuales > 0:
        print("\n🎉 ¡Nivel " + str(nivel) + " superado! Puntaje: " + str(puntaje_actual))
        nivel_superado = True
    else:
        print("\n💀 Perdiste todas las vidas.")
        reinicios -= 1
        if reinicios > 0:
            print("🔁 Reiniciando nivel... Reinicios restantes: " + str(reinicios))
        else:
            print("🚫 Fin del juego. Puntaje final: " + str(puntaje_actual))

    return puntaje_actual, reinicios, nivel_superado


# ================= FUNCIONES DE USUARIO =================

def inicializar_estadisticas_usuario(nombre_usuario: str, usuarios: dict, ruta: str) -> None:
    """
    Asegura que un usuario tenga todas las estadísticas necesarias.
    
    PARAMETROS:
    nombre_usuario (str) -> Nombre del usuario a inicializar.
    usuarios (dict) -> Diccionario con todos los usuarios.
    ruta (str) -> Ruta del archivo JSON para guardar los usuarios.
    
    DEVUELVE:
    None -> Modifica directamente el diccionario usuarios.
    """
    encontrado = False
    for nombre in usuarios:
        if nombre == nombre_usuario:
            encontrado = True
            datos_usuario = usuarios[nombre]
            break

    if encontrado:
        estadisticas_necesarias = ["partidas_jugadas", "palabras_acertadas", "palabras_erradas",
                                   "victorias", "derrotas", "puntos"]

        i = 0
        while i < len(estadisticas_necesarias):
            nombre_estadistica = estadisticas_necesarias[i]

            existe = False
            for campo in datos_usuario:
                if campo == nombre_estadistica:
                    existe = True
                    break

            if not existe:
                datos_usuario[nombre_estadistica] = 0

            i += 1

        guardar_usuarios(usuarios, ruta)


def finalizar_juego(nombre_usuario: str, usuarios: dict, ruta: str, nivel: int, puntaje: int) -> None:
    """
    Actualiza las estadísticas del usuario al finalizar el juego y muestra mensaje final.
    
    PARAMETROS:
    nombre_usuario (str) -> Nombre del jugador.
    usuarios (dict) -> Diccionario con todos los usuarios.
    ruta (str) -> Ruta del archivo JSON para guardar los usuarios.
    nivel (int) -> Nivel alcanzado por el jugador.
    puntaje (int) -> Puntaje final del jugador.
    
    DEVUELVE:
    None -> Modifica directamente el diccionario usuarios y muestra mensajes.
    """
    if nombre_usuario in usuarios:
        stats = usuarios[nombre_usuario]
        if nivel > 5:
            stats["victorias"] += 1
            print("\n🏆 ¡Felicitaciones " + nombre_usuario + ", ganaste la partida!")
        else:
            stats["derrotas"] += 1
            print("\n💀 " + nombre_usuario + ", perdiste esta vez.")
        stats["puntos"] += puntaje
        guardar_usuarios(usuarios, ruta)

    print("\n🏁 Juego terminado. Puntaje final: " + str(puntaje))


# ================= FUNCIONES DE ESTADO =================

def inicializar_estado_juego(vidas_iniciales: int = 3) -> tuple:
    """
    Inicializa todas las variables de estado necesarias al comenzar un juego.
    
    PARAMETROS:
    vidas_iniciales (int) -> Cantidad de vidas iniciales del jugador.
    
    DEVUELVE:
    tuple -> (reinicios (int), nivel (int), puntaje (int), continuar (bool),
              vidas (int), comodines_jugador (dict))
    """
    reinicios = 2
    nivel = 1
    puntaje = 0
    continuar = True
    vidas = vidas_iniciales

    comodines_jugador = {
        "revelar_palabra": True,
        "eliminar_restricciones": True,
        "pista_extra": True
    }

    return reinicios, nivel, puntaje, continuar, vidas, comodines_jugador


def ejecutar_juego(nombre_usuario: str, usuarios: dict, ruta: str, vidas: int, reinicios: int, nivel: int,
                   puntaje: int, comodines_jugador: dict) -> tuple:
    """
    Ejecuta todo el flujo del juego, manejando niveles y puntajes.
    
    PARAMETROS:
    nombre_usuario (str) -> Nombre del jugador.
    usuarios (dict) -> Diccionario con todos los usuarios.
    ruta (str) -> Ruta del archivo JSON.
    vidas (int) -> Vidas iniciales del jugador.
    reinicios (int) -> Cantidad de reinicios disponibles.
    nivel (int) -> Nivel inicial.
    puntaje (int) -> Puntaje acumulado.
    comodines_jugador (dict) -> Diccionario con comodines disponibles.
    
    DEVUELVE:
    tuple -> (nivel_actual (int), puntaje_actual (int))
    """
    continuar = True
    nivel_actual = nivel
    puntaje_actual = puntaje
    reinicios_actual = reinicios

    while nivel_actual <= 5 and reinicios_actual >= 0 and continuar:
        puntaje_actual, reinicios_actual, nivel_superado = jugar_nivel(
            nivel_actual, vidas, puntaje_actual, reinicios_actual, comodines_jugador
        )

        if nivel_superado:
            nivel_actual += 1
        elif reinicios_actual < 0:
            continuar = False

    return nivel_actual, puntaje_actual


# ================= FUNCIÓN PRINCIPAL =================

def iniciar_juego(nombre_usuario: str, usuarios: dict, ruta: str, vidas: int = 3) -> None:
    """
    Función principal que inicia el juego completo para un usuario.
    
    PARAMETROS:
    nombre_usuario (str) -> Nombre del jugador.
    usuarios (dict) -> Diccionario con todos los usuarios.
    ruta (str) -> Ruta del archivo JSON.
    vidas (int) -> Cantidad de vidas iniciales (por defecto 3).
    
    DEVUELVE:
    None -> Ejecuta el juego, actualiza usuarios y muestra mensajes en consola.
    """
    mostrar_encabezado_de_juego()
    inicializar_estadisticas_usuario(nombre_usuario, usuarios, ruta)
    reinicios, nivel, puntaje, continuar, vidas, comodines_jugador = inicializar_estado_juego(vidas)

    nivel, puntaje = ejecutar_juego(nombre_usuario, usuarios, ruta, vidas, reinicios, nivel,
                                    puntaje, comodines_jugador)

    finalizar_juego(nombre_usuario, usuarios, ruta, nivel, puntaje)
