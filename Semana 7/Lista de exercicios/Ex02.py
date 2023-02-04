#Recebe largura e altura
#Printa só os que estiverem na borda

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

c = 0
d = 0
while c <= altura:
    #print (end='')
    if c == 0 or c == altura:
        while d != largura:
            print ('#', end='')
            d += 1
        print ()
    if c > 1 and c < altura:
        print ('#'+(" " * (largura - 2)) + '#')    
        
    d = 0
    c += 1