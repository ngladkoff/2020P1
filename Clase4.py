# Clase 4

def bubble_sort(lista_original):
    lista = lista_original.copy()
    max_index = len(lista) - 1
    
    for j in range(0,max_index):
        for i in range(0,max_index):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux

    return lista

vector = [2,9,8,3,7,1]
print(vector)
vector_ordenado = bubble_sort(vector)
print(vector_ordenado)


def busqueda_lineal(vector, valor_a_buscar):
    for i in range(0, len(vector)):
        if valor_a_buscar == vector[i]:
            return i
    return -1
    
def busqueda_binaria(vector, valor):
    izq = 0
    dcha = len(vector) - 1
    while izq <= dcha:
        medio = (izq + dcha) // 2
        if vector[medio] == valor:
            return medio
        elif valor < vector[medio]:
            dcha = medio - 1
        else:
            izq = medio + 1
    return -1    
    

vector2 = [-2,3, 5, 7, 8, 14, 16, 20]
valor_a_buscar = 16

print(busqueda_lineal(vector2, valor_a_buscar))

vector3 = [3 * i for i in range(0,20000000)]
v = 18000000

for i in range(0,10):
    print(busqueda_lineal(vector3, v))
    #print(busqueda_binaria(vector3, v))

print("----------------")

for i in range(0,10):
    #print(busqueda_lineal(vector3, v))
    print(busqueda_binaria(vector3, v))
