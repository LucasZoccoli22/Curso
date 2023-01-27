
n = int(input('Digite um numero inteiro: '))

uni = n % 10
dezena = ((n - uni)/10)%10

print ('O dígito das dezenas é {:.0f}'.format(dezena))