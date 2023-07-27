
from random_word import RandomWords

r = RandomWords()
to_word = r.get_random_word()
list_r = list(to_word)
to_adivine = len(list_r) - 2

print('Welcome to hangman game :D. You have 8 tries, good luck')
print(list_r)


def tshow():
    lista = []
    counter = 0
    for lett in list_r:
        if counter == 0:
            lista.append(lett)
            counter += 1
        elif counter == (to_adivine + 1):
            lista.append(lett)
            counter += 1
        else:
            lista.append('_,')
    return lista


print(tshow())
show_list = [list_r[0], to_adivine *'_']


def correct(letter):
    for lett in list_r:
        if lett == letter:
            show_list.append(lett)
        else:
            show_list.append('_')
    show_list.append(list_r[to_adivine+1])

    return show_list


letra = input('Enter a letter: ')
letra_lower = letra[0].lower()

if letra_lower in list_r:
    indict = list_r.index(letra_lower)
    print(correct(letra_lower))
else:
    print(show_list)






