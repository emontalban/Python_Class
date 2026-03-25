import math

def pretty_price(number, decimal):
    if type(decimal) != float:
        decimal = decimal/ 100
    number = math.floor(number)

    resultado = number + decimal
    print(resultado)

    return resultado

pretty_price(3.20, 99)  
pretty_price(3.20, 0.99) 

# Solucion al ejercicio

def pretty_price(valor_bruto, extension):
    # 1. Verificamos si la extensión es un entero (ej. 99) o decimal (ej. 0.99)
    if isinstance(extension, int) or extension >= 1:
        extension = extension / 100
    
    # 2. Tomamos la parte entera del valor bruto y sumamos la extensión
    return int(valor_bruto) + extension

# Pruebas:
print(pretty_price(3.20, 99))   # 3.99
print(pretty_price(3.20, 0.95)) # 3.95
print(pretty_price(10.50, 0))   # 10.0 (Precio plano)

