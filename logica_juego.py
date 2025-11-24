##########################
# LOGICA_JUEGO.PY
##########################

import random
import time
from mis_funciones import agregar_elemento, convertir_a_minusculas , desordenar_letras, seleccionar_palabra_y_lista
import comodines
from usuarios import cargar_usuarios, guardar_usuarios , inicializar_datos_usuario
from palabras import PALABRAS
from funciones_auxiliares import mostrar_letras, mostrar_encabezado_de_juego, mostrar_encabezado_de_nivel
from validaciones import validar_palabra
from manejo_puntaje import calcular_puntos_por_palabra, sumar_puntos_por_acierto, sumar_error


def jugar_una_partida(palabra_base, lista_palabras, vidas, puntaje, comodines_jugador, usuario, ruta, clave_usuario):
    """
    Ejecuta una ronda completa donde el jugador intenta adivinar palabras
    hasta quedarse sin vidas. Maneja puntaje, errores, comodines y progreso.

    Parámetros:
    - palabra_base (str): Palabra base de donde salen todas las palabras válidas.
    - lista_palabras (list): Lista con todas las palabras correctas del nivel.
    - vidas (int): Cantidad de vidas disponibles al iniciar la partida.
    - puntaje (int): Puntaje acumulado hasta antes de la partida.
    - comodines_jugador (dict): Comodines disponibles en este nivel.
    - usuario (dict): Diccionario con todas las estadísticas del usuario.
    - ruta (str): Ruta al archivo JSON donde guardar los cambios.
    - clave_usuario (str): Clave de identificación dentro del archivo JSON.

    Retorno:
    - tuple: (puntaje_actualizado (int), vidas_restantes (int))
    """

    palabras_usadas = []

    # Mostramos las letras en orden real (solo la palabra base)
    mostrar_letras(list(palabra_base))

    puntaje_actual = puntaje
    vidas_actuales = vidas
    errores = 0
    racha = 0
    inicio = time.time()

    while vidas_actuales > 0:
        vidas_actuales = comodines.manejar_comodines(
            comodines_jugador,
            palabra_base,
            lista_palabras,
            vidas_actuales
        )

        intento = input("📝 Ingresá una palabra: ")
        usuario["partidas_jugadas"] += 1
        tiempo_respuesta = time.time() - inicio

        if validar_palabra(intento, lista_palabras, palabras_usadas):
            palabras_usadas = agregar_elemento(
                palabras_usadas,
                convertir_a_minusculas(intento)
            )

            puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)
            if racha >= 2:
                puntos += 2

            puntaje_actual += puntos
            sumar_puntos_por_acierto(usuario, puntos)
            racha += 1

            encontradas = len(palabras_usadas)
            totales = len(lista_palabras)

            print(f"✅ Correcto! Ganaste {puntos} puntos.")
            print(f"📘 Progreso: {encontradas}/{totales} palabras.")

        else:
            vidas_actuales -= 1
            errores += 1
            sumar_error(usuario)
            racha = 0
            print(f"❌ Incorrecto! Te quedan {vidas_actuales} vidas.")

        if vidas_actuales == 0:
            break

    usuario["errores_totales_juego"] += errores
    usuario["tiempo_total_juego"] += time.time() - inicio

    if clave_usuario != None:
        usuarios = cargar_usuarios(ruta)
        usuarios[clave_usuario] = usuario
        guardar_usuarios(usuarios, ruta)

    return puntaje_actual, vidas_actuales


