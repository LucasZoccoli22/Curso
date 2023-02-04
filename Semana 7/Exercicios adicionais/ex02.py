#Faça uma função soma_hipotenusas que recebe como parâmetro um número inteirio positivo n e deolva s oma de todos os inteiros entre 1 e n
#para ser hipotenusa h² = i² + j²

def cal_hipotenusa(a,b):
    return ((a*a) + (b*b))


def soma_hipotenusas(h):
    c = 1
    soma = 0
    while (c <= h):
        n = (c*c)       
        a = 1
        b = 1
        while (a < h):
            while (b < h):
                if (n == cal_hipotenusa(a, b)):
                    soma = soma + c
                    a = h
                b += 1
            a += 1
            b = a
        c += 1
  
    return soma
    
    
h   = int (input('Digite um número inteiro e positivo: '))

print (soma_hipotenusas(h))