# Pide una palabra y cuenta cuántas vocales y consonantes tiene usando for. paralelepipedo -> 14, 7 vocales y 7 consonantes

palabra = input('Ingrese una palabra: ')

contador_vocales = 0
contador_consonantes = 0

for caracter in palabra: # hola mundo
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contador_vocales += 1
    elif caracter != ' ':
        contador_consonantes += 1

print(f'En la palabra {palabra} hay {contador_consonantes} consonantes y {contador_vocales} vocales')