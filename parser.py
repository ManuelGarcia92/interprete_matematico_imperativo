def nodo_binario(izquierda, operador, derecha):
    return {
    "tipo"      : "nodo_binario",   
    "izquierda" : izquierda,
    "operador"  : operador,
    "derecha"   : derecha
    }

def nodo_numero(valor):
    return {
    "tipo"  : "nodo_numero",
    "valor" : valor
    }

def advance(estado, pasos=1):
    if estado["puntero"] + pasos < len(estado["tokens"]):
        token = estado["tokens"][estado["puntero"]]
        estado["puntero"] += pasos
        return token
    return None

def peek(estado, pasos=0):
    pos = estado["puntero"] + pasos
    if pos < len(estado["tokens"]):
        return estado["tokens"][pos]
    return None

def match(tipo, estado, pasos=0):
    token = peek(estado, pasos)
    if token and token["tipo"] == tipo:
        return token 
    return None

def parsear(tokens):
    estado = {
    "tokens"  : tokens,
    "puntero" : 0
    }

    if match("FIN", estado):
        raise Exception("Expresión vacia")
    
    tree = expr(estado)

    token_actual = peek(estado)
    
    if token_actual and token_actual["tipo"] != "FIN":
        raise ValueError("Quedan tokens sin procesar")
    
    return tree

def expr(estado):
    nodo = term(estado)

    while match("SUMA", estado) or match("RESTA", estado):
        operador = advance(estado)
        derecha = term(estado)
        nodo = nodo_binario(nodo, operador["valor"], derecha)

    return nodo

def term(estado):
    nodo = factor(estado)

    while match("MULTI", estado) or match("DIV", estado) or match("DIV_ENTERA", estado):
        operador = advance(estado)
        derecha = factor(estado)
        nodo = nodo_binario(nodo, operador["valor"], derecha)

    return nodo   

def factor(estado):
    if match("NUMERO", estado):
        token = advance(estado)
        return nodo_numero(token["valor"])
    
    else:
        raise ValueError("Esperaba un número")
            
            
    