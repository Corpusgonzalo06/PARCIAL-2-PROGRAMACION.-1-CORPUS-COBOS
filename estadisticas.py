# estadisticas.py
from usuarios import guardar_usuarios


# ============================================================
# INICIALIZAR ESTADISTICAS DE UN USUARIO
# ============================================================

def inicializar_estadisticas(usuario_data: dict) -> None:
    """
    Se asegura de que un usuario tenga todas las estadísticas necesarias.
    """

    claves_necesarias = {
        "partidas_jugadas": 0,
        "palabras_acertadas": 0,
        "palabras_erradas": 0,
        "victorias": 0,
        "derrotas": 0,
        "puntos": 0,
        "tiempo_total": 0,
        "tiempo_total_juego": 0,
        "errores_totales_juego": 0
    }

    for clave in claves_necesarias:
        if clave not in usuario_data:
            usuario_data[clave] = claves_necesarias[clave]

