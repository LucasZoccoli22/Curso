#Converter segundos em
#Dias
#Horas
#Minutos
#Segundos

n = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = n//86400 #178615 = 2
segr = n % 86400 #178615 = 
print (segr)
horas = segr // 3600
segr = segr % 3600
minutos = segr // 60
segr = segr % 60
print ('{} dias, {} horas, {} minutos e {} segundos'.format(dias,horas,minutos,segr))