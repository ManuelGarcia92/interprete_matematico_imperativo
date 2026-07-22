def validar_expresion_vacia(expresion):
    if not expresion:
        raise ValueError("No hay operación.")

def validar_longitud(expresion, longitud = 3):
    if len(expresion) < longitud:
        raise ValueError("La operación no puede tener menos de 3 caracteres.")

def validar_permitidos(expresion, permitidos):
    invalido = set(expresion) - permitidos
    if invalido:
        raise ValueError(f"Caracteres no permitidos : {invalido}.")

def validar_extremos(expresion, operadores):
    if expresion[0] in operadores or expresion[-1] in operadores:
        raise ValueError("La operación no puede empezar ni terminar con un operador.")
    
def validar_operadores_repetidos(expresion, operadores):
    for i in range(len(expresion)):
        if i < len(expresion) - 1:
            if expresion[i] in operadores and expresion[i+1] in operadores:
                if expresion[i] + expresion[i+1] not in operadores:
                    raise ValueError(f"No puedes repetir los operadores : {expresion[i]} y {expresion[i+1]}.") 
        if i < len(expresion) - 2:
            if expresion[i] in operadores and expresion[i+1] in operadores and expresion[i+2] in operadores:
                raise ValueError(f"No puedes repetir tres o más operadores.")
                
def validar_puntos_decimales(expresion, operadores):
    contador_punto_flotante = 0
    for token in expresion:
        if token == ".":
            contador_punto_flotante += 1
        if contador_punto_flotante > 1:
            raise ValueError("Tienes un número decimal con más de un punto.")
        elif token in operadores or token in "()":
            contador_punto_flotante = 0 

def validar_numeros_decimales(expresion):
    for i in range(len(expresion)):
        if i > 0 and i < len(expresion) - 1:
            if expresion[i] == "." and not expresion[i+1].isdigit() and not expresion[i-1].isdigit():
                raise ValueError("Después o antes de los puntos decimales debe ir un número.")
            
def validar_parentesis(expresion):
    pila = []
    for token in expresion:
        if token == "(":
            pila.append(token)
        elif token == ")":
            if not pila:
                raise ValueError("Cerraste un paréntesis sin abrirlo.")
            pila.pop()
    if pila:
        raise ValueError("Te falto cerrar algun paréntesis.")
    
def validar_parentesis_vacios(expresion):
    if "()" in expresion:
        raise ValueError("Dentro de los paréntesis debes colocar una operación.")  
                            
def validar_parentesis_operadores(expresion, operadores):
    for i in range(len(expresion)):
        if i < len(expresion) - 1:
            if expresion[i] == "(" and expresion[i+1] in operadores and expresion[i+1] not in ("-", "+") :
                raise ValueError(f"No puedes poner el operador {expresion[i+1]} al principio de la operación dentro del paréntesis.")
            elif expresion[i] in operadores and expresion[i+1] == ")":
                raise ValueError(f"No puedes poner el operador {expresion[i]} al final de un paréntesis.")
        if i < len(expresion) - 2:
            if expresion[i] == "(" and expresion[i+1] in ("+","-") and expresion[i+2] != "." and not expresion[i+2].isdigit():
                raise ValueError("Después de un operador debe ir un número")
        

                