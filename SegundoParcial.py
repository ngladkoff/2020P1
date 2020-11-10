# Segundo Parcial

CANTIDAD_MAQUINAS = 5

class Produccion:
    def __init__(self, maquina, hora, cantidad):
        self.maquina= maquina
        self.hora = hora
        self.cantidad_producida = cantidad
        self.cantidad_defectuosa = 0


class Defecto:
    def __init__(self, maquina, hora, cantidad):
        self.maquina= maquina
        self.hora= hora
        self.cantidad_defectuosa = cantidad


def main():
    producciones = cargar_producciones()
    defectos = cargar_defectos()
    unificar_producciones_defectos(producciones, defectos)
    generar_reporte_fallas_parciales(producciones, '{0} | {1} | {2} | {3} | {4:3.2f}% \n')
    generar_reporte_maquinas_defectuosas(producciones)



def cargar_producciones():
    producciones = []
    primera_vuelta = True
    with open('produccion.csv', 'r') as archivo:
        for linea in archivo:
            if primera_vuelta:
                primera_vuelta= False
                continue
            dato = linea[:-1].split(';')
            producciones.append(Produccion(dato[0], int(dato[1]), int(dato[2])))
    return producciones


def cargar_defectos():
    defectos = []
    primera_vuelta = True
    with open('calidad.csv', 'r') as archivo:
        for linea in archivo:
            if primera_vuelta:
                primera_vuelta= False
                continue
            dato = linea[:-1].split(';')
            defectos.append(Defecto(dato[0], int(dato[1]), int(dato[2])))
    return defectos


def unificar_producciones_defectos(producciones, defectos):
    for defecto in defectos:
        i = buscar_maquina_hora(defecto.maquina, defecto.hora, producciones)
        producciones[i].cantidad_defectuosa = defecto.cantidad_defectuosa


def buscar_maquina_hora(maquina, hora, producciones):
    for i in range(0,len(producciones)):
        if producciones[i].maquina == maquina and producciones[i].hora == hora:
            return i
    return -1


def generar_reporte_fallas_parciales(producciones, formato):
    with open('fparciales.txt', 'w', encoding='utf-8') as archivo:
        for produccion in producciones:
            porc_falla = produccion.cantidad_defectuosa / produccion.cantidad_producida
            if porc_falla > 0.02:
                archivo.write(formato.format(
                                             produccion.maquina,
                                             produccion.hora,
                                             produccion.cantidad_producida,
                                             produccion.cantidad_defectuosa,
                                             porc_falla))


def generar_reporte_maquinas_defectuosas(producciones):
    produccion_maquina = [0,0,0,0,0]
    defectos_maquina = [0] * CANTIDAD_MAQUINAS

    for produccion in producciones:
        i = ord(produccion.maquina) - 65
        produccion_maquina[i] = produccion_maquina[i] + produccion.cantidad_producida
        defectos_maquina[i] += produccion.cantidad_defectuosa

    with open('fmaquinas.txt', 'w', encoding='utf-8') as archivo:
        for i in range(0,CANTIDAD_MAQUINAS):
            porc_falla = defectos_maquina[i] / produccion_maquina[i]
            if porc_falla > 0.01:
                archivo.write('{0} | {1} | {2} | {3:3.2f}% \n'.format(
                            chr(i + 65),
                            produccion_maquina[i],
                            defectos_maquina[i],
                            porc_falla
                ))



if __name__ == "__main__":
    main()
