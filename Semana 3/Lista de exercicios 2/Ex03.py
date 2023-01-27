#Recebe um número inteiro
#Se for divisivel por 5, imprima 'Buzz'
#Se não for divisivel por 5, imprima o número 

n = int(input('Insira um número inteiro: '))

if n % 5 == 0:
    print ('Buzz')
else:
    print (n)