from lexer import tokenizar
from parser import parsear
from interprete import evaluar

def limpiar_terminal() -> None:
    import os
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpiar_terminal()
    print("[Ingrese xyz para salir.]")
    texto = input(">>> : ")

    if texto == "xyz":
        break

    try:
        tokens = tokenizar(texto)
        arbol = parsear(tokens)
        resultado = evaluar(arbol, imprimir=True)
        print(resultado)

    except Exception as error:
        print(error)

    input("Presione ENTER para continuar...")