def evaluar(nodo, imprimir=False):
    if nodo["tipo"] == "nodo_numero":
        return nodo["valor"]
    
    elif nodo["tipo"] == "nodo_binario":
        derecha = evaluar(nodo["derecha"], imprimir)
        izquierda = evaluar(nodo["izquierda"], imprimir)
       
        if nodo["operador"] == "+":
            if imprimir:
                print(f"{derecha} + {izquierda} = {derecha + izquierda}")
            return derecha + izquierda
            
        elif nodo["operador"] == "-":
            if imprimir:
                print(f"{derecha} - {izquierda} = {derecha - izquierda}")
            return derecha - izquierda
          
        elif nodo["operador"] == "*":
            if imprimir:
                print(f"{derecha} * {izquierda} = {derecha * izquierda}")
            return derecha * izquierda
           
        elif nodo["operador"] == "/":
            if imprimir:
                print(f"{derecha} / {izquierda} = {derecha / izquierda}")
            return derecha / izquierda

