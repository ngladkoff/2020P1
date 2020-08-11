#tp2Ej2c

def existe_en_lista(valor, lista):
    
    for item in lista:
        if item == valor:
            return True
    
    return False

def elementos_unicos(lista):
    
    respuesta= []
    
    for item in lista:
        if not existe_en_lista(item, respuesta):
            respuesta.append(item)
    
    return respuesta

lst= [1,2,3,3,4,5,5,6]
lst2= elementos_unicos(lst)
print(lst2)