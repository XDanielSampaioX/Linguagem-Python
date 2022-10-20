lista = [1,2,3,4,5,6,7,8,9999]
valor= 9999
resultado= False

# resultado= 7 in lista

for i in range (len(lista)):
    if lista[i]== valor:
        resultado= True

print(resultado)