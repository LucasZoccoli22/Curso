#calcular bhaskara
#Se nao tiver raiz, imprima "esta equação não possui raízes reais"
from math import sqrt

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if delta == 0:
    
    raiz1 = (-b + sqrt(delta))/ (2 * a)
    print(f'A unica raiz é: {raiz1}')
else:
    if delta < 0:
        print('Esta equeção não possui raízes reais')
    else:
        raiz1 = (-b + sqrt(delta))/ (2 * a)
        raiz2 = (-b - sqrt(delta))/ (2 * a)
        print (f'A primeira raiz é {raiz1}')
        print (f'A segunda raiz é {raiz2}')