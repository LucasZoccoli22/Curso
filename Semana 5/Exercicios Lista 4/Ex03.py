#Função que recebe uma letra
#Diga TRUE se for vogal
#FALSE se for consoante

def vogal (x):
   if x.lower() in 'aeiou':
       return True
   else:
       return False
    
print (vogal("a"))
print (vogal("b"))
print (vogal('E'))