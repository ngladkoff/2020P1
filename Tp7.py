#TP7

#EJ1
def cant_digitos(nro):
    if nro < 10:
        return 1
    return 1 + cant_digitos(nro // 10)

#print(cant_digitos(123456))
#print(cant_digitos(1234))
#print(cant_digitos(1))
#print(cant_digitos(123456789))

#EJ2
def convertir_binario(binario):
    if binario == "":
        return 0
    else:
        return (int(binario[0]) * (2 ** (len(binario) - 1))) + convertir_binario(binario[1:])

print(convertir_binario("11001011"))
print(convertir_binario(""))
