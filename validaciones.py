# validaciones.py
from mis_funciones import crear_mi_separador , convertir_a_minusculas
# ===========================
# VALIDAR PALABRA INGRESADA
# ===========================
def validar_palabra_ingresada(palabra_ingresada, palabra_correcta):
    # Convertir a minúsculas y quitar espacios/tabulaciones manualmente
    palabra_procesada = ""
    for char in palabra_ingresada:
        if char != " " and char != "\t":
            # convertir mayúsculas a minúsculas
            codigo = ord(char)
            if 65 <= codigo <= 90:
                palabra_procesada += chr(codigo + 32)
            else:
                palabra_procesada += char

    palabra_objetivo = ""
    for char in palabra_correcta:
        if char != " " and char != "\t":
            codigo = ord(char)
            if 65 <= codigo <= 90:
                palabra_objetivo += chr(codigo + 32)
            else:
                palabra_objetivo += char

    resultado = True

    if palabra_procesada == "":
        print("⚠️ No ingresaste ninguna palabra.")
        resultado = False
    else:
        if len(palabra_procesada) != len(palabra_objetivo):
            resultado = False
        else:
            for i in range(len(palabra_procesada)):
                if palabra_procesada[i] != palabra_objetivo[i]:
                    resultado = False
                    break

    return resultado

# ===========================
# VALIDAR LETRAS USADAS
# ===========================
def validar_letras_usadas(palabra_ingresada, letras_disponibles):
    # Convertir palabra a minúsculas y quitar espacios
    palabra_procesada = ""
    for char in palabra_ingresada:
        if char != " " and char != "\t":
            codigo = ord(char)
            if 65 <= codigo <= 90:
                palabra_procesada += chr(codigo + 32)
            else:
                palabra_procesada += char

    # Crear copia manual de letras disponibles en minúsculas
    letras_procesadas = []
    for letra in letras_disponibles:
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            letras_procesadas.append(chr(codigo + 32))
        else:
            letras_procesadas.append(letra)

    resultado = True

    for letra in palabra_procesada:
        encontrada = False
        for i in range(len(letras_procesadas)):
            if letras_procesadas[i] == letra:
                encontrada = True
                letras_procesadas[i] = ""  # "remover" letra manualmente
                break
        if not encontrada:
            print(f"⚠️ La letra '{letra}' no está disponible.")
            resultado = False
            break

    return resultado

def validar_palabra(palabra, lista, usadas):
    # Simular strip usando crear_mi_separador
    partes = crear_mi_separador(palabra, " ")

    palabra_limpia = ""
    i = 0
    while i < len(partes):
        if partes[i] != "":     # si no está vacío
            palabra_limpia = partes[i]
        i += 1

    palabra_limpia = convertir_a_minusculas(palabra_limpia)

    # Buscar si está en la lista
    encontrada = False
    i = 0
    while i < len(lista):
        if lista[i] == palabra_limpia:
            encontrada = True
        i += 1

    # Buscar si ya fue usada
    usada = False
    i = 0
    while i < len(usadas):
        if usadas[i] == palabra_limpia:
            usada = True
        i += 1

    # Valor final con un solo return
    es_valida = False
    if encontrada:
        if not usada:
            es_valida = True

    return es_valida
