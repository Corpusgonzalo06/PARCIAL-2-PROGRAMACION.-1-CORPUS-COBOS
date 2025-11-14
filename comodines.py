#comodines.py
from mis_funciones import *

def revelar_palabra(palabra_correcta: str) -> None:
    """
    Muestra en pantalla la palabra correcta.
    """
    print("💡 La palabra correcta era: " + palabra_correcta)


def eliminar_restricciones(vidas: int) -> int:
    """
    Permite al jugador tener un intento libre sin perder vida.
    """
    print("🚀 Restricciones eliminadas. Tenés un intento libre sin perder vida.")
    return vidas


def dar_pista_extra(palabra_correcta: str) -> None:
    """
    Muestra una pista extra indicando la primera letra de la palabra.
    """
    primera_letra = palabra_correcta[0]
    letra_minuscula = convertir_a_minusculas(primera_letra)
    print("🕵️ Pista extra: la palabra empieza con '" + letra_minuscula + "'")


def usar_comodin(opcion: int, palabra_correcta: str, vidas: int) -> int:
    """
    Ejecuta la acción del comodín seleccionado.
    """
    match opcion:
        case 1:
            revelar_palabra(palabra_correcta)
        case 2:
            vidas = eliminar_restricciones(vidas)
        case 3:
            dar_pista_extra(palabra_correcta)
        case _:
            print("⚠️ Comodín desconocido")
    return vidas

def preguntar_uso_comodin() -> bool:
    """
    Pregunta al jugador si desea usar un comodín.
    """
    resultado = False
    while True:
        usar = input("¿Querés usar un comodín? (si/no): ")

        if usar == "si" or usar == "Si" or usar == "sI" or usar == "SI":
            resultado = True
            break
        elif usar == "no" or usar == "No" or usar == "nO" or usar == "NO":
            resultado = False
            break
        else:
            print("Por favor, ingresá 'si' o 'no'.")

    return resultado

def obtener_comodines_disponibles(comodines_jugador: dict) -> list:
    """
    Obtiene la lista de comodines que todavía están disponibles.
    """
    disponibles = []
    for nombre in comodines_jugador:
        if comodines_jugador[nombre] == True:
            # guardamos el nombre en la lista de disponibles
            largo = len(disponibles)
            disponibles += [nombre] 
    return disponibles


def manejar_comodines(comodines_jugador: dict, palabra_correcta: str, vidas_actuales: int) -> int:
    """
    Maneja el uso de comodines durante la partida (sin métodos ni try/except).
    """
    disponibles = obtener_comodines_disponibles(comodines_jugador)

    if len(disponibles) == 0:
        print("🚫 No te quedan comodines disponibles.")
        return vidas_actuales

    usar = preguntar_uso_comodin()
    if usar == True:
        print()
        print("🎁 Comodines disponibles:")
        print()
        indice = 0
        while indice < len(disponibles):
            print(str(indice + 1) + ". " + disponibles[indice])
            indice += 1

        opcion = input("Elegí el número del comodín que querés usar: ")

   
        es_numero = True
        contador = 0
        while contador < len(opcion):
            if opcion[contador] < "0" or opcion[contador] > "9":
                es_numero = False
            contador += 1

        if es_numero == True:
            opcion_num = 0
            contador = 0
            while contador < len(opcion):
                opcion_num = opcion_num * 10 + (ord(opcion[contador]) - 48)
                contador += 1

            if opcion_num >= 1 and opcion_num <= len(disponibles):
                nombre = disponibles[opcion_num - 1]
                vidas_actuales = usar_comodin(opcion_num, palabra_correcta, vidas_actuales)
                comodines_jugador[nombre] = False  # marcar como usado
            else:
                print("⚠️ Número fuera de rango.")
        else:
            print("⚠️ Debés ingresar un número válido.")
    return vidas_actuales
