#TP 6 Ej 1
SINGLE_QUOTE= "'"
DOUBLE_QUOTE= '"'
HASHTAG= '#'
ESCAPE_CHAR= '\\'


# Ejemplos: al inicio
a = 5 # al final
prueba = "dentro de 'un string #hola"
prueba = 'dentro de "otro string #hola'
prueba = "string" # y luego comentario
prueba = "que no se rompa el string \" con la comilla escapeada y un docstring de linea simple\\" """ prueba """

"""
un docstring
multilinea
a borrar
"""

prueba = "otra" ''' un coment al final
pero multilinea
""" ojo q esto no termina el docstring
'''

def main():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión incluida): ")
    lineas_archivo = obtener_lineas_archivo(nombre_archivo)
    lineas_sin_comentarios = obtener_lineas_sin_comentarios(lineas_archivo)
    guardar_copia_archivo(nombre_archivo, lineas_sin_comentarios)


def obtener_lineas_archivo(nombre_archivo):
    lineas = []
    with open(nombre_archivo, 'r') as py:
        for linea in py:
            lineas.append(linea[:-1])
    return lineas


def obtener_lineas_sin_comentarios(lineas_archivo):
    lineas = []
    en_docstring = False
    en_string = False
    string_quote = None
    docsstring_chars= 0
    for linea in lineas_archivo:
        nueva_linea = []
        for i in range(0, len(linea)):
            c = linea[i]

            if docsstring_chars > 0:
                docsstring_chars -=1
                continue

            if en_string and c != string_quote:
                nueva_linea.append(c)
            elif en_string and c == string_quote and linea[i-1] == ESCAPE_CHAR and linea[i-2] != ESCAPE_CHAR:
                nueva_linea.append(c)
            elif en_string and c == string_quote and (linea[i-1] != ESCAPE_CHAR or (linea[i-1] == ESCAPE_CHAR and linea[i-2] == ESCAPE_CHAR)):
                en_string= False
                nueva_linea.append(c)
            elif not en_string and not en_docstring and c == SINGLE_QUOTE:
                if len(linea) > i + 2:
                    if linea[i + 1] == SINGLE_QUOTE and linea[i+2] == SINGLE_QUOTE:
                        en_docstring = True
                        string_quote= SINGLE_QUOTE
                        continue
                en_string= True
                string_quote= SINGLE_QUOTE
                nueva_linea.append(c)
            elif not en_string and not en_docstring and c == DOUBLE_QUOTE:
                if len(linea) > i + 2:
                    if linea[i + 1] == DOUBLE_QUOTE and linea[i+2] == DOUBLE_QUOTE:
                        en_docstring = True
                        string_quote= DOUBLE_QUOTE
                        continue
                en_string= True
                string_quote= DOUBLE_QUOTE
                nueva_linea.append(c)
            elif not en_string and not en_docstring and c == HASHTAG:
                break
            elif en_docstring:
                if len(linea) <= i + 2:
                    continue
                if c != string_quote or linea[i + 1] != string_quote or linea[i+2] != string_quote:
                    continue
                en_docstring = False
                docsstring_chars= 2
            else:
                nueva_linea.append(c)

        if len(nueva_linea) > 0:
            lineas.append("".join(nueva_linea))

    return lineas


def guardar_copia_archivo(nombre_archivo, lineas):
    with open(nombre_archivo[:-3] + '-2.py', 'w', encoding="utf-8") as arch:
        for i in range(0, len(lineas)):
            arch.write(lineas[i]+'\n')

if __name__ == ("__main__"):
    main()