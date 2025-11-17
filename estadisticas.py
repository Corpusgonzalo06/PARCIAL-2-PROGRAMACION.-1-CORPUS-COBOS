# estadisticas.py
import time
from usuarios import guardar_usuarios

# ============================================================
# MEDIR TIEMPO TOTAL DEL JUEGO
# ============================================================



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
        "puntos": 0,
        "tiempo_total": 0    
    }

    for clave_necesaria in claves_necesarias:
        clave_existe = False
        for clave_usuario in usuario_data:
            if clave_usuario == clave_necesaria:
                clave_existe = True
                break
        if clave_existe == False:
            usuario_data[clave_necesaria] = claves_necesarias[clave_necesaria]








def calcular_tiempo_total(inicio, fin):
    tiempo_total = fin - inicio
    return tiempo_total


# ============================================================
# GUARDAR ESTADISTICAS AL FINAL DEL JUEGO
# ============================================================

def guardar_estadisticas_finales(nombre_usuario, usuarios, ruta,
                                 tiempo_total, errores_totales):

    for usuario in usuarios:
        if usuario == nombre_usuario:

            usuarios[usuario]["tiempo_total_juego"] = tiempo_total
            usuarios[usuario]["errores_totales_juego"] = errores_totales

            guardar_usuarios(usuarios, ruta)
            break


# ============================================================
# MOSTRAR RESUMEN FINAL SIMPLE EN LA CONSOLA
# ============================================================

def mostrar_resumen_final(nombre_usuario, usuarios):

    for usuario in usuarios:
        if usuario == nombre_usuario:

            datos = usuarios[usuario]

            print("\n===== RESUMEN DEL JUEGO =====\n")

            tiempo = datos["tiempo_total_juego"]
            errores = datos["errores_totales_juego"]

            print("Tiempo total de juego:", tiempo, "segundos")
            print("Errores totales:", errores)
            print()
