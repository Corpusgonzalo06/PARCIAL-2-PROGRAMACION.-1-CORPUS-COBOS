# funciones_auxiliares.py
import random
from palabras import PALABRAS
from mis_funciones import agregar_elemento, copiar_lista


# ===========================
# FUNCIONES DE PANTALLA
# ===========================

def mostrar_encabezado_de_juego() -> None:
    print("\n")
    print("==============================================")
    print("🎮 BIENVENIDO A 'PALABRAS EN PALABRA' 🎮")
    print("==============================================")
    print("🔥 OBJETIVO: formar palabras correctas usando")
    print("   las letras mezcladas que se te muestran.\n")


def mostrar_encabezado_de_nivel(nivel: int) -> None:
    print(f"\n========== NIVEL {nivel} ==========")


# ===========================
# FUNCIONES DE PALABRAS
# ===========================

def mezclar_lista(lista: list) -> list:
    """
    Mezcla una lista usando random.shuffle pero sin métodos de lista.
    """
    copia = copiar_lista(lista)
    random.shuffle(copia)
    return copia


def preparar_palabra_desordenada(palabra: str) -> list:
    """
    Convierte palabra → lista y la mezcla.
    Sin join, sin append.
    """
    letras = []
    i = 0
    while i < len(palabra):
        letras = agregar_elemento(letras, palabra[i])
        i += 1

    return mezclar_lista(letras)


def mostrar_letras(letras: list) -> None:
    """
    Muestra las letras sin usar join().
    """
    print("\n🔠 Letras disponibles:")
    i = 0
    while i < len(letras):
        print(letras[i], end=" ")
        i += 1
    print("\n------------------------------")


# ===========================
# FUNCIONES PARA NIVELES
# ===========================
def obtener_palabras_del_nivel(nivel: int) -> dict:
    """
    Devuelve un diccionario con:
    - palabra_base
    - letras_desordenadas
    - palabras_validas
    """
    
    # crear lista de claves sin usar keys()
    claves = []
    for clave in PALABRAS:
        claves = agregar_elemento(claves, clave)

    # elegir índice aleatorio
    total = len(claves)
    indice = random.randint(0, total - 1)
    palabra_base = claves[indice]

    # obtener palabras válidas
    palabras_validas = PALABRAS[palabra_base]

    # generar letras desordenadas
    letras = preparar_palabra_desordenada(palabra_base)

    # retornar en un diccionario como quiere tu profe
    resultado = {
        "palabra_base": palabra_base,
        "letras": letras,
        "validas": palabras_validas
    }

    return resultado
