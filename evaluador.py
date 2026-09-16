from tabla_de_simbolos import declarar_variable, obtener_variable

def evaluar(nodo, memoria, imprimir=False):
    if nodo["tipo"] == "nodo_numero":
        return nodo["valor"]
    
    elif nodo["tipo"] == "nodo_positivo":
        return evaluar(nodo["valor"], memoria, imprimir)

    elif nodo["tipo"] == "nodo_negativo":
        return -evaluar(nodo["valor"], memoria, imprimir)
    
    elif nodo["tipo"] == "nodo_asignacion":
        variable = evaluar(nodo["var_valor"], memoria, imprimir=True)
        return declarar_variable(memoria, nodo["var_nombre"], variable)
    
    elif nodo["tipo"] == "nodo_identificador":
        return obtener_variable(memoria, nodo["var_nombre"])

    elif nodo["tipo"] == "nodo_binario":
        izquierda = evaluar(nodo["izquierda"], memoria, imprimir)
        derecha = evaluar(nodo["derecha"], memoria, imprimir)
       
        if nodo["operador"] == "+":
            if imprimir:
                print(f"{izquierda} + {derecha} = {izquierda + derecha}")
            return izquierda + derecha
            
        elif nodo["operador"] == "-":
            if imprimir:
                print(f"{izquierda} - {derecha} = {izquierda - derecha}")
            return izquierda - derecha
          
        elif nodo["operador"] == "*":
            if imprimir:
                print(f"{izquierda} * {derecha} = {izquierda * derecha}")
            return izquierda * derecha
        
        elif nodo["operador"] == "**":
            if imprimir:
                print(f"{izquierda} ** {derecha} = {izquierda ** derecha}")
            return izquierda ** derecha
        
        elif nodo["operador"] == "$":
            if imprimir:
                if izquierda < 0 and derecha % 2 != 0:
                    print(f"{izquierda} $ {derecha} = {-(-derecha) ** (1 / izquierda)}")
        
                else:
                    print(f"{izquierda} $ {derecha} = {derecha ** (1 / izquierda)}")

            if derecha < 0 and izquierda % 2 != 0:
                return -(-derecha) ** (1 / izquierda)
            return derecha ** (1 / izquierda)
          
        elif nodo["operador"] == "/":
            if derecha == 0:
                raise Exception("ERROR: No se puede dividir por 0")
            
            if imprimir:
                print(f"{izquierda} / {derecha} = {izquierda / derecha}")
            return izquierda / derecha
        
        elif nodo["operador"] == "//":
            if derecha == 0:
                raise Exception("ERROR: No se puede dividir por 0")
            
            if imprimir:
                print(f"{izquierda} // {derecha} = {izquierda // derecha}")
            return izquierda // derecha
        
def recorrer(arboles, memoria, imprimir):
    resultado = None
    for arbol in arboles:
        resultado = evaluar(arbol, memoria, imprimir)
    return resultado       

        
