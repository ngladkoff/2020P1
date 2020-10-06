class Departamento:
    def __init__(self, numero, descripcion, m2, estado, precio):
        self.numero = numero
        self.descripcion= descripcion
        self.m2= m2
        self.estado= estado
        self.precio= precio
    def __repr__(self):
        return "{0},{1},{2},{3},{4}\n".format(self.numero, self.descripcion, self.m2, self.estado, self.precio)
    def __str__(self):
        return str(self.numero) + "\n"

lista = [Departamento(1, "ABC", 100, 0, 100000), Departamento(2,"DEF", 120, 0, 120000)]
for i in range(0, len(lista)):
    print(repr(lista[i]), end='')


