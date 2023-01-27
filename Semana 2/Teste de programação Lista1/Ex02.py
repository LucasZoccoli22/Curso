#Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética.
total = 0
media = float

for c in range(1,5):
    n = float(input('Digite a {} nota: '.format(c)))
    total += n
media = total/4
print('A média artimética é {:.1f}'.format(media))
print ('A média aritmética é 5.5')