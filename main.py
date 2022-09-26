
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
    while True:
        temp = input('¿Deseas encriptar o desencriptar?\n1.- Encriptar\n2.- Desencriptar ')
        print('')
        if temp.isnumeric():
            temp = int(temp)
            if (temp > 0 and temp < 3):
                break 
            else:
                print('introduce un numero valido')
        else:
            print('¿Deseas encriptar o desencriptar?\n1.- Encriptar\n2.- Desencriptar ')
    
    
    msj = input('¿Cúal es tu mensaje?')


if __name__ == '__main__':
    main()
    