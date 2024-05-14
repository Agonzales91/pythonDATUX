
def sumar():
    total = 0
    n1 = input('Ingresa un número: ')

    for a in range(1,int(n1)+1):
        #total = total + a
        total += a

    print(total)           

def main ():
    sumar()

if __name__ == '__main__':
    main()