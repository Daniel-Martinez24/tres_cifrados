# librerias
import numpy as np
from collections import deque

# codigo Hill
# dict_encoder = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
#           'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
#           '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}
            
dict_encoder = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'Ñ':14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# dict_desencoder = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
#             '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
#             '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}


dict_desencoder = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 
                13: 'N', 14: 'Ñ', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

mat_cif = np.array([[1,2,3], [0,4,5], [1,0,6]])
mat_cif_t = np.array([[6, 24, 22] , [26, 21, 1], [17, 5, 10]])

def hill_encoder(msj: str) -> str:
    num_msj = []
    for _let in msj:
        num_msj.append(dict_encoder[_let])
    
    # guardar 
    deque_num = deque(num_msj)
    list_vector = []
    temp_list = []
    for _ in range(len(num_msj) // 3):
        for _ in range(3):
            temp_list.append(deque_num.popleft())
        list_vector.append(np.array(temp_list))
        temp_list = []

    # le añado numeros de relleno en caso de que el vector no sea de tamaño suficiente
    if len(deque_num) > 0:
        for _ in range(3):
            if len(deque_num) > 0:
                temp_list.append(deque_num.popleft())
            else:
                temp_list.append(0)
        list_vector.append(np.array(temp_list))
    
    res = ''
    text_dec = []
    for _vec in list_vector:
        text_num = np.dot(mat_cif , _vec) % 27
        for _ in text_num:
            res += dict_desencoder[_]

        text_dec.append(text_num)

    return res[:len(msj)]

def hill_desencoder(msj: str) -> str:
    num_msj = []
    for _let in msj:
        num_msj.append(dict_encoder[_let])
    
    # guardar 
    deque_num = deque(num_msj)
    list_vector = []
    temp_list = []
    for _ in range(len(num_msj) // 3):
        for _ in range(3):
            temp_list.append(deque_num.popleft())
        list_vector.append(np.array(temp_list))
        temp_list = []

    # le añado numeros de relleno en caso de que el vector no sea de tamaño suficiente
    if len(deque_num) > 0:
        for _ in range(3):
            if len(deque_num) > 0:
                temp_list.append(deque_num.popleft())
            else:
                temp_list.append(0)
        list_vector.append(np.array(temp_list))
    
    res = ''
    text_dec = []
    for _vec in list_vector:
        text_num = np.dot(mat_cif_t , _vec) % 27
        for _ in text_num:
            res += dict_desencoder[_]

        text_dec.append(text_num)

    return res[:len(msj)]

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

    # eliminar espacios y hacer mayusculas
    msj = msj.upper().replace(" ", "") 
    
    if (typ == 2):
        res = hill_menu(option=temp, msj=msj)
        print(res)

if __name__ == '__main__':
    main()
    