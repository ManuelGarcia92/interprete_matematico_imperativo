def tabla_de_simbolos():
    return {
    "pi" : 3.1415926536,
    "e"  : 2.7182818285
    }

def declarar(memoria, nombre, valor):
    if nombre in memoria:
        raise Exception(f"Error semántico: La variable {nombre} ya ha sido declarada.")
    memoria[nombre] = valor

def obtener(memoria, nombre):
    if nombre not in memoria:
        raise Exception(f"Error semántico: La variable {nombre} no esta definida.")
    return memoria[nombre]
