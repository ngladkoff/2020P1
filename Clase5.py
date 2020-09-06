# Juntar vector de strings

persona = ["Juan","Perez"]
nombre_completo = " ".join(persona)
print(nombre_completo)


def cargar_vector(vector):
    vector.append("A")
    return vector


def inicializar_vector():
    v = []
    v.append("A")
    return v


def main():
    vector= []
    cargar_vector(vector)
    vector = inicializar_vector()