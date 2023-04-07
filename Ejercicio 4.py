# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

contador = 100

while contador <= 100:
    print(contador)
    contador -=1
    if contador == 0:
        break    
print('Fin del ejercicio')