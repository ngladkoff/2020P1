# Primer Parcial
import random

class ValMinMaxError(Exception):
    pass

def validar_valor(valor, valmin, valmax):
    if valor < valmin:
        raise ValMinMaxError
    if valor > valmax:
        raise ValMinMaxError
    

def ingresar_numero(mensaje, valmin, valmax, msgerror):
    while True:
        try:
            valor = int(input(mensaje))
            validar_valor(valor,valmin,valmax)
            """
            if valor < valmin:
                raise ValMinMaxError
            if valor > valmax:
                raise ValMinMaxError
            """
            return valor
        except ValueError:
            print("Debe ingresar un número")
        except ValMinMaxError:
            print(msgerror)


def menu():
    print("=" * 10)
    print("Menu")
    print("0-Salir")
    print("1-Cargar Solicitud")
    print("2-Asignar Técnicos")
    print("3-Listado")
    print("=" * 10)
    op = ingresar_numero("Ingrese opción: ", 0, 3, "Ingrese un número entre 0 y 3")
    return op
    

def main():
    clientes = []
    zonas = []
    tecnicos = []
    
    inicializar_solicitudes(clientes, zonas, tecnicos)
    
    while True:
        
        op= menu()
        if op == 1:
            cargar_solicitud(clientes,zonas,tecnicos)
        elif op == 2:
            asignar_tecnicos(clientes,zonas,tecnicos)
        elif op == 3:
            imprimir_solicitudes(clientes, zonas, tecnicos)
        elif op == 0:
            print("Chau")
            return
        else:
            print("Opción inválida")
    

def inicializar_solicitudes(clientes, zonas, tecnicos):
    for i in range(0,20):
        clientes.append("Cliente " + str(i))
        zonas.append(random.randint(1,4))
        tecnicos.append(0)

    clientes.append(clientes[5])
    zonas.append(zonas[5])
    tecnicos.append(0)

    clientes.append(clientes[7])
    zonas.append(zonas[7])
    tecnicos.append(0)


def cargar_solicitud(clientes,zonas,tecnicos):
    nombre = input("Ingrese nombre cliente: ")
    print("Zonas: 1-Pinamar, 2-Ostende, 3-Valeria, 4-Cariló")
    zona = ingresar_numero("Ingrese zona [1-4]: ", 1, 4, "Debe ingresar un número de 1 a 4")
    clientes.append(nombre)
    zonas.append(zona)
    tecnicos.append(0)
    
    
def imprimir_solicitudes(clientes, zonas, tecnicos):
    print()
    print("=" * 43)
    print("  # | Cliente              | Zona | Tecnico")
    for i in range(0, len(clientes)):
        print(" {0:02d} | {1:<20} |   {2:1d}  | {3:02d}".format(i+1, clientes[i], zonas[i], tecnicos[i]))
    print("=" * 43)
    print()


def asignar_tecnicos(clientes,zonas,tecnicos):
    
    for i in range(0, len(clientes)):
        
        if tecnicos[i] != 0:
            continue
        
        tecnico = buscar_tecnico(i, clientes, zonas, tecnicos)
        
        if tecnico == 0:
            print("No se pudo encontrar técnico para la solicitud " + str(i + 1))
        else:
            tecnicos[i] = tecnico


def buscar_tecnico(i, clientes, zonas, tecnicos):
    
    tecnico = buscar_tecnico_otra_solicitud_mismo_cliente(i, clientes, tecnicos)
    if tecnico != 0 and tecnico_tiene_disponibilidad(tecnico, tecnicos):
        return tecnico
    
    for t in range(1,11):
        if not tecnico_tiene_disponibiblidad(t, tecnicos):
            continue
        
        zona_tecnico = buscar_zona_tecnico(t,tecnicos, zonas)
        
        if zona_tecnico == 0 or zona_tecnico == zonas[i]:
            return t

    return 0


def buscar_tecnico_otra_solicitud_mismo_cliente(i, clientes, tecnicos):
    cliente = clientes[i]
    
    for f in range(0,len(clientes)):
        if clientes[f] == cliente and tecnicos[f] != 0:
            return tecnicos[f]
    
    return 0


def tecnico_tiene_disponibilidad(tecnico, tecnicos):
    contador = 0
    for f in range(0, len(tecnicos)):
        if tecnicos[f] == tecnico:
            contador += 1
    
    if contador < 4:
        return True
    else:
        return False


def buscar_zona_tecnico(tecnico,tecnicos, zonas):
    for i in range(0,len(tecnicos)):
        if tecnicos[i] == tecnico:
            return zonas[i]
    return 0
    

if __name__ == '__main__':
    main()