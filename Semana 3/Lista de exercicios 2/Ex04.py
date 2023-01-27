#Recebe um número inteiro
#Se for divisivel por 3 e 5, imprima 'FizzBuzz'
#Se não for divisivel por 3 e 5, imprima o número 

n = int(input('Insira um número inteiro: '))

if n % 3 == 0 and n % 5 ==0:
    print ('FizzBuzz')
else:
    print (n)