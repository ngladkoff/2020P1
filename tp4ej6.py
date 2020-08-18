#TP4Ej6
texto = "El número de teléfono es 4356-7890"
print(texto[25:25+9])

telefono = ""
for i in range(0, len(texto)):
    if i >= 25 and i <= (25+9):
        telefono = telefono + texto[i]
    
print(telefono)

