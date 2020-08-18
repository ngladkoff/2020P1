#Tp5Ej1

class MenorMinimoError(Exception):
    pass


class MayorMaximoError(Exception):
    pass

def validar_numero(texto_numero, nro_min, nro_max):
    numero = int(texto_numero)
    if numero <= nro_min:
        raise MenorMinimoError()
    if numero >= nro_max:
        raise MayorMaximoError()
    return numero

def ingresar_numero(mensaje, nro_min, nro_max, mensaje_min, mensaje_max):
    
    while True:
        try:
            return validar_numero(input(mensaje), nro_min, nro_max)
        
        except ValueError:
            print("Debe ingresar un número entero")
        
        except MenorMinimoError:
            print(mensaje_min)
    
        except MayorMaximoError:
            print(mensaje_max)
    
    
def main():
    edad = ingresar_numero("Ingrese su edad: ", -1, 150, "La edad no puede ser negativa", "Imposible que tengas esa edad")    
    print("Edad: ", edad)
    nota = ingresar_numero("Ingrese la nota: ", 0, 11, "La nota no puede ser menor a 1", "La nota no puede ser mayor a 10")


if __name__ == '__main__':
    main()