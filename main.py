
def main():
    print('Menu: \nLos cifrados disponibles son\n1.- Cifrado de Playfair\n2.- Cifrado de Hill\n3.- Libreta de un sólo Uso (OTP).')

    while True:
        typ = input('¿Qué tipo de cifrado deseas? ')
        if typ.isnumeric():
            typ = int(typ)
            if (typ > 0 and typ < 4):
                break 
            else:
                print('introduce un numero valido')
        else:
            print('Introduce el numero del algoritmo')
    msj = input('¿Cúal es tu mensaje?')


if __name__ == '__main__':
    main()
    