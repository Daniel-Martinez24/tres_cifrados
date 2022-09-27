# codigo Hill
dict_encoder = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
            '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}

dict_desencoder = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
            '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
            '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}

def hill_encoder(msj: str) -> str:
    pass

def hill_desencoder(msj: str) -> str:
    pass

def hill_menu(option: int, msj: str) -> str:
    return hill_encoder(msj) if option == 1 else hill_desencoder(msj)

# Código main
def main() -> None:
    print('Menu: \nLos cifrados disponibles son\n1.- Cifrado de Playfair\n2.- Cifrado de Hill\n3.- Libreta de un sólo Uso (OTP).')
    typ, temp = '', ''
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

    if (typ == 2):
        hill_menu(option=temp, msj=msj)

if __name__ == '__main__':
    main()
    