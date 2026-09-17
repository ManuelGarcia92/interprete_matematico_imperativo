import tabla_de_simbolos 

def evaluar(nodo, memoria):
    if nodo["tipo"] == "nodo_numero":
        return nodo["valor"]
    
    elif nodo["tipo"] == "nodo_positivo":
        return evaluar(nodo["valor"], memoria)

    elif nodo["tipo"] == "nodo_negativo":
        return -evaluar(nodo["valor"], memoria)
    
    elif nodo["tipo"] == "nodo_asignacion":
        variable = evaluar(nodo["var_valor"], memoria)
        return tabla_de_simbolos.declarar_variable(memoria, nodo["var_nombre"], variable)
    
    elif nodo["tipo"] == "nodo_identificador":
        return tabla_de_simbolos.obtener_variable(memoria, nodo["var_nombre"])

    elif nodo["tipo"] == "nodo_binario":
        izquierda = evaluar(nodo["izquierda"], memoria)
        derecha = evaluar(nodo["derecha"], memoria)
       
        if nodo["operador"] == "+":
            return izquierda + derecha
            
        elif nodo["operador"] == "-":
            return izquierda - derecha
          
        elif nodo["operador"] == "*":
            return izquierda * derecha
        
        elif nodo["operador"] == "**":
            return izquierda ** derecha
        
        elif nodo["operador"] == "$":
            if derecha < 0 and izquierda % 2 != 0:
                return -(-derecha) ** (1 / izquierda)
            return derecha ** (1 / izquierda)
          
        elif nodo["operador"] == "/":
            if derecha == 0:
                raise Exception("ERROR: No se puede dividir por 0")
            return izquierda / derecha
        
        elif nodo["operador"] == "//":
            if derecha == 0:
                raise Exception("ERROR: No se puede dividir por 0")
            return izquierda // derecha
        
def recorrer(arboles, memoria):
    resultado = None
    for arbol in arboles:
        resultado = evaluar(arbol, memoria)
    return resultado       

        
