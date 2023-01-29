#recebe 3 numeros inteiros
#Mostra qual o maior

def maximo(x,y,z):
    if x > y and x > z:
        maior = x
    elif y > x and y > z:
        maior = y
    elif z > x and z > y:
        maior = z 
    else :
        maior = x
    return maior



print (maximo (30,14,10))
print (maximo (0,-1,1))
