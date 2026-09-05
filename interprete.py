def evaluar(nodo, imprimir=False):
    if nodo["tipo"] == "nodo_numero":
        return nodo["valor"]
    
    elif nodo["tipo"] == "nodo_binario":
        izquierda = evaluar(nodo["izquierda"], imprimir)
        derecha = evaluar(nodo["derecha"], imprimir)
       
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
                    print(f"{izquierda} $ {derecha} = {-(-izquierda) ** (1 / derecha)}")
        
                else:
                    print(f"{izquierda} $ {derecha} = {izquierda ** (1 / derecha)}")

            if izquierda < 0 and derecha % 2 != 0:
                return -(-izquierda) ** (1 / derecha)
            return izquierda ** (1 / derecha)
          
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
        
        

        
