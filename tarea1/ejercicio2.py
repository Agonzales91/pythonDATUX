
tipoDato= input('ingresa un dato por teclado: ')

try:
    int(tipoDato)
    print(type(int(tipoDato)))
except Exception as e:
    try:
        if(tipoDato=='true' or tipoDato=='false'):
            print(type(bool(tipoDato)))
        else:
            print(type(tipoDato))
    except Exception as f:
        pass