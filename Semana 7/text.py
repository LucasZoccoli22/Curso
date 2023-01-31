#Calcular o fatorial


def funfatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    print (fatorial)


n = int (input('Digite um numero: '))
while n >= 0:
    
    funfatorial(n)
    
    n = int (input('Digite um numero: '))
    
