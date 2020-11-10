# Clase 15 - Repaso

X = 'X'
O = 'O'

# Matrices

def imprimir_matriz(matriz):
    print()
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print()

# Crear una matriz
matriz = [[0,0,0],[0,0,0],[0,0,0]]

imprimir_matriz(matriz)

matriz[0][0] = X
matriz[1][0] = X
matriz[2][0] = X

# guardar un dato en una matriz
for fila in range(0,3):
    for col in range(0,3):
        if fila == col:
            #matriz[fila][col] = X
            pass

imprimir_matriz(matriz)

#leer un dato de una matriz
for fila in range(0,len(matriz)):
    for col in range(0, len(matriz[0])):
        if fila == col:
            print(matriz[fila][col])

print()
valor = matriz[1][1]
print(valor)

for fila in range(0, len(matriz)):
    if matriz[fila][0] == matriz[fila][1] and matriz[fila][0] == matriz[fila][2] and matriz[fila][0] != 0:
        print("Gano!!: " + matriz[fila][0])

for col in range(0, len(matriz[0])):
    if matriz[0][col] == matriz[1][col] and matriz[0][col] == matriz[2][col] and matriz[0][col] != 0:
        print("Gano!!: "+ matriz[0][col])


    