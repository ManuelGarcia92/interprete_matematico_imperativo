from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES

def token(tipo, valor):
    return {
        "tipo" : tipo,
        "valor" : valor
    }

def leer_palabra(texto, puntero):
    buffer = ""

    while puntero < len(texto) and (texto[puntero].isalnum() or texto[puntero] == "_"):
        buffer += texto[puntero]
        puntero += 1
        
    return puntero, token("IDENTIFICADOR", buffer)

def leer_numero(texto, puntero):
    contador_punto_decimal = 0
    buffer = ""
    
    while puntero < len(texto) and (texto[puntero].isdigit() or texto[puntero] == "."):
        if texto[puntero] == ".":
            contador_punto_decimal += 1
            
        buffer += texto[puntero]
        puntero += 1

    if contador_punto_decimal > 1 or buffer == ".":
        return puntero, token("ERROR", buffer)
    
    if contador_punto_decimal:
        if buffer[0] == ".":
            buffer = "0" + buffer

        elif buffer[-1] == ".":
            buffer += "0"

        return puntero, token("NUMERO", float(buffer))
    
    return puntero, token("NUMERO", int(buffer))

def leer_simbolo(texto, puntero):
    if puntero < len(texto):

        if puntero < len(texto) - 1 and texto[puntero] + texto[puntero + 1] in OPERADORES_DOBLES:
            valor_token = texto[puntero] + texto[puntero + 1]
            tipo_token = OPERADORES_DOBLES[valor_token]
            puntero += 2
            
        else:
            valor_token = texto[puntero]
            tipo_token = OPERADORES_SIMPLES[valor_token]
            puntero += 1  

        return puntero, token(tipo_token, valor_token)

def tokenizar(texto):
    tokens  = [] 
    puntero = 0
    
    while puntero < len(texto):
        char_actual = texto[puntero]

        if char_actual.isspace():
            puntero += 1

        elif char_actual.isalpha() or char_actual == "_" :
            puntero, palabra = leer_palabra(texto, puntero)
            tokens.append(palabra)

        elif char_actual.isdigit() or char_actual == ".":
            puntero, numero = leer_numero(texto, puntero)
            tokens.append(numero)

        elif char_actual in OPERADORES_SIMPLES:
            puntero, simbolo = leer_simbolo(texto, puntero)
            tokens.append(simbolo)

        else:
            tokens.append(token("ERROR", char_actual))
            puntero += 1

    tokens.append(token("FIN", None))
    return tokens

