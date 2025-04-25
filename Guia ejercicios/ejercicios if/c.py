# Pide una nota del 1 al 7 e indica si es “Insuficiente”, “Suficiente”, “Bueno” o “Excelente”.
# Excelente 6 - 7
# Bueno 6 - 5
# suciente 5 - 4
# insuficionete > 4

nota = float(input('Ingrese una nota: '))

# Diferentes formas de abordar un rango
if nota >= 6:
    print('Excelente')
elif nota >= 5 and nota < 6:
    print('Bueno')
elif 4 <= nota < 5:
    print('Suficiente')
else:
    print('Insuficiente')