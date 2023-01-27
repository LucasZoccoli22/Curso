#calcular bhaskara
#Se nao tiver raiz, imprima "esta equação não possui raízes reais"
#As raízes devem ser listadas em ordem crescente
from math import sqrt

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c


if delta == 0:
    
    raiz1 = (-b + sqrt(delta))/ (2 * a)
    print(f'a raiz desta equação é {raiz1:.1f}')
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raiz1 = (-b + sqrt(delta))/ (2 * a)
        raiz2 = (-b - sqrt(delta))/ (2 * a)
        if raiz1 < raiz2:
            print (f'A primeira raiz é {raiz1:.1f}')
            print (f'A segunda raiz é {raiz2:.1f}')
        else:
            print (f'A primeira raiz é {raiz2:.1f}')
            print (f'A segunda raiz é {raiz1:.1f}')