def tokenizar_numeros(expresion, numeros):
    lista_tokens = []
    buffer_numero = ""
    for token in expresion:
        if token in numeros or token == ".":
            buffer_numero += token
        else:
            if buffer_numero:
                lista_tokens.append(buffer_numero)
            lista_tokens.append(token)
            buffer_numero = ""
    if buffer_numero:
        lista_tokens.append(buffer_numero)
    return lista_tokens

def tokenizar_decimales_implicitos(expresion):
    lista_tokens = []
    for token in expresion:
        if "." in token[0]:
            lista_tokens.append("0" + token)
        elif "." in token[-1]:
            lista_tokens.append(token + "0")
        else:
            lista_tokens.append(token)
    return lista_tokens

def tokenizar_operadores(expresion, operadores):
    lista_tokens = []
    for i, token in enumerate(expresion):
        if token in operadores:
            if i < len(expresion) - 1:
                if expresion[i] + expresion[i+1] in operadores:
                    lista_tokens.append(expresion[i] + expresion[i+1])
                elif i > 0:
                    if expresion[i] in operadores and expresion[i-1] not in operadores:
                        lista_tokens.append(token)
        else:            
            lista_tokens.append(token)
    return lista_tokens

def tokenizar_numeros_positivos_negativos(expresion):
    lista_tokens = []
    i = 0
    while i < len(expresion):
        token = expresion[i]
        if i < len(expresion) - 2 and expresion[i] == "(" and expresion[i+1] in ("-", "+"):
            lista_tokens.append(token)
            if expresion[i+1] == "-":
                lista_tokens.append(expresion[i+1] + expresion[i+2])
            else:
                lista_tokens.append(expresion[i+2])
            i += 3
        else:
            lista_tokens.append(token)
            i += 1
    return lista_tokens

def tokenizar_multiplicacion_implicita(expresion):
    lista_tokens = []
    for i, token in enumerate(expresion):
        lista_tokens.append(token)
        if i < len(expresion) - 1:
            if expresion[i].replace(".","", 1).isdigit() and expresion[i+1] == "(":
                lista_tokens.append("*")
            elif expresion[i] == ")" and expresion[i+1].replace(".","", 1).isdigit():
                lista_tokens.append("*")
            elif expresion[i] == ")" and expresion[i+1] == "(":
                lista_tokens.append("*")
    print(lista_tokens)
    return lista_tokens 
 
def tokenizar_potencias(expresion, operadores):
    lista_tokens = []
    contador = 0
    i = 0
    while i < len(expresion):
        token = expresion[i]
        if i < len(expresion) - 1 and expresion[i+1] == "**":
            if i < len(expresion) - 3 and expresion[i+3] == "**":
                lista_tokens.append(token)
                lista_tokens.append(expresion[i+1])
                lista_tokens.append("(")
                contador += 1
                i += 2
                continue
        lista_tokens.append(expresion[i])
        if i == len(expresion) - 1 or (i < len(expresion) - 1 and expresion[i+1] in operadores and expresion[i+1] != "**"):
            while contador > 0:
                lista_tokens.append(")")
                contador -= 1
        i += 1      
    return lista_tokens 

def conseguir_posiciones_parentesis(expresion):
    for i, token in enumerate(expresion):
        if token == "(":
            cara_izq = i
        elif token == ")":
            cara_der = i
            break
    return cara_izq, cara_der  

def calcular_raices(x, y):
    if x >= 0:
        return x ** (1 / y)
    else:
        raise ValueError("No se puede calcular raíces negativas.")
    
def calcular_operacion(operacion, operaciones, niveles_prioridad):
    for grupo_operadores in niveles_prioridad:
        i = 0
        while i < len(operacion) - 2:
            operador = operacion[i+1]
            if operador in grupo_operadores:
                primer_numero = float(operacion[i])
                segundo_numero = float(operacion[i+2])
                resultado = operaciones[operador](primer_numero, segundo_numero)
                operacion = operacion[:i] + [str(resultado)] + operacion[i+3:]
                print(f"{primer_numero} {operador} {segundo_numero} = {resultado}")   
            else:
                i += 2
    return operacion

