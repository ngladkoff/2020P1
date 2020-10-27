# Simulacro 2do Parcial
CATEGORIAS = ["Star", "Medium", "Basic"]

PRESTACIONES= [100,200,300,400]
PRESTACIONES_IMP= [1000,2000,3000,4000]


class Servicio:
    def __init__(self, afiliado, prestacion):
        self.afiliado= afiliado
        self.prestacion= prestacion
        self.reintegro = 0


def main():
    servicios = leer_servicios()
    procesar_servicios(servicios)
    emitir_liquidacion(servicios)


def leer_servicios():
    servicios = []
    with open('servicios-os.csv', 'r') as a:
        for linea in a:
            # "32000;100\n"
            # "32000;200\n"
            # "32000;300\n"
            servicio = linea[:-1].split(';')
            servicios.append(Servicio(int(servicio[0]), int(servicio[1])))
    return servicios


def procesar_servicios(servicios):
    cantidad_procesados= 0
    total_reintegros= 0
    cant_srv_categorias= [0,0,0]

    for servicio in servicios:
        cantidad_procesados += 1
        reintegro= procesar_servicio(servicio)
        total_reintegros = total_reintegros + reintegro
        categoria_srv = categoria_afiliado(servicio.afiliado)
        cant_srv_categorias[categoria_srv] += 1

    print("Total a recibir de la OS: ", total_reintegros)
    print("Servicios procesados: ", cantidad_procesados)
    for i in range(0,len(CATEGORIAS)):
        print("Cantidad servicios categoría {0}: {1}".format(CATEGORIAS[i], cant_srv_categorias[i]))


def categoria_afiliado(afiliado):
    if afiliado >= 1 and afiliado <= 30000:
        return 0
    if afiliado >= 30001 and afiliado <= 60000:
        return 1
    return 2


def procesar_servicio(servicio):
    importe_prestacion = obtener_importe_prestacion(servicio.prestacion)
    categoria = categoria_afiliado(servicio.afiliado)
    reintegro = calcular_reintegro_os(categoria, servicio.prestacion, importe_prestacion)
    servicio.reintegro = reintegro
    return servicio.reintegro


def calcular_reintegro_os(categoria, prestacion, importe_prestacion):
    if categoria == 0:
        return importe_prestacion

    if categoria == 2:
        return importe_prestacion * 0.20

    if prestacion == 100 or prestacion == 200:
        return importe_prestacion

    return importe_prestacion * 0.60


def obtener_importe_prestacion(prestacion):
    for i in range(0, len(PRESTACIONES)):
        if PRESTACIONES[i] == prestacion:
            return PRESTACIONES_IMP[i]
    return -1


def emitir_liquidacion(servicios):
    with open('servicios-os.txt', 'w', encoding='utf-8') as a:
        for servicio in servicios:
            a.write("{0:05d} | {1:03d} | {2:7.2f}\n".format(servicio.afiliado, servicio.prestacion, servicio.reintegro))


if __name__ == '__main__':
    main()
