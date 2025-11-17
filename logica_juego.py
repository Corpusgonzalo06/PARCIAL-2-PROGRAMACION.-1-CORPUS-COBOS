#logica_juego
import random
from usuarios import guardar_usuarios
from extras import *
from mis_funciones import *
from validaciones import *
from funciones_auxiliares import *
from partidas import *
import comodines

import time
# ================= FUNCIONES DE PALABRAS =================

def obtener_palabras_del_nivel(nivel: int) -> list:
    palabras_por_categoria = cargar_palabras_por_categoria("palabras.csv")
    palabras_nivel = generar_nivel_aleatorio(palabras_por_categoria, 4, 4)
    return palabras_nivel


def obtener_palabra_aleatoria(palabras: list) -> str:
    lista_copia = copiar_lista(palabras)
    indice = random.randint(0, len(lista_copia) - 1)
    palabra_elegida = lista_copia[indice]
    return palabra_elegida


# ================= FUNCIONES DE PALABRA =================

def pedir_y_validar_palabra(palabra_correcta: str) -> bool:
    intento = input("📝 Ingresá una palabra: ")

    intento = convertir_a_minusculas(intento)
    palabra_correcta_minus = convertir_a_minusculas(palabra_correcta)

    palabra_validada = validar_palabra_ingresada(intento, palabra_correcta_minus)
    return palabra_validada


# ================= FUNCIONES DE PARTIDA =================

def jugar_partida(palabra_correcta: str, vidas: int, puntaje: int, comodines_jugador: dict) -> tuple:
    letras = preparar_palabra_desordenada(palabra_correcta)
    mostrar_letras(letras)

    acierto = False
    vidas_actuales = vidas
    puntaje_actual = puntaje

    while vidas_actuales > 0 and not acierto:
        vidas_actuales = comodines.manejar_comodines(comodines_jugador, palabra_correcta, vidas_actuales)
        palabra_valida = pedir_y_validar_palabra(palabra_correcta)

        if palabra_valida:
            puntos = len(palabra_correcta)
            puntaje_actual += puntos
            print(f"✅ ¡Correcto! Ganaste {puntos} puntos.")
            acierto = True
        else:
            vidas_actuales -= 1
            print(f"❌ ¡Incorrecto! Te quedan {vidas_actuales} vidas.")

    return (puntaje_actual, vidas_actuales)


# ================= FUNCIONES DE NIVEL =================

def jugar_nivel(nivel: int, vidas_totales: int, puntaje: int, reinicios: int, comodines_jugador: dict) -> tuple:
    mostrar_encabezado_de_nivel(nivel)
    palabras = obtener_palabras_del_nivel(nivel)

    nivel_superado = False
    vidas_actuales = vidas_totales
    puntaje_actual = puntaje
    partidas = 0

    resultado = (puntaje_actual, reinicios, nivel_superado)  # variable de retorno única

    if len(palabras) == 0:
        print(f"⚠️ No hay palabras cargadas para el nivel {nivel}.")
        return resultado

    while partidas < 10 and vidas_actuales > 0:
        print(f"\n🏆 Palabra {partidas + 1} de 10")
        palabra = obtener_palabra_aleatoria(palabras)

        puntaje_actual, vidas_actuales = jugar_partida(
            palabra, vidas_actuales, puntaje_actual, comodines_jugador
        )

        if vidas_actuales > 0:
            partidas += 1

    # Evaluar resultado final
    if vidas_actuales <= 0:
        print("\n💀 Perdiste todas las vidas.")
        reinicios -= 1

        if reinicios < 0:
            print(f"🚫 Fin del juego. Puntaje final: {puntaje_actual}")
            resultado = (puntaje_actual, reinicios, False)
        else:
            print(f"🔁 Reiniciando nivel... Reinicios restantes: {reinicios}")
            resultado = (puntaje_actual, reinicios, False)
    else:
        # GANÓ EL NIVEL
        print(f"\n🎉 ¡Nivel {nivel} superado! Puntaje: {puntaje_actual}")
        resultado = (puntaje_actual, reinicios, True)

    return resultado


