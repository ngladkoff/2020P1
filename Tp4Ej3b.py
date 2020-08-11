def obtener_clave_1(clave_maestra):
    return obtener_clave(clave_maestra, True)

def obtener_clave_2(clave_maestra):
    return obtener_clave(clave_maestra, False)

def obtener_clave(clave, buscar_impares):
    clv = ""
    
    for i in range(0, len(clave)):
        """
        if buscar_impares:
            if i + 1 % 2 != 0:
                clv += clave[i]
            else:
                pass
        else:
            if i + 1 % 2 == 0:
                clv += clave[i]
            else:
                pass
        """
        
        if buscar_impares and (i + 1) % 2 != 0:
            clv = clv + clave[i]
        
        if buscar_impares == False and (i + 1) % 2 == 0:
            clv = clv + clave[i]
    
    return clv
    

def main():
    clave_maestra = input("Ingrese clave maestra: ")
    clave1 = obtener_clave_1(clave_maestra)
    clave2 = obtener_clave_2(clave_maestra)
    print("Clave 1:", clave1)
    print("Clave 2:", clave2)
    
if __name__ == "__main__":
    main()