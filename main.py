from extras import limpiar_terminal, pausa
from tabla_de_simbolos import tabla_de_simbolos
from lexer import tokenizar
from parser import parsear
from evaluador import evaluar

def main() -> None:
    while True:
        limpiar_terminal()
        print("[Ingrese break para salir]")
        texto = input(">>> : ")
        if texto == "break":
            break
        try:
            tokens = tokenizar(texto)
            arbol = parsear(tokens)
            memoria = tabla_de_simbolos()
            resultado = evaluar(arbol, memoria)
            if resultado == None:
                print()
            else:
                print(resultado)
        except Exception as error:
            print(error)
        pausa()
    
if __name__ == "__main__":
    main()