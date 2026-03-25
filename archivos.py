archivo = open("archivo.txt", "w")
archivo.write("Hola mundo\n")
archivo.write("Segunda línea\n")
archivo.close()

archivo = open("archivo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

file_builder = open("logger.txt", "w+")

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n")

file_builder.close()
