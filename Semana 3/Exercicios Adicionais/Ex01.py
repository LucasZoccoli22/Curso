#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#longe
#se for menor que 10, perto
from math import sqrt

x1 = int(input('Digite o primeiro número: '))
y1 = int(input('Digite o segundo número: '))
x2 = int(input('Digite o terceiro número: '))
y2 = int(input('Digite o quarto número: '))

a = (x1 - x1)**2
b = (y1-y2)**2
d = sqrt(a+b)

if d >= 10:
    print('longe')
else:
    print('perto')

