from dataclasses import dataclass

@dataclass
class Alumno:
    nombre: str
    apellido: str
    edad: int


# tuplas
lista = [9,8,7]
tupla1 = (1,2,3)
tupla2 = 1, 2, 3
print(tupla1[2])
# tupla1.append(4) -> error

def mi_funcion():
    return (2,3,4,5)

a = mi_funcion()
print(a)

a,b,c,d = mi_funcion()

print(a)
print(c)

print(tupla1[-2:])

tupla3 = tuple(lista)

print(tupla3)

tupla4 = tupla1, 4, 5, 6
print(tupla4)

TuplaDiasSemana = ("Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do")

for i in range(0, len(TuplaDiasSemana)):
    print(TuplaDiasSemana[i])


capitales = {
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Argentina': 'Buenos Aires'
}

print('La capital de Chile es: ', capitales['Chile'])

alumnos = {
    'LU123': Alumno('Juan', 'Perez', 30),
    'LU124': Alumno('John', 'Doe', 24)
}

alumnos['LU124'] = Alumno('NO', 'Name', 99)

print(alumnos['LU124'])

alumnos['LU125'] = Alumno('Jane', 'Doe', 26)

print(alumnos['LU125'])

del alumnos['LU124']

for key in alumnos.keys():
    print(key)
    print(alumnos[key])

for val in alumnos.values():
    print(val)

for key,value in alumnos.items():
    print(key)
    print(value)
