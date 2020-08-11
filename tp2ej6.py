#TP2Ej6

def existe_en_lista(valor, lista):
    
    for item in lista:
        if item == valor:
            return True
    
    return False


def main():
    lista1= ["palabra1", "palabra2", "palabra3", "palabra4", "palabra4", "palabra5"]
    lista2= ["palabra2", "palabra4"]
    lista3= []
    
    for item in lista1:
        lista3.append(item)
    
    lista1.append("palabra6")
    
    for item in lista2:
        while existe_en_lista(item, lista3):
            lista3.remove(item)
    
    print(lista1)
    print(lista2)
    print(lista3)
    
    
if __name__ == "__main__":
    main()