# ================= FUNCIONES DE USUARIO =================

def inicializar_estadisticas_usuario(nombre_usuario: str, usuarios: dict, ruta: str) -> None:
    encontrado = False
    datos_usuario = None

    for nombre in usuarios:
        if nombre == nombre_usuario:
            encontrado = True
            datos_usuario = usuarios[nombre]
            break

    if encontrado:
        estadisticas_necesarias = [
            "partidas_jugadas", "palabras_acertadas", "palabras_erradas",
            "victorias", "derrotas", "puntos"
        ]

        for estadistica in estadisticas_necesarias:
            existe = False
            for clave in datos_usuario:
                if clave == estadistica:
                    existe = True
                    break

            if not existe:
                datos_usuario[estadistica] = 0

        guardar_usuarios(usuarios, ruta)


def finalizar_juego(nombre_usuario: str, usuarios: dict, ruta: str, nivel: int, puntaje: int) -> None:
    for usuario in usuarios:
        if usuario == nombre_usuario:
            estadisticas = usuarios[usuario]

            if nivel > 5:
                estadisticas["victorias"] += 1
                print(f"\n🏆 ¡Felicitaciones {nombre_usuario}, ganaste la partida!")
            else:
                estadisticas["derrotas"] += 1
                print(f"\n💀 {nombre_usuario}, perdiste esta vez.")

            estadisticas["puntos"] += puntaje
            guardar_usuarios(usuarios, ruta)
            break

    print(f"\n🏁 Juego terminado. Puntaje final: {puntaje}")


# ================= FUNCIONES DE ESTADO =================

def inicializar_estado_juego(vidas_iniciales: int = 3) -> tuple:
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


def ejecutar_juego(nombre_usuario: str, usuarios: dict, ruta: str, vidas: int,
                   reinicios: int, nivel: int, puntaje: int, comodines_jugador: dict) -> tuple:

    nivel_actual = nivel
    puntaje_actual = puntaje
    reinicios_actual = reinicios

    while nivel_actual <= 5 and reinicios_actual >= 0:
        puntaje_actual, reinicios_actual, nivel_superado = jugar_nivel(
            nivel_actual, vidas, puntaje_actual, reinicios_actual, comodines_jugador
        )

        if reinicios_actual < 0:
            break

        if nivel_superado:
            nivel_actual += 1

    return nivel_actual, puntaje_actual


# ================= FUNCIÓN PRINCIPAL =================


def iniciar_juego(nombre_usuario: str, usuarios: dict, ruta: str, vidas: int = 3) -> None:

    # =========================
    # INICIO DEL TIEMPO
    # =========================
    inicio = time.time()

    mostrar_encabezado_de_juego()
    inicializar_estadisticas_usuario(nombre_usuario, usuarios, ruta)

    reinicios, nivel, puntaje, continuar, vidas, comodines_jugador = inicializar_estado_juego(vidas)

    nivel, puntaje = ejecutar_juego(
        nombre_usuario, usuarios, ruta, vidas,
        reinicios, nivel, puntaje, comodines_jugador
    )

    # =========================
    # FIN DEL TIEMPO
    # =========================
    fin = time.time()
    tiempo_total = fin - inicio

    print(f"\n🕒 Tiempo total jugado: {tiempo_total:.2f} segundos")

    # =========================
    # GUARDAR TIEMPO TOTAL
    # =========================
    clave_existente = False

    for clave in usuarios[nombre_usuario]:
        if clave == "tiempo_total":
            clave_existente = True
            break

    # Si no existía, inicializamos
    if not clave_existente:
        usuarios[nombre_usuario]["tiempo_total"] = 0

    usuarios[nombre_usuario]["tiempo_total"] += tiempo_total
    guardar_usuarios(usuarios, ruta)

    # =========================
    # FINALIZAR JUEGO
    # =========================
    finalizar_juego(nombre_usuario, usuarios, ruta, nivel, puntaje)
