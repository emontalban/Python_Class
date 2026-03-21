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

## -Clases
Las clases es una estructura que permite definir un tipo de objeto agrpando datos o caracteristicas(atributos) y comportamientos(funciones o acciones) que un objeto especifico tendrá.

La clases son basicamente plantillas o moldes para crear objetos, la convencion del nombre de la clase es CamelCase.

Un objeto(intancia )es un ejemplar concreto creado a partir de una clase. Por ejemplo una clase puede se un coche, un objeto(instancia) tu coche real.

Las clases se usan pra organizar codido en estructuras logicas, respresentan entidades del mundo real,  reutilizan el codigo y aplican programcion orientada a objetos.

Las clases permiten organizar el código de manera más modular y lógica, facilitando la creación de programs complejos mediante herencia y encapsulamiento.

Dentro de la clase se pueden crear metodos, todo metodo de instancia necesita self como primer parametro, self representa la instancia especifica del objeto. Esto permite que cada objeto creado pueda usar us propios datos y metodos.

#### Como se construye una clase

Un constructor es un metodo especial de una clase que se ejecuta automaticamente en el  momento quen se crea(instancia) un objeto.
En Python el constructor se define cone el metodo  `__int__`
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
- parametros son los parametor de entrada
- self.atributo es el atributo del objeto.

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
```