# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.


año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año', año, 'es bisiesto')
        else:
            print('El año', año, 'no es bisiesto')
    else:
        print('El año', año , 'es bisiesto')
else:
    print('El año', año, 'no es bisiesto')
    