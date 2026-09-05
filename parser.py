from nodos import nodo_binario, nodo_numero, nodo_positivo, nodo_negativo, nodo_identificador, nodo_asignacion

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
    tree = []
    estado = {
    "tokens"  : tokens,
    "puntero" : 0
    }

    if match("FIN", estado):
        raise Exception("Expresión vacia")
    
    while not match("FIN", estado):
        if estado["puntero"] < len(estado["tokens"]) - 1 and match("IDENTIFICADOR", estado) and match("ASIGNACION", estado, 1):
            token = advance(estado, 2)
            nodo = expr(estado)
            asign_tree = nodo_asignacion(token["valor"], nodo)
            tree.append(asign_tree)

        else:
            tree.append(expr(estado))

        if match("PUNTO_Y_COMA", estado):
            advance(estado)

        else:
            break
    
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
    nodo = power(estado)

    while match("MULTI", estado) or match("DIV", estado) or match("DIV_ENTERA", estado):
        operador = advance(estado)
        derecha = power(estado)
        nodo = nodo_binario(nodo, operador["valor"], derecha)

    return nodo   

def power(estado):
    nodo = factor(estado)

    if match("POTENCIA", estado) or match("RAIZ_ENESIMA", estado):
        operador = advance(estado)
        derecha = power(estado)

        return nodo_binario(nodo, operador["valor"], derecha)
    return nodo

def factor(estado):
    if match("PAREN_IZQ", estado):
        advance(estado)
        paren_tree = expr(estado)

        if not match("PAREN_DER", estado):
            raise ValueError("No cerraste un parentesis")

        else:
            advance(estado)

        return paren_tree
    
    elif match("SUMA", estado) or match("RESTA", estado):
        if match("SUMA", estado, 1) or match("RESTA", estado, 1):
            raise ValueError("Operador repetido")

        operador = advance(estado)

        if operador["tipo"] == "SUMA":
            return nodo_positivo(power(estado))
        
        elif operador["tipo"] == "RESTA":
            return nodo_negativo(power(estado))
        
    elif match("IDENTIFICADOR", estado):
        token = advance(estado)
        return nodo_identificador(token["valor"])
                
    elif match("NUMERO", estado):
        token = advance(estado)
        return nodo_numero(token["valor"])
    
    else:
        raise ValueError("Esperaba un número")
            
            
    