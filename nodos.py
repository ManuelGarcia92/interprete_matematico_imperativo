def nodo_binario(operador, izquierda, derecha):
    return {
    "tipo"      : "nodo_binario",  
    "operador"  : operador, 
    "izquierda" : izquierda,
    "derecha"   : derecha
    }

def nodo_numero(valor):
    return {
    "tipo"  : "nodo_numero",
    "valor" : valor
    }

def nodo_positivo(valor):
    return {
    "tipo"  : "nodo_positivo",
    "valor" : valor
    }

def nodo_negativo(valor):
    return {
    "tipo"  : "nodo_negativo",
    "valor" : valor
    }

def nodo_identificador(nombre):
    return {
    "tipo"       : "nodo_identificador",
    "var_nombre" : nombre
    }

def nodo_asignacion(var_nombre, var_valor):
    return {
    "tipo"       : "nodo_asignacion",
    "var_nombre" : var_nombre,
    "var_valor"  : var_valor
    }