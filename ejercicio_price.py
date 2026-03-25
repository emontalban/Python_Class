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