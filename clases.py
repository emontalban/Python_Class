class Language:

    def __init__(self, name, year, type, extension, creator):
        self.name = name
        self.year = year
        self.type = type
        self.extension = extension
        self.creator = creator

    def __str__(self):
        return (f'Language {self.name} was created by {self.creator} in the year {self.year}, it is of type {self.type} and has an extension {self.extension}')
    
    def __repr__(self):
        return(f'Language: {self.name}, {self.creator}, {self.year}, {self.type}, {self.extension}')

language_one = Language('Python', 1991,'interpretado','.py','Guido van Rossum')    
language_two = Language('Ruby', 1995, 'interpretado', '.rb', 'Yukihiro Matsumoto')
print(str(language_one))
print(repr(language_two))

print(" ")

class Lenguajes:
    def __init__(self, lista):
        self.lista = lista
        self.last_index = len(lista) - 1
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        lenguaje = self.lista[self.n]

        if self.n < self.last_index:
            self.n += 1
        else:
            self.n = 0

        return lenguaje
    
lenguajes = ["Python", "JavaScript", "Java", "C++"]

bucle = Lenguajes(lenguajes)
it = iter(bucle)

print(next(it))  # Python
print(next(it))  # JavaScript
print(next(it))  # Java
print(next(it))  # C++
print(next(it))  # Python (reinicia)
print(next(it))  # JavaScript

print(" ")

#Ejercicio del profesor
class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))


## uso de yield
print("**********************************************")
class InfinityLoop:
    def __init__(self,languages):
        self.languages = languages

    def cycle(self):
        total_index = len(self.languages)
        current_index  = 0

        while  True:
            if current_index  < total_index:
                yield self.languages[current_index]
            else:
                current_index = 0
                yield self.languages[current_index]

            current_index += 1

    def __str__(self):
            return f"InfinityLoop: {(self.languages)}"  

# bucle = InfinityLoop(lenguajes).cycle()
favorite_languages = InfinityLoop(lenguajes)
bucle = favorite_languages.cycle()

print(next(bucle))
print(next(bucle))
print(next(bucle))
print(next(bucle))
print(next(bucle))


print("**********************************************")

#atributo de clase y atributo de instancia
class NewLanguage:
    categoria = "Programación"  # atributo de clase

    def __init__(self, nombre, paradigma):
        self.nombre = nombre
        self.paradigma = paradigma

    def mostrar_info(self):
        print(f"{self.nombre} es de tipo {self.categoria} y paradigma {self.paradigma}")

l1 = NewLanguage("Python", "multiparadigma")
l2 = NewLanguage("JavaScript","multiparadigma")

l1.mostrar_info()
l2.categoria = "Programacion de alto nivel"
l2.mostrar_info()

print(l1.__dict__)
print(l2.__dict__)

print(NewLanguage.__dict__['categoria'])

print("**********************************************")

#herencia

class Lenguaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        return f"{self.nombre} se puede ejecutar"
    
class LenguajeCompilado(Lenguaje):
    def compilar(self):
        return f"{self.nombre} necesita ser compilado"

class LenguajeInterpretado(Lenguaje):
    def interpretar(self):
        return f"{self.nombre} se ejecuta sin compilar"

l1 = Lenguaje("JavaScript")    
python = LenguajeInterpretado("Python")
c = LenguajeCompilado("C")

print(l1.ejecutar())       # Propio del padre

print(python.ejecutar())     # Propio del padre que heredan los hijos
print(python.interpretar())  # propio del hijo

print(c.ejecutar())         #  Propio del padre que heredan los hijos
print(c.compilar())         # propio del hijo
    

# Poliformismo 
class Language:
    def __init__(self,name):
        self.name = name

    def creator(self):
        raise NotImplementedError ("Error")
    
class JavaScript(Language):
    def creator(self):
        return f'JavaScript fue creado por {self.name}'   
class Python(Language):
    def creator(self):
        return f'Python fue creado por {self.name}'
class Ruby (Language):
    def creator(self):
        return  f'Ruby fue creado por {self.name}'
class Java(Language):
    def creator(self):
         return f'Java fue creado por {self.name}'
    
names =[
    JavaScript(" Brendan Eich"),
    Python("Guido van Rossum"),
    Ruby("Yukihiro Matsumoto"), 
    Java("James Gosling")
]

for name in names:
    print(name.creator())

#poliformismo sin herencia

    
class JavaScript:
    def __init__(self,year):
        self.year = year

    def creator_year(self):
        return f'JavaScript fue creado en {self.year}'   
class Python:
    def __init__(self,year):
        self.year = year
    
    def creator_year(self):
        return f'Python fue creado por {self.year}'
class Ruby:
    def __init__(self,year):
        self.year = year

    def creator_year(self):
        return  f'Ruby fue creado por {self.year}'
class Java:
    def __init__(self,year):
        self.year = year

    def creator_year(self):
         return f'Java fue creado por {self.year}'
    

javaScript = JavaScript(1995)
python = Python(1991)
ruby = Ruby(1993) 
java =Java(1995)

def year_render(year_objet):
    print(year_objet.creator_year())

year_render(javaScript)
year_render(python)
year_render(ruby)
year_render(java)

