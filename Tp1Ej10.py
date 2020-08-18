#TP1Ej10

def dia_de_la_semana(dia,mes,anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

def calcular_dias_mes(mes,anio):
    meses_31_dias = [1,3,5,7,8,10,12]
    
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28

    if mes in meses_31_dias:
        return 31
    else:
        return 30

def imprimir_semana(semana):
    #for i in range(0, len(semana))
    for dia in semana:
        print("{0:>3} |".format(dia), end='')
    print()
    # DRY -> Do not Repeat Yourself (No te repitas)

def imprimir_mes(mes,anio):
    primer_dia = dia_de_la_semana(1,mes,anio)
    cantidad_dias_mes = calcular_dias_mes(mes,anio)
    
    semana_dias = ['do', 'lu', 'ma', 'mi', 'ju', 'vi', 'sa']
    
    semana_dias2 = ["<" + item + ">" for item in semana_dias]
    print(semana_dias2)
    
    semana_num  = [''] * 7
    
    print ('===================================')
    imprimir_semana(semana_dias)

    dia_mes = 1
    indice_dia_semana = primer_dia
    while dia_mes <= cantidad_dias_mes:
        semana_num[indice_dia_semana] = dia_mes
        indice_dia_semana = indice_dia_semana + 1
        
        if indice_dia_semana > 6 or dia_mes == cantidad_dias_mes:
            imprimir_semana(semana_num)

            indice_dia_semana = 0
            semana_num  = [''] * 7
    
        dia_mes = dia_mes + 1
    
    print ('===================================')
        
        



def main():
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))    
    imprimir_mes(mes,anio)
    
    
    
    
if __name__ == '__main__':
    main()
