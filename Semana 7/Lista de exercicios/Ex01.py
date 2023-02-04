#Recebe altura e largura
# print #largura
# print #altura

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

c = 0
d = 0
while c != altura:
    while d != largura:
        print ('#', end='')
        d += 1
    print ()
    d = 0
    c += 1
         