# Definición de la clase "Persona"
class Persona:
    def __init__(self, nombre, edad, genero, ocupacion):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Método 1: Presentarse
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, soy {self.genero} y trabajo como {self.ocupacion}.")

    # Método 2: Cumplir años (incrementar la edad)
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Felicidades! Ahora tienes {self.edad} años.")

    # Método 3: Cambiar de nombre
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Tu nuevo nombre es {self.nombre}.")

    # Método 4: Mostrar información
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}")

    # Método 5: Saludar a otra persona
    def saludar_a_otra_persona(self, otra_persona):
        print(f"Hola {otra_persona.nombre}, soy {self.nombre}. Mucho gusto")

# Creación de una instancia de la clase Persona
persona1 = Persona("Reyna",19, "Mujer", "Ingeniero")
persona1.presentarse()  # Llamada al método presentarse

# Uso de los otros métodos
persona1.cumplir_anios()  # Llamada al método cumplir años
persona1.cambiar_nombre("Aitana")  # Cambiar el nombre
persona1.mostrar_informacion()  # Mostrar información

# Creación de otra instancia y saludo entre dos personas
persona2 = Persona("Obdulia", 25, "femenino", "Enfermera")
persona1.saludar_a_otra_persona(persona2)

persona3 = Persona("Johana", 19, "Femenino", "Ingeniera")
persona4 = Persona("Alejandro", 19, "Masculino", "Doctor")
persona5 = Persona("Ashley",19, "Femenino", "Administradora")

persona3.saludar_a_otra_persona(persona4)