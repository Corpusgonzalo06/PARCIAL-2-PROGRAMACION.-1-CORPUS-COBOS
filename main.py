from logica_juego import iniciar_juego
from usuarios import cargar_usuarios
from login import iniciar_sesion, registrar_usuario

RUTA = "usuarios.json"

def main() -> None:
    usuarios = cargar_usuarios(RUTA)
    continuar = True

    while continuar:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                usuario, nombre_usuario = iniciar_sesion(usuarios)
                if usuario:
                    print(f"\n🎮 Bienvenido {nombre_usuario}! Iniciando juego...\n")
                    # <- PASAMOS el nombre del usuario para que se guarden los datos correctamente
                    iniciar_juego(usuario, RUTA, vidas=3, clave_usuario=nombre_usuario)

            case "2":
                usuarios = registrar_usuario(usuarios, RUTA)

            case "3":
                continuar = False
                print("👋 ¡Hasta luego!")

            case _:
                print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
