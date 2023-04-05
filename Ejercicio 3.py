#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable 
# imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. 

inicio = str(input ('¿Quieres conocer tu IMC?'))
if inicio == 'si':
    peso = float(input('¿Cual es tu peso?'))
    altura = float(input ('¿Tu altura?'))
    IMC = peso / (altura**2)
    print('Tu IMC es:', IMC)
print('Que tengas un buen día!')




