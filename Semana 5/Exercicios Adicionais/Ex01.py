#Escreva uma função Fizzbuzz
#Recebe um int
#Se for divisivel por 3 e não por 5
#return "Fizz"
#Se for divisivel por 5 e nao por 3
#return "Buzz"
#Se for divisivel por 3 e 5
#return "FizzBuzz"
#Se nao for divisivel nem por 3 nem por 5
#return n

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    elif n % 5 == 0 and n % 3 != 0:
        return 'Buzz'
    elif n % 5 == 0 and n % 3 == 0 :
        return 'FizzBuzz'
    else :
        return n
    
print (fizzbuzz(3))
print (fizzbuzz(5))
print (fizzbuzz(15))
print (fizzbuzz(4))