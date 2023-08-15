# ------------------------ DAY 6 ------------------------


# open, read, close

"""
mi_archivo = open('mi.txt')
print(mi_archivo.read())

print(mi_archivo.readline())

print(mi_archivo.readline().rstrip())

mi_archivo.close()



mi_archivo = open('texto.txt')
print(mi_archivo.read())

mi_archivo = open('texto.txt')
print(mi_archivo.readline())
"""

# changes in file, r (only read) , w (only writing), a ( writing since final of file)

"""archivo = open('mi.txt', 'r')
archivo.close()

archivo = open('mi.txt', 'w')
archivo.write('soy el nuevo texto')
archivo.write(' mundo\n')
archivo.write('mundial')
archivo.close()

archivo = open('mi.txt', 'w')
archivo.writelines(['hola', 'mundo'])

lista = ['antonio', 'perez']
for elemento in lista:
    archivo.writelines(f'{elemento}\n')
archivo.close()


archivo = open('mi.txt', 'a')
archivo.write('soy el nuevo texto2')
archivo.close()


mi_archivo = open('mi_archivo.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo.readline())

line = "Nuevo inicio de sesión"
file = open('mi_archivo.txt', 'a')
file.write('Nuevo inicio de sesión')
file.close()

file = open('mi_archivo.txt', 'r')
print(file.read())

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open('registro.txt', 'a')
for elemento in registro_ultima_sesion:
    registro.writelines(f'{elemento}\t')

registro.close()

registro = open('registro.txt', 'r')
print(registro.read())
"""

# directories, path, os

import os

"""ruta = os.getcwd()
print(ruta)

ruta2 = os.chdir("C:\\Users\\atope\\Documents")
archivo = open('hola.txt', 'r')
print(archivo.read())

ruta2 = os.makedirs("C:\\Users\\atope\\Documents\\otra\\hola.txt")


ruta = "C:\\Users\\atope\\Documents\\hola.txt"
elemento = os.path.basename(ruta)
print(elemento)

ruta = "C:\\Users\\atope\\Documents\\hola.txt"
elemento = os.path.dirname(ruta)
print(elemento)

ruta = "C:\\Users\\atope\\Documents\\hola.txt"
elemento = os.path.split(ruta)
print(elemento)

os.rmdir("C:\\Users\\atope\\Documents\\otra")

otro_archivo = open("C:\\Users\\atope\\Documents\\hola.txt")
print(otro_archivo.read())


from pathlib import Path

carpeta = Path('C:/Users/atope/Documents/')
archivo = carpeta / 'hola.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())


carpeta = Path('C:/Users/atope/Documents/') / 'hola.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
"""

# pathlib

