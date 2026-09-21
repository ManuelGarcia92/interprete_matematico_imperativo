from tabla_de_simbolos import declarar_variable, obtener_variable 
from constantes import OPERACIONES

def recorrer(nodo, memoria):
    if nodo["tipo"] == "nodo_numero":
        return nodo["valor"]
    
    elif nodo["tipo"] == "nodo_positivo":
        return recorrer(nodo["valor"], memoria)

    elif nodo["tipo"] == "nodo_negativo":
        return -recorrer(nodo["valor"], memoria)
    
    elif nodo["tipo"] == "nodo_asignacion":
        variable = recorrer(nodo["var_valor"], memoria)
        return declarar_variable(memoria, nodo["var_nombre"], variable)
    
    elif nodo["tipo"] == "nodo_identificador":
        return obtener_variable(memoria, nodo["var_nombre"])

    elif nodo["tipo"] == "nodo_binario":
        operador = nodo["operador"]
        izquierda = recorrer(nodo["izquierda"], memoria)
        derecha = recorrer(nodo["derecha"], memoria)
        resultado = OPERACIONES[operador](izquierda, derecha)
        return resultado
    
def evaluar(arboles, memoria):
    resultado = None
    for arbol in arboles:
        resultado = recorrer(arbol, memoria)
    return resultado       

        
