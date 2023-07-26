def palabratron(word):
    nueva_lista = set([*word])
    nueva_lista = list(nueva_lista)
    nueva_lista.sort()
    return nueva_lista


print(palabratron('atolardo'))
