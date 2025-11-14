#main.py
from logica_juego import iniciar_juego
from usuarios import *
from login import iniciar_sesion, registrar_usuario
import comodines

RUTA = "usuarios.json"  # archivo JSON donde se guardan los usuarios

def main() -> None:
    """
    Función principal del juego. Muestra el menú inicial y permite al usuario:
    - Iniciar sesión
    - Registrarse
    - Salir del juego

    No recibe parámetros y no devuelve nada (None) porque controla el flujo principal.
    """
    usuarios = cargar_usuarios(RUTA)  # cargamos los usuarios al inicio
    continuar = True

    while continuar:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                print(f"\n🎮 Bienvenido {usuario}! Iniciando juego...\n")
                iniciar_juego(usuario, usuarios, RUTA)  # pasamos usuarios y ruta
        elif opcion == "2":
            usuarios = registrar_usuario(usuarios, RUTA)  # registramos y guardamos en JSON
        elif opcion == "3":
            continuar = False
            print("👋 ¡Hasta luego!")
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
