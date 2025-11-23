##########################
# LOGICA_JUEGO.PY
##########################

import random
import time
from mis_funciones import agregar_elemento, convertir_a_minusculas
import comodines
from usuarios import cargar_usuarios, guardar_usuarios
from palabras import PALABRAS
from funciones_auxiliares import mostrar_letras, mostrar_encabezado_de_juego, mostrar_encabezado_de_nivel
from validaciones import validar_palabra

##########################
# FUNCIONES DE USUARIO
##########################

def inicializar_datos_usuario(usuario):
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


def crear_comodines_iniciales(valor=True):
    return {
        "revelar_palabra": valor,
        "eliminar_restricciones": valor,
        "pista_extra": valor
    }

##########################
# FUNCIONES DE PALABRAS
##########################

def seleccionar_palabra_y_lista():
    palabra = random.choice(list(PALABRAS.keys()))
    lista = PALABRAS[palabra]
    return palabra, lista


def desordenar_letras(palabra, dificultad=2):
    lista_letras = []
    for letra in palabra:
        lista_letras = agregar_elemento(lista_letras, letra)

    for _ in range(dificultad):
        for i in range(len(lista_letras)):
            r = random.randint(0, len(lista_letras) - 1)
            lista_letras[i], lista_letras[r] = lista_letras[r], lista_letras[i]

    return "".join(lista_letras)

##########################
# FUNCIONES DE PUNTAJE
##########################

def calcular_puntos_por_palabra(palabra, tiempo_respuesta):
    puntos = len(palabra)
    if len(palabra) > 4:
        puntos += 2
    if tiempo_respuesta < 5:
        puntos += 3
    elif tiempo_respuesta < 10:
        puntos += 1
    return puntos

def sumar_puntos_por_acierto(usuario, puntos):
    usuario["palabras_acertadas"] += 1
    usuario["puntos"] += puntos

def sumar_error(usuario):
    usuario["palabras_erradas"] += 1

##########################
# FUNCIONES DE PARTIDA
##########################

def jugar_una_partida(palabra_base, lista_palabras, vidas, puntaje, comodines_jugador, usuario, ruta, clave_usuario):
    palabras_usadas = []
    mostrar_letras(desordenar_letras(palabra_base))

    puntaje_actual = puntaje
    vidas_actuales = vidas
    errores = 0
    racha = 0
    inicio = time.time()

    while vidas_actuales > 0:
        vidas_actuales = comodines.manejar_comodines(comodines_jugador, palabra_base, lista_palabras, vidas_actuales)

        intento = input("📝 Ingresá una palabra: ")
        usuario["partidas_jugadas"] += 1
        tiempo_respuesta = time.time() - inicio

        if validar_palabra(intento, lista_palabras, palabras_usadas):
            palabras_usadas = agregar_elemento(palabras_usadas, convertir_a_minusculas(intento))
            puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)
            if racha >= 2:
                puntos += 2
            puntaje_actual += puntos
            sumar_puntos_por_acierto(usuario, puntos)
            racha += 1
            print(f"✅ Correcto! Ganaste {puntos} puntos. Palabras encontradas: {len(palabras_usadas)}/{len(lista_palabras)}")
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

    # GUARDO solo si clave_usuario es válida
    if clave_usuario is not None:
        usuarios = cargar_usuarios(ruta)
        usuarios[clave_usuario] = usuario
        guardar_usuarios(usuarios, ruta)

    return puntaje_actual, vidas_actuales

##########################
# FUNCIONES DE NIVEL
##########################

def jugar_un_nivel(nivel, vidas, puntaje, reinicios, comodines_jugador, usuario, ruta, clave_usuario):
    mostrar_encabezado_de_nivel(nivel)
    palabra_base, lista_palabras = seleccionar_palabra_y_lista()
    puntaje_actual = puntaje
    vidas_actuales = vidas
    nivel_superado = False

    palabras_restantes = 10
    while palabras_restantes > 0 and vidas_actuales > 0:
        print(f"\n🏆 Palabra {10 - palabras_restantes + 1} de 10")
        puntaje_actual, vidas_actuales = jugar_una_partida(
            palabra_base, lista_palabras, vidas_actuales, puntaje_actual,
            comodines_jugador, usuario, ruta, clave_usuario
        )
        palabras_restantes -= 1

    if vidas_actuales > 0:
        print(f"\n🎉 Nivel {nivel} superado! Puntaje acumulado: {puntaje_actual}")
        nivel_superado = True
    else:
        print("\n💀 Ya no te quedan vidas.")
        reinicios -= 1

    return puntaje_actual, reinicios, nivel_superado

##########################
# FUNCIÓN PRINCIPAL
##########################

def ejecutar_juego_completo(usuario, ruta, vidas, reinicios, nivel, puntaje, comodines_jugador, clave_usuario):
    nivel_actual = nivel
    puntaje_actual = puntaje
    reinicios_actual = reinicios

    while nivel_actual <= 5 and reinicios_actual >= 0:
        puntaje_actual, reinicios_actual, superado = jugar_un_nivel(
            nivel_actual, vidas, puntaje_actual, reinicios_actual,
            comodines_jugador, usuario, ruta, clave_usuario
        )

        if superado:
            nivel_actual += 1
        else:
            break

    return nivel_actual, puntaje_actual

def iniciar_juego(usuario, ruta, vidas=3, clave_usuario=None):
    if usuario is None or clave_usuario is None:
        print("❌ No se puede iniciar el juego sin iniciar sesión correctamente.")
        return

    inicio = time.time()
    mostrar_encabezado_de_juego()

    inicializar_datos_usuario(usuario)
    reinicios, nivel, puntaje = 2, 1, 0
    comodines_jugador = crear_comodines_iniciales(True)

    nivel_final, puntaje_final = ejecutar_juego_completo(
        usuario, ruta, vidas, reinicios, nivel, puntaje, comodines_jugador, clave_usuario
    )

    usuario["tiempo_total_juego"] += time.time() - inicio

    # GUARDO solo si clave_usuario es válida
    if clave_usuario is not None:
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
