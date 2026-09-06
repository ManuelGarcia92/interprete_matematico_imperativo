from tabla_de_simbolos import tabla_de_simbolos
from lexer import tokenizar
from parser import parsear
from interprete import recorrer

def limpiar_terminal() -> None:
    import os
    os.system("cls" if os.name == "nt" else "clear")


while True:
    limpiar_terminal()
    print("[Ingrese xyz para salir.]")
    texto = input(">>> : ")
    memoria = tabla_de_simbolos()
    
    if texto == "xyz":
        break

    try:
        tokens = tokenizar(texto)
        arbol = parsear(tokens)
        resultado = recorrer(arbol, memoria, imprimir=True)
        if resultado:
            print(resultado)
        else:
            print()

    except Exception as error:
        print(error)

    input("Presione ENTER para continuar...")