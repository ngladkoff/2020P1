# Clase 7 - Registros

class Servicio:
    def __init__(self, p_nombre, p_costo):
        self.nombre = p_nombre
        self.costo = p_costo
    def __repr__(self):
        return "{0}: ${1:6.2f}".format(self.nombre, self.costo)

legal = Servicio("Asesoria Legal", 2000.00)
print(legal.nombre)
legal.costo = 1800.00
print(legal.costo)
contable = Servicio("Asesoria Contable", 1500.00)
print(contable.nombre)
print(contable)


class Persona:
    def __init__(self, nombre, telefono, edad, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        self.direccion = direccion
    def __repr__(self):
        return self.nombre + " | " + self.direccion.calle

class Direccion:
    def __init__(self, calle, altura, localidad):
        self.calle = calle
        self.altura = altura
        self.localidad = localidad

localidades = ["Madariaga", "Valeria", "Pinamar"]

direccion1 = Direccion("Libertador", 1234, 2)

persona1 = Persona("Carlos", "1112345678", 20, direccion1)

print(persona1.direccion.calle)
print(localidades[persona1.direccion.localidad])


personas = []

for i in range(0,5):
    personas.append(
        Persona("P" + str(i), 
                "1234", 
                20, 
                Direccion("Calle" + str(i), 1234, 1)
        )
    )

print(personas)
