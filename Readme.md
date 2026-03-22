# Python

## Cómo empezar 
1. Clonar repo  
2. Instalar dependencias:  
   pipenv install  
3. Activar entorno:  
   pipenv shell  
4. Ejecutar:  
   python main.py  

---

## ● Pipenv
Pipenv es una herramienta de python que combina gestion de dependencias y entonornos virtuales su objetivo es organizar y aislar las librerias de cada proyecto.
Pipenv crea un proyecto en un entorno aislado(virtual environment) donde cada proyecto tiene sus propias liberias, no hay confictos entre versiones y todo queda organizado en un archivo (Pipfile)

✅ Ventajas

✔ Aislamiento de dependencias  
✔ Evita conflictos entre proyectos  
✔ Control de versiones automático  
✔ Fácil de usar  
✔ Integra pip + virtualenv  
✔ Mejora la reproducibilidad del proyecto

❌ Desventajas

❌ Puede ser más lento que pip  
❌ A veces da problemas en Windows  
❌ Menos usado que alternativas modernas (como Poetry)  
❌ Puede ser confuso al principio

#### 1. Requisitos previos

   Antes de empezar necesitas:
   python --version
   pip --version

   Si no funcionan, instala Python desde https://www.python.org

#### 2. Instalar Pipenv

   En PowerShell o CMD:
   pip install pipenv
   Esto instala Pipenv globalmente

#### 3. Crear un proyecto

    mkdir python-env
    cd python-env

#### 4. Crear entorno virtual

   pipenv --python 3
   Esto crea un entorno virtual, seleciona la version de python y genera un archivo Pipfile.

#### 5. Estructura del proyecto

   Después la estructura del proyecto se vera asi:

    python-env/
    │
    ├── Pipfile
    ├── Pipfile.lock
    

#### 6. ¿Qué es el Pipfile?

   Ejemplo:
   ```
   [[source]]        
   url = "https://pypi.org/simple"

   [packages]

   [dev-packages]

   [requires]
   python_version = "3.x"
   ```

  `source` → de dónde descarga librerías (PyPI = “Cheese Shop”)  
  `packages` → dependencias del proyecto  
  `dev-packages` → solo para desarrollo  
  `python_version` → versión usada

#### 7. Instalar librerías

   En lugar de pip install, usa:

    pipenv install numpy
    pipenv install requests

   De esta manera se instala la libreria, se añada al pipfile y se guarda las versiones en Pipfile.lock

#### 8. ¿Qué es Pipfile.lock?

   Es un archivo automático con:

   Versiones exactas
   Dependencias internas
   Seguridad (hashes)

   Ejemplo:
   ```bash
   "numpy": {
    "version": "==1.24.0"
   }
   ```
   Esto evita que tu proyecto se rompa en el futuro


   #### Diferencia Pip vs Pipenv


    | Característica       | pip    | pipenv     |
    | -------------------- | ------ | ---------- |
    | Instalación          | Global | Aislada    |
    | Control de versiones | Manual | Automático |
    | Entorno virtual      | No     | Sí         |
    | Seguridad            | Baja   | Alta       |

## ● Clases
Las clases es una estructura que permite definir un tipo de objeto agrpando datos o caracteristicas(atributos) y comportamientos(funciones o acciones) que un objeto especifico tendrá.

La clases son basicamente plantillas o moldes para crear objetos, la convencion del nombre de la clase es CamelCase.

Un objeto(intancia )es un ejemplar concreto creado a partir de una clase. Por ejemplo una clase puede se un coche, un objeto(instancia) tu coche real.

Las clases se usan pra organizar codido en estructuras logicas, respresentan entidades del mundo real,  reutilizan el codigo y aplican programcion orientada a objetos.

Las clases permiten organizar el código de manera más modular y lógica, facilitando la creación de programs complejos mediante herencia y encapsulamiento.

Dentro de la clase se pueden crear metodos, todo metodo de instancia necesita self como primer parametro, self representa la instancia especifica del objeto. Esto permite que cada objeto creado pueda usar us propios datos y metodos.

#### Como se construye una clase

Un constructor es un metodo especial de una clase que se ejecuta automaticamente en el  momento quen se crea(instancia) un objeto.
En Python el constructor se define cone el metodo  `__int__`, el doble guion bajo significa que esta reservado jpar un uso especial del lenguaje en esta caso seria para el constructor.
Sintaxi basica:
```
class NombreClase:
    def __init__(self, parametros):
        self.atributo = parametros

    def metodo(self):
        return "algo"

        
```

