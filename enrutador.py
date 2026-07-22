import datos
import constantes
import interfaz
import validaciones
import logica

def validar_expresion(expresion, permitidos, operadores):
    validaciones.validar_expresion_vacia(expresion)
    validaciones.validar_longitud(expresion)
    validaciones.validar_permitidos(expresion, permitidos)
    validaciones.validar_extremos(expresion, operadores)
    validaciones.validar_operadores_repetidos(expresion, operadores)
    validaciones.validar_puntos_decimales(expresion, operadores)
    validaciones.validar_numeros_decimales(expresion)
    if "(" in expresion or ")" in expresion:
        validaciones.validar_parentesis(expresion)
        validaciones.validar_parentesis_vacios(expresion)
        validaciones.validar_parentesis_operadores(expresion, operadores)
        
def tokenizar_expresion(expresion, numeros, operadores):
    lista_tokens = logica.tokenizar_numeros(expresion, numeros)
    lista_tokens = logica.tokenizar_decimales_implicitos(lista_tokens)
    lista_tokens = logica.tokenizar_operadores(lista_tokens, operadores)
    lista_tokens = logica.tokenizar_numeros_positivos_negativos(lista_tokens)
    return logica.tokenizar_multiplicacion_implicita(lista_tokens)

def calcular_expresion(expresion):
        lista_tokens = logica.tokenizar_potencias(expresion, constantes.OPERADORES)
        while "(" in lista_tokens:
            izq, der = logica.conseguir_posiciones_parentesis(lista_tokens)
            sub_expresion = lista_tokens[izq + 1 : der]
            sub_resultado = logica.calcular_operacion(sub_expresion, constantes.OPERACIONES, constantes.NIVELES_PRIORIDAD)
            lista_tokens = lista_tokens[:izq] + sub_resultado + lista_tokens[der + 1:]
        return logica.calcular_operacion(lista_tokens, constantes.OPERACIONES, constantes.NIVELES_PRIORIDAD)
  
def guardar_registro_operaciones(operacion):
    registro = datos.cargar_datos(constantes.RUTA_JSON)
    registro.append(operacion)
    datos.guardar_datos(constantes.RUTA_JSON, registro)

def ver_registro():
    registro = datos.cargar_datos(constantes.RUTA_JSON)
    return interfaz.mostrar_registro(registro)

def calculo():
    while True:
        interfaz.limpiar_terminal()
        expresion = input(">>> : ").replace(" ","")
        if expresion == "xyz":
            break
        else:
            try:
                validar_expresion(expresion, constantes.CARACTERES_PERMITIDOS, constantes.OPERADORES)
                lista_tokens = tokenizar_expresion(expresion, constantes.NUMEROS ,constantes.OPERADORES)
                while "(" in lista_tokens:
                    izq, der = logica.conseguir_posiciones_parentesis(lista_tokens)
                    sub_expresion = lista_tokens[izq + 1 : der]
                    sub_resultado = calcular_expresion(sub_expresion)
                    lista_tokens = lista_tokens[:izq] + sub_resultado + lista_tokens[der + 1:]
                resultado_final = calcular_expresion(lista_tokens)
                resultado = round(float(resultado_final[0]), 4)
                operacion = {"operacion" : expresion, "resultado": resultado}
                guardar_registro_operaciones(operacion)
                interfaz.mostrar_mensaje(resultado) 
            except ValueError as error:
                interfaz.mostrar_error(error)
            except ZeroDivisionError:
                interfaz.mostrar_error("No se puede dividir por cero.")
            except OverflowError:
                interfaz.mostrar_error("El número resultante es demasiado grande.")
        interfaz.pausa()
        
def iniciar_sistema():
    while True:
        interfaz.limpiar_terminal()
        interfaz.mostrar_titulo("INTÉRPRETE MATEMÁTICO v0.8")
        interfaz.mostrar_menu(constantes.MENU_PRINCIPAL)
        opcion = interfaz.pedir_dato(">>> : ")
        if opcion == "3":
            interfaz.mostrar_mensaje("Saliendo...")
            break
        elif opcion == "1":
            calculo()
        elif opcion == "2":
            interfaz.limpiar_terminal()
            interfaz.mostrar_titulo("Registro de operaciones.")
            ver_registro()
        else:
            interfaz.mostrar_error(f"La opción: {opcion} no existe.")
        interfaz.pausa()
            
        

