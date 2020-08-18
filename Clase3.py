#Clase 3
# Matrices

def imprimir_matriz(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            print("{0:>2}".format(matriz[f][c]), end='|')
        print()


fila1 = [1,2,3]
fila2 = [2,6,12]
matriz2 = [fila1, fila2]
matriz2.append([0,1,2])

print(matriz2)

matriz = [[1,2,3],[2,6,12],[0,1,2],[8,5,3]]
# print(matriz)

imprimir_matriz(matriz)

"""
for f in range(0,4):
    for c in range(0,3):
        print("{0:>2}".format(matriz[f][c]), end='|')
    print()
"""

matriz[2][2]= 7
print(matriz[2][2])

filas = 4
columnas = 3

matriz3 = [[0] * columnas for i in range(filas)]
imprimir_matriz(matriz3)