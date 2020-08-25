# Ambulancias
MAXIMO = 5
VALOR_NULO_VECTORES_NUMERICOS= 0
INDICE_NO_ENCONTRADO = -1


class ErrorValorMinimo(Exception):
    pass

class ErrorValorMaximo(Exception):
    pass

class ErrorDia10(Exception):
    pass

def ValidarNoDia10(ingreso_usuario):
    if ingreso_usuario * 5 == 50:
        raise ErrorDia10

def ingresar_dia():
    while True:
        try:
            ingreso_usuario = ingresar_numero("Ingrese un día: ", 1, 31)
            
            ValidarNoDia10(ingreso_usuario)
            
            return ingreso_usuario            
        except ValueError:
            print("Día inválido")
        except ErrorValorMinimo:
            print("Día mínimo es 1")
            return 1
        except ErrorValorMaximo:
            print("Día máximo es 31")
            return 31
        except ErrorDia10:
            print("ingresó el día 10")

        
def ingresar_numero(mensaje,valmin,valmax):
    ingreso_usuario = int(input(mensaje))
    if ingreso_usuario <= valmin:
        raise ErrorValorMinimo
    elif ingreso_usuario >= valmax:
        raise ErrorValorMaximo
    
def promedio_km_srv(ambulancias,fila):
    return ambulancias[fila][3] / ambulancias[fila][2]

def b_calcular_mayor_promedio_km_dia(ambulancias):
    mayor_fila = 0
    mayor_promedio = promedio_km_srv(ambulancias, 0)
    
    for fila in range(0, len(ambulancias)):
        promedio = promedio_km_srv(ambulancias, fila)
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mayor_fila= fila

    print("Móvil: ", ambulancias[mayor_fila][0])
    print("Día: ", ambulancias[mayor_fila][1])

def d_calcular_mayor_servicios_dia(ambulancias, d_dia):
    mayor_fila = 0
    for fila in range(0, len(ambulancias)):
        if ambulancias[fila][1] == d_dia:
            if ambulancias[fila][2] > ambulancias[mayor_fila][2]:
                mayor_fila= fila
    return mayor_fila
        

def b_calcular_mayor_promedio_km_dia_op2(ambulancias):
    mayor_fila = 0
    
    for fila in range(0, len(ambulancias)):
        promedio = promedio_km_srv(ambulancias, fila)
        mayor = promedio_km_srv(ambulancias, mayor_fila)
        if promedio > mayor:
            mayor_fila= fila

    print("Móvil: ", ambulancias[mayor_fila][0])
    print("Día: ", ambulancias[mayor_fila][1])
            
    
def imprimir_ambulancias(numeros,servicios,kilometros):
    for i in range(0,len(numeros)):
        print(numeros[i], servicios[i], kilometros[i])
    

def buscar_vector(vector, a_buscar):
    for i in range(0,len(vector)):
        if vector[i] == a_buscar:
            return i
    return INDICE_NO_ENCONTRADO    

def a_cargar_vectores_ambulancia(matriz, numeros, servicios, kilometros):
    
    for i in range(0, len(matriz)):
        numero_ambulancia = matriz[i][0]
        
        indice_ambulancia= buscar_vector(numeros, numero_ambulancia)
        if indice_ambulancia == INDICE_NO_ENCONTRADO:
            indice_ambulancia = buscar_vector(numeros, VALOR_NULO_VECTORES_NUMERICOS)
        
        numeros[indice_ambulancia] = numero_ambulancia
        servicios[indice_ambulancia] = servicios[indice_ambulancia] + matriz[i][2]
        kilometros[indice_ambulancia] = kilometros[indice_ambulancia] + matriz[i][3]

    

def main():
    ambulancias = [[1,2,5,9],[2,2,4,8],[3,4,6,5],[1,4,4,9],[1,6,5,8],[2,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]]
    
    ambulancia_numeros = [VALOR_NULO_VECTORES_NUMERICOS] * MAXIMO
    ambulancia_servicios = [VALOR_NULO_VECTORES_NUMERICOS] * MAXIMO
    ambulancia_kilometros = [VALOR_NULO_VECTORES_NUMERICOS] * MAXIMO
    
    a_cargar_vectores_ambulancia(ambulancias, ambulancia_numeros, ambulancia_servicios, ambulancia_kilometros)        

    print("# Sv Km")
    imprimir_ambulancias(ambulancia_numeros,ambulancia_servicios,ambulancia_kilometros)

    b_calcular_mayor_promedio_km_dia(ambulancias)

    d_dia = ingresar_dia()
    fila = d_calcular_mayor_servicios_dia(ambulancias, d_dia)
    print("Móvil: ", ambulancias[fila][0])


if __name__ == '__main__':
    main()