- `__init__ es un metodo especial (dunder method)
- self referencia al objeto creado
- parametros son los parametros de entrada
- self.atributo es el atributo del objeto.
- metodo es la operacion que se puede realizar con la clase

Uso del constructor, no es obligatorio usar un constructor, si no lo defines python usa uno por defecto, pero ese contructor no inicializa atributos. Y a que el constructor se sirve para inicializar atributos
Ejemplo
```python
class LenguajeProgramacion:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def descripcion(self):
        return f"{self.nombre} es un lenguaje {self.tipo} de {self.nivel}"

    def es_interpretado(self):
        return self.tipo == "Interpretado"


python = LenguajeProgramacion("Python", "Interpretado", "alto nivel")

```


#### Encapsulacion

Este concepto no consiste simplemente en *ocultar* datos, sino en controlar cmo se accede y se modifica el estado interno de un objeto. 
los atributos de una clase no deberían ser modificados de forma arbitraria desde el exterior, ya que esto puede romper la coherencia del objeto o llevarlo a estados inválidos.   
En muchos lenguajes orientados a objetos, este problema se resuelve mediante el uso explicito de metodos getter y setter, es decir en lugar de acceder directamente a un atributo, se utilizan funciones getter y setters, permitiendo controlar la logica de acceso y garantizar la integridad de los datos (encapsulamiento).  
Un **getter** se usa para  obtener(leer) el valor de un atributo de un objeto. Se accede a los datos internos de forma controlada.  
Un **setter** se usa para modificar (escribir) el valor de un atributo. Cambia los datos internos de forma controlada.  
Ejemeplo de getter y setter clasico
```Python
class Lenguaje: 
   def __init__(self, nombre): 
      self.__nombre = nombre 
      return self.__nombre 
      
      def set_nombre(self, valor): 
         if valor != "": 
            self.__nombre = valor 

l = Lenguaje("Python") 
l.set_nombre("Java") 
print(l.get_nombre())
```
Esto funciona pero no es pythonico.

En python este enfoque es poco natural, ya que rompe con la simplicidad y la claridad el lenguaje, aqui en donde aparece el decorador `@property`. Este decorador permite crear un especie de 'puente' entre el exterior y el atributo interno. Desde fuera, parece que estas usando un atributo normas, pero en realidad  por dentro se esta ejecutando una funcion que puede controla lo que ocurre. 
En resumen, `@property` sirve para proteger y controlar los datos internos de una clase sin complicar su uso, manteniendo una sintaxis simple pero añadiendo lógica cuando lo necesitas.
Ejemplo con `@property`: 

```Python
class Lenguaje:
    def __init__(self, nombre): 
      self.__nombre = nombre # atributo privado 
      
   @property
   def nombre(self): # getter 
      return self.__nombre 
   
   @nombre.setter 
   def nombre(self, valor): # setter 
      if valor != "": 
         self.__nombre = valor 
      else: print("Nombre inválido")

l = Lenguaje("Python") 

print(l.nombre) # getter 
l.nombre = "Java" # setter 
l.nombre = "" # controlado
```

#### Atributos privados, publicos y protegidos

Los atributos publicos son lo que son accesibles desdes cualquier sitio. `self.atributo`.
Los atributos protegidos son los que estan protegidos por convención, significa que no deberias tocarlo fuera de la clase, pero si se puede hacer. `self._atributo`.
Los atributos privados python lo transforma  internamente `_clase__atributo`, se dificulta el acceso interno y evita la sobreescritura accidental. 

Ejemplo de atributo privado
```python
class Padre:
    def __init__(self):
        self.__valor = 10

    def mostrar(self):
        print(self.__valor)


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.__valor = 20  # NO sobrescribe realmente

h = Hijo()
h.mostrar()
```
Aunque parece que el valor ha cambiado en realidad no lo ha hecho , ya que python  transforma internamente los nombre:
- En Padre seria:_Padre__valor  
- En Hijo seria: _Hijo__valor  
Es decir son dos atributos distintos aunque se vean igual con el mismo nombre.
Si inspeccionamos el objeto :
```python
print(h.__dict__)

# Resultado sera :

