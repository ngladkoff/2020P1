# Cadenas de Caracteres

a = "Hola "
b = "Mundo"
print(a + b)

c = "=" * 10
print(c)

d= "20"
e= int(d)
print(e)
print(type(e))

f= "15.5"
g= float(f)
print(g)
print(type(g))

a = int("5")
b = int("10")
print (a + b)

h= 1300
i= str(1300)
print(i)
print(type(i))

a = ["a","b","c","d"]

for i in range(0,len(a)):
    a[i] = chr(ord(a[i]) - 32)
    
print(a)

a = "Hola Mundo".lower()
print(a)
print(a.upper())
print(a.title())

print("Facultad".replace("a", "@"))

print("Hola Mundo".replace("Mundo", "UADE"))

texto = "Nicolas<#>Gladkoff<#>ngladkoff@uade.edu.ar"
text2 = "Juan|Perez|jperez@uade.edu.ar"
parrafo = "Un texto es una composición \\a de signos codificados \r\n en un \"sistema\" de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original"
persona = texto.split("<#>")
persona2 = text2.split("|")
palabras = parrafo.replace(",","").replace(".", "").split(" ")
print(persona)
print(persona2)
print(parrafo)
print(palabras)
texto3 = "|".join(persona)
print(texto3)

print("Hola ", end="")
print("Mundo")

z= 5
print("{3} - {0}, {1}: {2}".format(persona[1], persona[0], persona[2], z))
print(str(z) + " - " + persona[1] + ", " + persona[0] + ": " + persona[2])
print()

a = "{0:>6} | {1:<15} | {2:^10} | {3}".format("Legajo", "Nombre", "DNI", "Promedio")
b = "{0:>6} | {1:15} | {2:010d} | {3:8.3f}".format(4123,"Juan Perez", 12123123, 1.5)
c = "{0:>6} | {1:15} | {2:010d} | {3:8.3f}".format(4123,"Juan Perez", 12123123, 12.5)
d = "{0:>6} | {1:15} | {2:010d} | {3:8.3f}".format(4123,"Juan Perez", 12123123, 123.5)
print(a)
print(b)
print(c)
print(d)
print()

a = "Hola Mundo"
print(a[0])
print()

for i in range(0, len(a)):
    print(a[i])
    
vocales = ["a", "e", "i", "o", "u"]

contador = 0
for i in range(0,len(a)):
    if a[i] in vocales:
        contador += 1

print("Cantidad de Vocales: ",contador)

print(a[5:8])
print(a[5:])
print(a[:4])
print(a[:-4])
print(a[-4:])

print(a[-2])

# 5/0

try:
    5/0
except:
    print("Hubo un error")
    
# input("Presione Enter para continuar")

class DatoInvalido(Exception):
    pass

def dividir(x,y):
    try:
        #c = int("a")
        result = x/y
        raise DatoInvalido()
    except ZeroDivisionError:
        print("división por cero!!")
    except ValueError:
        print("error de conversion")
    except DatoInvalido:
        print("dato invalido")
    except:
        print("Error desconocido")
    else:
        print("El resultado es:", result)
    finally:
        print("esto se ejecuta siempre")

a1= int(input("Numerador: "))
a2= int(input("Denominador: "))
dividir(a1,a2)
        
bandera = True        
        
while bandera:
    try:
        x = int(input("Ingrese un número: "))
    except:
        print("Ingrese un número válido")
    else:
        #bandera = False
        break
    
print(x)


















