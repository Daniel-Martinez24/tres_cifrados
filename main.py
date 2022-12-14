# librerias
import numpy as np
from collections import deque

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

# código otp
valores_msj, valores_key, valores_cryp, msj_encript = [], [], [], []
def otp_menu(option: int, msj: str, key: str) -> str:
    return otp_encoder(msj, key) if option == 1 else otp_desencoder(msj, key)

def otp_encoder(msj : str, key : str) -> str:
    for pos in range (len(msj)):
        letra_msj = msj[pos]
        letra_key = key[pos]
        valores_msj.append(dict_encoder[letra_msj]) #Se añade el valor de la letra
        valores_key.append(dict_encoder[letra_key]) #a la lista de valores
        valores_cryp.append(valores_msj[pos]+valores_key[pos]) #Se añade la sumatoria de valores de msj y llave a lista de valores encriptados

        if valores_cryp[pos]>26:
            valores_cryp[pos] = (valores_cryp[pos]%26)-1

        msj_encript.append(dict_desencoder[valores_cryp[pos]]) #Se convierten los valores a letras del nuevo msj encriptado
        #print(valores_cryp)

    result = ''.join(msj_encript) #Se añaden a string las letras del nuevo msj encriptado
    return result

def otp_desencoder(msj: str, key: str) -> str:
    for pos in range (len(msj)):
        letra_msj = msj[pos]
        letra_key = key[pos]
        valores_msj.append(dict_encoder[letra_msj]) #Se añade el valor de la letra
        valores_key.append(dict_encoder[letra_key]) #a la lista de valores
        valores_cryp.append(valores_msj[pos]-valores_key[pos]) #Se añade la resta de valores de msj y llave a lista de valores encriptados

        if valores_cryp[pos]<0:
            valores_cryp[pos] = (26+valores_cryp[pos]+1)

        msj_encript.append(dict_desencoder[valores_cryp[pos]]) #Se convierten los valores a letras del nuevo msj encriptado

    return ''.join(msj_encript) #Se añaden a string las letras del nuevo msj encriptado

# código playfair
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 
        'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def playflair_menu(msj:str, option:int) -> str:
    while True:
        key = input('Qué llave deseas utilizar? ').upper()
        if (key.isalpha()):
            break
        else:
            print('solo letras en la clave')
    return playfair(key, msj) if option == 1 else playfair(key, msj, encrypt=False)
    
def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    for letter in range(65,91):
        if letter==74:
                continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix

def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message

def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue
def playfair(key, message, encrypt=True):
    inc = 1
    if encrypt==False:
        inc = -1
    matrix = create_matrix(key)
    message = message.upper()
    message = message.replace(' ','')    
    message = separate_same_letters(message)
    cipher_text=''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: #Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:# Rule 3, the letters are in the same column
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: #Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

# codigo Hill
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

    if (typ == 3):
        while True:
            key = input('Qué llave deseas utilizar? ').upper()
            if (len(msj)==len(key)):
                break
            else:
                print('La palabra y la llave deben tener el mismo número de letras')

        print(otp_menu(option=temp, msj=msj, key=key))
    
    if (typ == 1):
        print(playflair_menu(option=temp, msj=msj))


if __name__ == '__main__':
    main()
    