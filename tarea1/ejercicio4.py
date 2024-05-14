edad=input('ingrese su edad: ')
sueldo=input('ingrese su sueldo: ')

if (int(edad))>=18: 
    print('mayor de edad')
    if int(sueldo)>1000: 
        if (int(sueldo)>=1000) and (int(sueldo)<=3000):
            print('usted puede acceder a una tarjeta clásica')
        else:
            print('usted puede acceder a una tarjeta dorada')
    else:
        print ('no puede acceder a una tarjeta de crédito')
else:
    print('no puede acceder a una tarjeta de crédito por ser menor de edad')