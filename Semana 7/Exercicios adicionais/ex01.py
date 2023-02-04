def primo(n):
    fator = 2
    while(n % fator != 0) and (fator <= n/2):
        fator += 1
    if (n % fator != 0) or (n == 2):
        return True
    else:
        return False

def n_primos(n):
    i = 2
    contador = 0
    fator = 2
    while(i <= n):
        if(primo(i)):
            contador += 1
        i += 1
    return  contador

print(n_primos(int(input('Numero: '))))