{
    '_Padre__valor': 10,
    '_Hijo__valor': 20
}
```
El doble guion no `(__)`esta pensado para evitar conflictos de nombres entre las clases hijas especialmente cuando se esta creando clases base para frameworks o librerias, ya que no se quiere que una subclase rompa la logica sin querer. 

## Metodos dunder
Los metodos dunder son metodos que comienzan y terminan con dos guiones bajos, por ejemplo `__init__`, `__str__`.  
La palabra `dunder` viene de **d**ouble **under**score. Se utilizan para definir comportamientos especiales de objetos y permiten que las clases interactúen con operadores o funciones integradas en python.

Métodos dunder más utilizados:
1. Inicialización y Gestión de Objetos  
`__init__`(self, ...): Inicializador de la clase (constructor).  
`__new__`(cls, ...): Creador de instancias.  
`__del__`(self): Destructor de objetos.   
 
2. Representación de Cadenas  
`__str__`(self): Representación amigable para el usuario (print(), str()).   
`__repr__`(self): Representación formal para desarrolladores.   

3. Operaciones Aritméticas (Sobrecarga de Operadores)
`__add__`(self, other): Suma (+).  
_`_sub__`(self, other): Resta (-).  
`__mul__`(self, other): Multiplicación (*).  
`__truediv__`(self, other): División (/).   

4. Comparaciones
`__eq__`(self, other): Igualdad (==).  
`__lt__`(self, other): Menor que (<).  
`__le__`(self, other): Menor o igual (<=).  
`__gt__`(self, other): Mayor que (>).  
`__ne__`(self, other): Distinto (!=).   

5. Contenedores y Colecciones
`__len__`(self): Longitud del objeto (len()).  
`__getitem__`(self, key): Obtener elemento (obj[key]).  
`__setitem__`(self, key, value): Asignar elemento (obj[key] = value).  
`__delitem__`(self, key): Eliminar elemento (del obj[key]).  
`__contains__`(self, item): Verificación de pertenencia (in).   

6. Iteración  
`__iter__`(self): Devuelve un iterador.  
`__next__`(self): Devuelve el siguiente elemento de la iteración.   

7. Comportamiento de Funciones y Contexto
`__call__`(self, ...): Permite llamar al objeto como una función (obj()).  
`__enter__`(self) /` __exit__`(self): Usados en contextos de gestión de recursos (with). 

En general, los metodos dunder no se llaman directamente, sino que python los invoca automaticamente en situaciones especiales.

Los metodos dunder permiten que los objetos se comportes como tipos nativos de python, por ejemplo par sumarlos
```python

a+b # Llama a a.___add__(b)
len(objeto)   # llama a objeto.__len__()
print(objeto) # llama a objeto.__str__()

```

Python tiene la filosofía de “todo es objeto”. Para que todas las operaciones estándar funcionen con cualquier tipo de objeto, necesitaba un mecanismo uniforme para que los objetos respondieran a operadores y funciones integradas.

Ejemplo:

- Cuando haces print(obj), Python internamente necesita una forma consistente de convertir cualquier objeto en texto.

- Para eso, llama al método especial` __str__ `del objeto.

- Si no existiera `__str__`, Python no tendría forma de saber cómo representar tu objeto como cadena.

Los métodos dunder son la interfaz estándar que Python usa para operar con todos los objetos, sin importar si son objetos propios o creados por el usuario.

#### El metodo `__str__`

El método` __str__ `sirve para definir la representación de un objeto cuando lo conviertes a texto o lo imprimes.
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


p = Persona("Keira", 30)
print(p)  

```

Si instanciamos un objeto y lo imprimimos en consola  la salida seria algo como esto  
 `<__main__.Persona object at 0x000001AC52C58C20>`

 Si quisiéramos conocer de que objeto se trata no podríamos saberlo con la información que nos ofrece la consola tendriamos que usar el metodo `__str__`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

p = Persona("Keira", 30)
print(p)  # -> Keira, 30 años
print(str(p))
```
Lo que ocurre es que cuando haces `print(p)`, Python internamente llama a `p.__str__()`, lo que devuelve ese método es lo que se muestra en pantalla, si no defines `__str__`, Python muestra algo como `<Persona object at 0x...>`, que no es muy legible.

Cuando haces print(str(p)), no estás delegando la conversión en Python, sino que la realizas tú de forma explícita antes de imprimir. Es decir, primero llamas a `str(p)`, lo que provoca directamente la ejecución del método `p.__str__()`, obteniendo así una cadena de texto. Después, print simplemente se encarga de mostrar ese resultado en pantalla sin necesidad de hacer ninguna conversión adicional. En este caso, tienes un mayor control sobre el proceso, ya que decides cuándo y cómo convertir el objeto a texto antes de utilizarlo o imprimirlo.

#### El metodo `__repr__`
Define la representacion oficial de un objeto como cadena de texto. Su objetivo es que sea preciso, sin ambiguedades  y util para la depuracion, idealmente(aunque no siempre), deberia permitir reconstruir el objeto.

Se usa principalmente en depuracion para ver cuaal es el estado real del objeto y en entornos mas técnicos como la consola o los logs. Muestra una version mas fiel del estado interno del objeto que `__str__`.
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

p = Persona("Ana", 30)

print(str(p))   # usa __str__
print(repr(p))  # usa __repr__
```

