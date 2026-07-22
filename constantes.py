import datos
import logica

RUTA_JSON = datos.ruta_actual("registros.json")  

NUMEROS = set("1234567890")

OPERADORES = {"+","-","*","/","**","//","$"}

OPERADORES_ESPECIALES = {"(",")","."}

CARACTERES_PERMITIDOS = NUMEROS | OPERADORES | OPERADORES_ESPECIALES

OPERACIONES = {
    "**": lambda x, y: x ** y,
    "$" : lambda x, y: logica.calcular_raices(x, y),
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y,
    "//": lambda x, y: x // y,
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y
}

NIVELES_PRIORIDAD = [
    ["**", "$"],          
    ["*", "/", "//"],     
    ["+", "-"]           
]

MENU_PRINCIPAL = {
    "1": "Calculo",
    "2": "Registro de operaciones",
    "3": "Salir"
}