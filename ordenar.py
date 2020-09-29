# ordenar

class Item:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    def __repr__(self):
        return str(self.id) + " - " + self.nombre
        
    
def ordenar(lista, campo):
    for j in range(0,len(lista) - 1):
        for i in range(0,len(lista) - 1):
            if getattr(lista[i], campo) > getattr(lista[i + 1], campo):
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux


def main():
    lst = [Item(1,"ZZZ"), Item(5,"CCC"), Item(3, "AAA")]
    print(lst)
    ordenar(lst,"id")
    print(lst)
    ordenar(lst, "nombre")
    print(lst)
    
if __name__ == "__main__":
    main()