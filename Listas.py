# Listas

def buscar_nombre(nombre_a_buscar, nombres):
    for i in range(len(nombres)):
        if nombres[i] == nombre_a_buscar:
            return i
    return -1

def remover_nombre(nombre_a_buscar, nombres):
    indice_a_remover = buscar_nombre(nombre_a_buscar, nombres)
    if indice_a_remover != -1:
        nombres.pop(indice_a_remover)

def imprimir_nombres(nombres):
    for i in range(len(nombres)):
        print(nombres[i])
    print("-------------")
    
nombres = ["Nicolas","Alejandro","Eduardo"]
print(nombres[1])
nombres[1]= "Carlos"

print("-------------")

"""
for i in range(3):
    print(nombres[i])
    # nombres[i]= input("Ingrese nombre: ")
"""
"""
for nombre in nombres:
    print(nombre)
    # nombres[i]= input("Ingrese nombre: ")
"""    

imprimir_nombres(nombres)
print("-------------")

nombres.append("Alberto")
nombres.append("Mario")
nombres.insert(1, "Maria")

imprimir_nombres(nombres)
print("-------------")

nombre1 = nombres.pop()
print(nombre1)

print("-------------")

imprimir_nombres(nombres)

nombre1 = nombres.pop()
print(nombre1)

print("-------------")

imprimir_nombres(nombres)

nombre1= nombres.pop(0)
print(nombre1)

print("-------------")

imprimir_nombres(nombres)

nombre1= nombres.pop(0)
print(nombre1)

print("-------------")

imprimir_nombres(nombres)

# remover_nombre("Carlos", nombres)
nombres.remove("Carlos")

imprimir_nombres(nombres)

