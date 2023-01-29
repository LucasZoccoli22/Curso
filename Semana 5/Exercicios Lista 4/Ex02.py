#Função maior_primo
#Recebe um número máximo e pega o ultimo número primo < ou ==


def maior_primo(n):
    for num in reversed(range(1,n+1)):
        if all(num%i!=0 for i in range(2,num)):
            return num
print (maior_primo(100))
print (maior_primo(7))