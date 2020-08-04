# TP1 - Ej1

def devolver_numero_mayor(nro1, nro2, nro3):
    if nro1 <= 0:
        return -99
    
    if nro2 <= 0:
        return -99
    
    if nro3 <= 0:
        return -99

    if nro1 > nro2:
        if nro1 > nro3:
            return nro1
        
    if nro2 > nro1:
        if nro2 > nro3:
            return nro2

    if nro3 > nro1:
        if nro3 > nro2:
            return nro3
    
    return -1

def main():
    n1 = int(input("Ingrese número 1: "))
    n2 = int(input("Ingrese número 2: "))
    n3 = int(input("Ingrese número 3: "))
    
    numero_mayor= devolver_numero_mayor(n1,n2,n3)
    if numero_mayor == -1:
        print("No se encontró un número mayor")
    elif numero_mayor == -99:
        print("No se admiten números negativos")
    else:
        print("Número mayor: ", numero_mayor)
    print("Chau")
        
if __name__ == '__main__':
    main()
    