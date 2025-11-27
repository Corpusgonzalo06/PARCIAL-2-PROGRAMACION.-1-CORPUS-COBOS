from mis_funciones import crear_mi_separador, convertir_a_minusculas, agregar_elemento

# ===========================
# VALIDAR PALABRA INGRESADA
# ===========================

def validar_palabra_ingresada(palabra_ingresada: str, palabra_correcta: str) -> bool:
    """
    Valida si la palabra ingresada coincide con la palabra correcta,
    ignorando mayúsculas, espacios y tabulaciones.

    Parámetros:
        palabra_ingresada (str): Palabra ingresada por el usuario.
        palabra_correcta (str): Palabra correcta que se debe validar.

    Retorna:
        bool: True si la palabra ingresada es correcta, False si no.
    """
    # Convertir a minúsculas y quitar espacios/tabulaciones manualmente
    palabra_procesada = ""
    for char in palabra_ingresada:
        if char != " " and char != "\t":
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

def validar_letras_usadas(palabra_ingresada: str, letras_disponibles: list) -> bool:
    """
    Valida si todas las letras de la palabra ingresada están disponibles
    en la lista de letras disponibles, ignorando mayúsculas y espacios.

    Parámetros:
        palabra_ingresada (str): Palabra que el usuario quiere usar.
        letras_disponibles (list): Lista de letras disponibles.

    Retorna:
        bool: True si todas las letras están disponibles, False si no.
    """
    # Convertir palabra a minúsculas y quitar espacios
    palabra_procesada = ""
    for char in palabra_ingresada:
        if char != " " and char != "\t":
            palabra_procesada += convertir_a_minusculas(char)

    # Crear copia de letras disponibles sin usar append
    letras_procesadas = []
    for letra in letras_disponibles:
        letras_procesadas = agregar_elemento(letras_procesadas, convertir_a_minusculas(letra))

    # Validar letra por letra
    resultado = True

    for letra in palabra_procesada:
        encontrada = False
        for i in range(len(letras_procesadas)):
            if letras_procesadas[i] == letra:
                encontrada = True
                letras_procesadas[i] = ""   # removemos la letra usada
                break

        if not encontrada:
            print(f"⚠️ La letra '{letra}' no está disponible.")
            resultado = False
            break

    return resultado


# ===========================
# VALIDAR PALABRA GENERAL
# ===========================

def validar_palabra(palabra: str, lista: list, usadas: list) -> bool:
    """
    Valida si una palabra es válida según la lista de palabras permitidas
    y si no ha sido usada previamente.

    Parámetros:
        palabra (str): Palabra a validar.
        lista (list): Lista de palabras permitidas.
        usadas (list): Lista de palabras ya usadas.

    Retorna:
        bool: True si la palabra es válida y no ha sido usada, False si no.
    """
   
    partes = crear_mi_separador(palabra, " ")
    palabra_limpia = ""
    i = 0
    while i < len(partes):
        if partes[i] != "":
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
    if encontrada and (not usada):
        es_valida = True

    return es_valida
