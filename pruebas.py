class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

p = Persona("Ana", 30)
print(p) # -> Ana, 30 años
print(str(p))