
from random_word import RandomWords
import string

r = RandomWords()
to_word = r.get_random_word()
list_r = list(to_word)
to_adivine = len(list_r) - 2

print('Welcome to hangman game :D. You have 8 tries, good luck')
print(list_r)


def tshow():
    lista = []
    counter = 0
    longitud = len(list_r)
    for lett in list_r:
        if counter == 0:
            lista.append(lett)
            counter += 1
        elif counter < longitud - 1:
            lista.append('_')
            counter += 1
        else:
            lista.append(lett)

    return lista


print(tshow())


def enter_letter():
    lower_check_list = list(string.ascii_lowercase)
    condicion = False
    while not condicion:
        letter = input('Ingresa una letra por favor: ').lower()
        if len(letter) > 1:
            print('Solo puedes ingresar una caracter. Intentalo de nuevo')
        else:
            if letter not in lower_check_list:
                print('Solo se aceptan caracteres alfabeticos. Intentalo de nuevo')
            else:
                condicion = True
    return letter


def verificar_exitencia():
    lista = []
    obtenidos = []
    longitud = len(list_r)
    counter = 0
    acert = False
    lives = 8

    while lives >= 0:
        print(obtenidos)
        obtenido = enter_letter()
        obtenidos.append(obtenido)
        for lett in list_r:
            if counter == 0:
                lista.append(lett)
                counter += 1
            elif counter < longitud - 1:
                if lett in obtenidos:
                    obtenidos.append(lett)
                    acert = True
                    pass
                else:
                    lista.append('_')
                counter += 1
            else:
                lista.append(lett)

        if acert:
            print(f'Has acertado la letra {obtenido}\n {lista}')

        else:
            print(f'No has acertado con la letra {obtenido}\n {lista}')
            lives -= 1
        counter = 0
        lista.append(enter_letter())

    else:
        repeat = input(f'No te quedan mas vidas, quieres intentar de nuevo? (S/N)')
        if repeat.lower() == 's':
            lives = 8
            letra_final = enter_letter()
        else:
            print('Hasta pronto :D')


verificar_exitencia()








