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

# Buqueda de archivos
import fnmatch
import os


lenguajes= [
    "python interpretado",
    "Java compilado",
    "C compilado",
    "JavaScript interpretado",
    "Ruby interpretado"
]
lenguajes_tipo = [tipo for tipo in lenguajes if fnmatch.fnmatchcase(tipo, "* interpretado")]

lenguajes_tipo_two = [tipo for tipo in lenguajes if fnmatch.fnmatch(tipo, "* INTERPRETADO")] # no distingue entre mayusculas y minusculas

print(lenguajes_tipo)
print(lenguajes_tipo_two)

# Busqueda de archivos

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch.fnmatch(file, '*.md'):
            print('Markdown files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()