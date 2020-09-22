class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def __repr__(self):
        return "{0}/{1}/{2}".format(self.dia, self.mes, self.anio)
    def __str__(self):
        return "{0:02d}-{1:02d}-{2:4d}".format(self.dia, self.mes, self.anio)

class Persona:
    def __init__(self, nombre, sueldo, fecha_nacimiento):
        self.nombre = nombre
        self.sueldo = sueldo
        self.f_nacimiento = fecha_nacimiento
    def __repr__(self):
        return self.nombre


def ordenar_lista(vector):
    i_max = len(vector) - 1
    for j in range(0,i_max):
        for i in range(0,i_max):
            if vector[i].nombre > vector[i + 1].nombre:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux


def main():
    lista = [Persona("Nicolas", 2000, Fecha(1,1,1980)), Persona("Alejandro", 4000, Fecha(2,2,1981)), Persona("Carlos", 3000, Fecha(3,3,1982))]
    print(lista)
    ordenar_lista(lista)
    print(lista)
    print("{0:03d} | {1:0.2f}".format(5, 4.5))
    persona = lista[0]
    print("Nombre: " + persona.nombre)
    print("Fecha: {0:02d}-{1:02d}-{2:4d}".format(persona.f_nacimiento.dia, persona.f_nacimiento.mes, persona.f_nacimiento.anio))

    print(persona.f_nacimiento)
    print(repr(persona.f_nacimiento))

    dato = Fecha(4,4,2004)
    print(dato)

    persona.f_nacimiento = dato
    print(persona.f_nacimiento)


if __name__ == "__main__":
    main()