##########################
# FUNCIONES DE NIVEL
##########################
def jugar_un_nivel(nivel, vidas, puntaje, reinicios, comodines_jugador, usuario, ruta, clave_usuario):
    """
    Ejecuta toda la lógica de un nivel completo: selecciona palabra base,
    controla vidas, progreso, reinicios y determina si el nivel se supera.

    Parámetros:
    - nivel (int): Número de nivel actual.
    - vidas (int): Vidas iniciales para jugar este nivel.
    - puntaje (int): Puntaje acumulado antes de este nivel.
    - reinicios (int): Cantidad de reinicios permitidos para repetir niveles.
    - comodines_jugador (dict): Comodines iniciales para este nivel.
    - usuario (dict): Datos completos del usuario.
    - ruta (str): Ruta al archivo JSON donde guardar las estadísticas.
    - clave_usuario (str): Identificador del usuario.

    Retorno:
    - tuple: (puntaje_actualizado (int), reinicios_restantes (int), nivel_superado (bool))
    """

    mostrar_encabezado_de_nivel(nivel)
    palabra_base, lista_palabras = seleccionar_palabra_y_lista(PALABRAS)

    comodines_jugador = comodines.crear_comodines_iniciales(True)
    puntaje_actual = puntaje
    vidas_actuales = vidas
    nivel_superado = False

    total_palabras = len(lista_palabras)
    palabras_restantes = total_palabras

    while palabras_restantes > 0 and vidas_actuales > 0:
        palabra_actual_num = total_palabras - palabras_restantes + 1
        print(f"\n🏆En esta palabra hay {total_palabras} palabras disponibles")

        puntaje_actual, vidas_actuales = jugar_una_partida(
            palabra_base,
            lista_palabras,
            vidas_actuales,
            puntaje_actual,
            comodines_jugador,
            usuario,
            ruta,
            clave_usuario
        )

        palabras_restantes -= 1

    if palabras_restantes == 0 and vidas_actuales > 0:
        nivel_superado = True
    else:
        reinicios -= 1
        print(f"\n💥 Nivel no completado. Reinicios restantes: {reinicios}")

    return puntaje_actual, reinicios, nivel_superado


##########################
# FUNCIÓN PRINCIPAL
##########################
def ejecutar_juego_completo(usuario, ruta, vidas, reinicios, nivel, puntaje, comodines_jugador, clave_usuario):
    """
    Controla la ejecución de todos los niveles del juego.
    Maneja reinicios, avance de niveles, acumulación de puntaje y finalización.

    Parámetros:
    - usuario (dict): Diccionario con todos los datos del jugador.
    - ruta (str): Ruta del archivo JSON.
    - vidas (int): Vidas iniciales para cada nivel.
    - reinicios (int): Cantidad de reinicios disponibles.
    - nivel (int): Nivel inicial.
    - puntaje (int): Puntaje inicial acumulado.
    - comodines_jugador (dict): Comodines iniciales.
    - clave_usuario (str): Identificador del usuario.

    Retorno:
    - tuple: (nivel_final (int), puntaje_final (int))
    """

    nivel_actual = nivel
    puntaje_actual = puntaje
    reinicios_actual = reinicios

    while nivel_actual <= 5 and reinicios_actual > 0:
        puntaje_actual, reinicios_actual, superado = jugar_un_nivel(
            nivel_actual,
            vidas,
            puntaje_actual,
            reinicios_actual,
            comodines_jugador,
            usuario,
            ruta,
            clave_usuario
        )

        if superado:
            nivel_actual += 1
        elif reinicios_actual > 0:
            print(f"♻️ Reiniciando el nivel {nivel_actual}...")
            vidas = 3
        else:
            break

    return nivel_actual, puntaje_actual



def iniciar_juego(usuario, ruta, vidas=3, clave_usuario=None):
    """
    Configura y comienza una partida completa.
    Inicializa estadísticas, reinicios, puntaje e inicia la secuencia de niveles.

    Parámetros:
    - usuario (dict): Datos del usuario que inició sesión.
    - ruta (str): Ruta del archivo JSON.
    - vidas (int): Vidas iniciales por nivel (default = 3).
    - clave_usuario (str|None): Identificador del usuario dentro del JSON.

    Retorno:
    - None: Solo ejecuta el flujo del juego.
    """

    if usuario == None or clave_usuario == None:
        print("❌ No se puede iniciar el juego sin iniciar sesión correctamente.")
        return

    inicio = time.time()
    mostrar_encabezado_de_juego()

    inicializar_datos_usuario(usuario)
    reinicios, nivel, puntaje = 3, 1, 0

    comodines_jugador = comodines.crear_comodines_iniciales(True)

    nivel_final, puntaje_final = ejecutar_juego_completo(
        usuario,
        ruta,
        vidas,
        reinicios,
        nivel,
        puntaje,
        comodines_jugador,
        clave_usuario
    )

    usuario["tiempo_total_juego"] += time.time() - inicio

    if clave_usuario != None:
        usuarios = cargar_usuarios(ruta)
        usuarios[clave_usuario] = usuario
        guardar_usuarios(usuarios, ruta)

    if nivel_final > 5:
        usuario["victorias"] += 1
        print(f"\n🏆 ¡Felicitaciones, ganaste la partida!")
    else:
        usuario["derrotas"] += 1
        print(f"\n💀 Perdiste, volvé a intentarlo más tarde.")

    print(f"🏅 Puntaje final acumulado: {puntaje_final}")
