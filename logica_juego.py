import random
import time
from mis_funciones import agregar_elemento, convertir_a_minusculas, desordenar_letras, seleccionar_palabra_y_lista
import comodines
from usuarios import cargar_usuarios, guardar_usuarios, inicializar_datos_usuario
from palabras import PALABRAS
from funciones_auxiliares import mostrar_letras, mostrar_encabezado_de_juego, mostrar_encabezado_de_nivel
from validaciones import validar_palabra
from manejo_puntaje import calcular_puntos_por_palabra, sumar_puntos_por_acierto, sumar_error

# =========================
# FIN DE NIVEL
# =========================
def finalizar_nivel(estado_juego, palabras_usadas, lista_palabras):
    if len(palabras_usadas) == len(lista_palabras):
        print(f"🎉 Nivel {estado_juego['nivel']} completado!")
        estado_juego["nivel"] += 1
    else:
        estado_juego["reinicios"] -= 1
        estado_juego["vidas"] = 3
        print(f"💥 Nivel no completado. Reinicios restantes: {estado_juego['reinicios']}")

# =========================
# FIN DEL JUEGO
# =========================
def finalizar_juego(estado_juego, usuario):
    if estado_juego["nivel"] > 5:
        usuario["victorias"] += 1
        print(f"\n🏆 ¡Felicitaciones, ganaste la partida!")
    else:
        usuario["derrotas"] += 1
        print(f"\n💀 Perdiste, volvé a intentarlo más tarde.")
    print(f"🏅 Puntaje final: {estado_juego['puntaje']}")

# =========================
# GUARDADO DE DATOS
# =========================
def guardar_datos_usuario(usuario, clave_usuario, ruta):
    if not (clave_usuario == None):
        usuarios = cargar_usuarios(ruta)
        usuarios[clave_usuario] = usuario
        guardar_usuarios(usuarios, ruta)

# =========================
# LÓGICA PRINCIPAL DEL JUEGO
# =========================
def logica_principal(usuario, ruta, vidas=3, clave_usuario=None):
    """
    Contiene toda la lógica del juego:
    - Manejo de rondas
    - Control de errores y vidas
    - Cálculo de puntaje
    - Avance de niveles
    """

    if usuario == None or clave_usuario == None:
        print("❌ No se puede iniciar el juego sin iniciar sesión.")
        return None

    # =========================
    # INICIO DEL JUEGO
    # =========================
    mostrar_encabezado_de_juego()
    inicializar_datos_usuario(usuario)

    estado_juego = {
        "puntaje": 0,
        "nivel": 1,
        "vidas": vidas,
        "reinicios": 3,
        "comodines_jugador": comodines.crear_comodines_iniciales(True)
    }

    # =========================
    # BUCLE DE NIVELES
    # =========================
    while estado_juego["nivel"] <= 5 and estado_juego["reinicios"] > 0:
        print(f"\n=== NIVEL {estado_juego['nivel']} ===")

        palabra_base, lista_palabras = seleccionar_palabra_y_lista(PALABRAS)
        mostrar_letras(list(palabra_base))  # Muestra la palabra ordenada
        palabras_usadas = []
        racha = 0
        errores_ronda = 0

        # =========================
        # BUCLE DE RONDAS (PALABRAS)
        # =========================
        while estado_juego["vidas"] > 0 and len(palabras_usadas) < len(lista_palabras):
            estado_juego["vidas"] = comodines.manejar_comodines(estado_juego["comodines_jugador"], palabra_base, lista_palabras, estado_juego["vidas"])

            intento = input("📝 Ingresá una palabra: ")
            usuario["partidas_jugadas"] += 1
            tiempo_respuesta = time.time()

            if validar_palabra(intento, lista_palabras, palabras_usadas):
                palabras_usadas = agregar_elemento(palabras_usadas, convertir_a_minusculas(intento))
                puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)
                if racha >= 2:
                    puntos += 2
                estado_juego["puntaje"] += puntos
                sumar_puntos_por_acierto(usuario, puntos)
                racha += 1
                
                # Variables para print
                progreso_actual = len(palabras_usadas)
                total_palabras = len(lista_palabras)
                
                print(f"✅ Correcto! Puntaje: {puntos}, Progreso: {progreso_actual}/{total_palabras}, Vidas: {estado_juego['vidas']}")
            else:
                estado_juego["vidas"] -= 1
                errores_ronda += 1
                racha = 0
                sumar_error(usuario)
                print(f"❌ Incorrecto! Vidas restantes: {estado_juego['vidas']}")

        # =========================
        # FIN DEL NIVEL
        # =========================
        finalizar_nivel(estado_juego, palabras_usadas, lista_palabras)

    # =========================
    # FIN DEL JUEGO
    # =========================
    finalizar_juego(estado_juego, usuario)

    # =========================
    # GUARDADO DE DATOS
    # =========================
    guardar_datos_usuario(usuario, clave_usuario, ruta)
