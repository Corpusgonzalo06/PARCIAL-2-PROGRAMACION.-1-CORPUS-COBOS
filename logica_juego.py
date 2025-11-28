import random
import time
from mis_funciones import agregar_elemento, convertir_a_minusculas, desordenar_letras, seleccionar_palabra_y_lista
import comodines
from usuarios import cargar_usuarios, guardar_usuarios, inicializar_datos_usuario
from palabras import PALABRAS
from funciones_auxiliares import mostrar_letras, mostrar_encabezado_de_juego, mostrar_encabezado_de_nivel
from validaciones import validar_palabra
from manejo_puntaje import calcular_puntos_por_palabra, sumar_puntos_por_acierto, sumar_error



def finalizar_nivel(estado_juego: dict, palabras_usadas: list, lista_palabras: list) -> None:
    """
    Finaliza el nivel actual.

    Parámetros:
    - estado_juego (dict): Datos del progreso actual (nivel, vidas, reinicios, puntaje).
    - palabras_usadas (list): Lista de palabras acertadas por el jugador.
    - lista_palabras (list): Lista de palabras válidas del nivel.

    Retorna:
    - None
    """
    if len(palabras_usadas) == len(lista_palabras):
        print(f"🎉 Nivel {estado_juego['nivel']} completado!")
        estado_juego["nivel"] += 1
    else:
        estado_juego["reinicios"] -= 1
        estado_juego["vidas"] = 3
        print(f"💥 Nivel no completado. Reinicios restantes: {estado_juego['reinicios']}")




def finalizar_juego(estado_juego: dict, usuario: dict) -> None:
    """
    Finaliza la partida y actualiza las estadísticas del usuario.

    Parámetros:
    - estado_juego (dict): Progreso final del juego.
    - usuario (dict): Datos del usuario para actualizar victorias/derrotas.

    Retorna:
    - None
    """
    if estado_juego["nivel"] > 5:
        usuario["victorias"] += 1
        print(f"\n🏆 ¡Felicitaciones, ganaste la partida!")
    else:
        usuario["derrotas"] += 1
        print(f"\n💀 Perdiste, volvé a intentarlo más tarde.")

    print(f"🏅 Puntaje final: {estado_juego['puntaje']}")



def guardar_datos_usuario(usuario: dict, clave_usuario: str | None, ruta: str) -> None:
    """
    Guarda los datos del usuario en el archivo JSON.

    Parámetros:
    - usuario (dict): Información del usuario actualizada.
    - clave_usuario (str | None): Identificador del usuario en el JSON.
    - ruta (str): Ruta del archivo JSON.

    Retorna:
    - None
    """
    if not (clave_usuario == None):
        usuarios = cargar_usuarios(ruta)
        usuarios[clave_usuario] = usuario
        guardar_usuarios(usuarios, ruta)



def logica_principal( usuario: dict | None, ruta: str, vidas: int = 3, clave_usuario = None | str) -> None:
    """
    Lógica principal del juego.

    Parámetros:
    - usuario (dict | None): Datos del usuario que inició sesión.
    - ruta (str): Ruta del archivo JSON donde se guardan los usuarios.
    - vidas (int): Vidas iniciales del jugador (default: 3).
    - clave_usuario (str | None): Clave del usuario dentro del archivo JSON.

    Retorna:
    - None
    """

    if usuario == None or clave_usuario == None:
        print("❌ No se puede iniciar el juego sin iniciar sesión.")
        return None


    # INICIO DEL JUEGO

    mostrar_encabezado_de_juego()
    inicializar_datos_usuario(usuario)

    estado_juego = {
        "puntaje": 0,
        "nivel": 1,
        "vidas": vidas,
        "reinicios": 3,
        "comodines_jugador": comodines.crear_comodines_iniciales(True)
    }


    # BUCLE DE NIVELES

    while estado_juego["nivel"] <= 5 and estado_juego["reinicios"] > 0:
        print(f"\n=== NIVEL {estado_juego['nivel']} ===")

        palabra_base, lista_palabras = seleccionar_palabra_y_lista(PALABRAS)
        mostrar_letras(list(palabra_base))
        palabras_usadas = []
        racha = 0
        errores_ronda = 0


        # BUCLE DE RONDAS

        while estado_juego["vidas"] > 0 and len(palabras_usadas) < len(lista_palabras):

            estado_juego["vidas"] = comodines.manejar_comodines(
                estado_juego["comodines_jugador"],
                palabra_base,
                lista_palabras,
                estado_juego["vidas"]
            )

            intento = input("📝 Ingresá una palabra: ")
            usuario["partidas_jugadas"] += 1
            tiempo_respuesta = time.time()

            if validar_palabra(intento, lista_palabras, palabras_usadas):

                palabras_usadas = agregar_elemento( palabras_usadas, convertir_a_minusculas(intento))

                puntos = calcular_puntos_por_palabra(intento, tiempo_respuesta)

                if racha >= 2:
                    puntos += 2

                estado_juego["puntaje"] += puntos
                sumar_puntos_por_acierto(usuario, puntos)
                racha += 1

                progreso_actual = len(palabras_usadas)
                total_palabras = len(lista_palabras)

                print(f"✅ Correcto! Puntaje: {puntos}, Progreso: {progreso_actual}/{total_palabras}, Vidas: {estado_juego['vidas']}")

            else:
                estado_juego["vidas"] -= 1
                errores_ronda += 1
                racha = 0
                sumar_error(usuario)

                print(f"❌ Incorrecto! Vidas restantes: {estado_juego['vidas']}")


        # FIN DEL NIVEL

        finalizar_nivel(estado_juego, palabras_usadas, lista_palabras)


    # FIN DEL JUEGO

    finalizar_juego(estado_juego, usuario)


    # GUARDADO DE DATOS

    guardar_datos_usuario(usuario, clave_usuario, ruta)
