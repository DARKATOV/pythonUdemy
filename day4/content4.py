# ------------------------ DAY 4 ------------------------

# comparation

"""mi_bool = 10==25
print(mi_bool)

mi_bool = 'blanco'=='blanco'
print(mi_bool)

mi_bool = 'blanco'=='Blanco'
print(mi_bool)

mi_bool = '100'==100
print(mi_bool)

mi_bool = 100.00==100
print(mi_bool)


mi_bool = 100 != 20
print(mi_bool)

num1 = 36
num2 = 17

mi_bool = num1 >= num2
print(mi_bool)

num1 = 25**(1/2)
num2 = 5

mi_bool = num1 == num2
print(mi_bool)

num1 = 64 * 3
num2 = 24 * 8

mi_bool = num1 != num2
print(mi_bool)
"""

# logical operators

"""mi_bool = 4<5<6
print(mi_bool)

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)

mi_bool = (4 < 5) or (5 > 6)
print(mi_bool)

texto = 'esto es un texto breve'

verTexto = 'frase' in texto
print(verTexto)

verTexto = 'texto' in texto
print(verTexto)

verTexto = 'texto' in texto and 'breve' in texto
print(verTexto)

mi_bool = 'a' == 'a'
print(mi_bool)

mi_bool = not ('a' == 'a')
print(mi_bool)

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num2 < num1 < num3
print(mi_bool)

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num1 > num2 or num1 < num3
print(mi_bool)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool)"""

# flow controls

"""if 10 > 9:
    print('es correcto')
else:
    print('falso')

if 10 > 15:
    print('es correcto')
else:
    print('falso')

if 10 == 15:
    print('es correcto')
else:
    print('falso')

mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

edad = 16
califiacion = 9

if edad < 18:
    print('Eres menor de edad')
    if califiacion >= 7:
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres Adulto')

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

edad = 16
tiene_licencia = False
if edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif tiene_licencia == True:
    print ("Puedes conducir")
else:
    print("No puedes conducir. Necesitas contar con una licencia")


habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Cumples con los requisitos para postularte")
"""

# loops, for

"""
nombres = ['juan', 'pedro', 'ana']

for elemento in nombres:
    print(f'Hola {elemento}')

for elemento in nombres:
    index = nombres.index(elemento) + 1
    print(f'Hola {elemento} con numero de letra {index}')

for elemento in nombres:
    if elemento.startswith('p'):
        print(f'Hola {elemento} si cumples las condiciones de nombre')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

for letra in 'python':
    print(letra)

for letra in ['python', 5, 8, 'fgdgfdgfd']:
    print(letra)

for a,b in [[1,2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for key in dic:
    print(key)

for key in dic.items():
    print(key)

for key in dic.values():
    print(key)

for key, dir in dic.items():
    print(key, dir)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f'Hola {alumno}')



lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

print(suma_numeros)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero 
    else:
        suma_impares = suma_impares + numero

print(suma_impares)
print(suma_pares)
"""

# loop while (mientras) break-continue-pass

"""monedas = 5

while monedas > 0:
    print(f'Tengo {monedas}')
    monedas -= 1
else:
    print('No tengo mas dinero')



respuesta = 'S'

while respuesta == 'S':
    respuesta = input('Quieres seguir? (S/N)')
else:
    print('Gracias')

while respuesta == 'S':
    pass

nombre = input('Tu nombre ')

for letra in nombre:
    print(letra)
    if letra == 'o':
        break

numero = 10

while numero >= 0:
    print(numero)
    numero -= 1


numero = 50

while numero >=0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1




lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in lista_numeros:
    if number > 0: 
        print(number)
    else:
        break
"""

# range

"""for numero in range(5):
    print(numero)

for numero in range(1,5):
    print(numero)

for numero in range(21, 50, 5):
    print(numero)

lista = list(range(1, 101))
print(lista)

mi_lista = list(range(2500, 2586))

mi_lista = list(range(3, 301, 3))




suma_cuadrados = 0

lista = list(range(1,16))

for number in lista:
    suma_cuadrados += number ** 2
"""

# enumerate

"""lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)
    indice += 1

for indice, item in enumerate(lista):
    print(indice, item)
    indice += 1

mis_tuples = list(enumerate(lista))
print(mis_tuples)

mis_tuples = list(enumerate(lista))
print(mis_tuples[0][1])

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

indice = 0

for nombre in enumerate(lista_nombres):
    indice += 1
    print(f'{nombre[1]} se encuentra en el índice {nombre[0]}')


word = "Python"
lista_indices = list(enumerate(word))

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for name in enumerate(lista_nombres):
    if name[1].startswith('M'):
        print(name[0])
"""

# zip

"""nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
combinados = list(zip(nombres, edades))

print(combinados)


nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Carcas', 'Maracay', 'Merida', 'Bogota']
combinados = list(zip(nombres, edades, ciudades))

print(combinados)


nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Carcas', 'Maracay', 'Merida', 'Bogota']
combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} y vive en {ciudad}')

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combina = list(zip(paises, capitales))


for pais, capital in combina :
    print(f'La capital de {pais} es {capital}')

marcas = ['Audi', 'BMW', 'Mercedez']
productos = ['Coches', 'Motores', 'Llantas']
mi_zip = zip(marcas, productos)

print(mi_zip)
print(mi_zip)

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

esp = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
por = ['um', 'dois', 'três', 'quatro', 'cinco']
ing = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(esp, por, ing))
print(numeros)
"""

# min, max

"""menor = min(58, 98, 23, 56)
print(menor)

mayor = max(58, 98, 23, 56)
print(mayor)

lista = [7, 85, 525, 548, 9685, 745869, 5784565, 7845]
print(max(lista))

lista_nombres = ['alicia', 'carlos', 'pedro', 'zamora']
lista_nombres2 = ['alicia', 'Carlos', 'pedro', 'zamora']

print(min(lista_nombres))
print(min(lista_nombres2))

nombre = 'Gilberto'
print(min(nombre))

nombre = 'Gilberto'
print(min(nombre.lower()))

dic = {'C1': 45, 'C2': 11}
print(min(dic))

dic = {'C1': 45, 'C2': 11}
print(min(dic.values()))

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros)-min(lista_numeros)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
"""

# randoms numbers, import python, randint(), uniform(), random(), choice(), shuffle()

"""from random import randint

aleatorio = randint(1, 50)
print(aleatorio)


from random import *

aleatorio = uniform(1, 50)
print(aleatorio)

aleatorio = round(aleatorio, 1)
print(aleatorio)

colores = ['azul', 'rojo', 'blanco', 'morado']
aleato = choice(colores)
print(aleato)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)
print(numeros)


from random import randint
aleatorio = randint(1, 10)

from random import *
aleatorio = uniform(0, 1)


from random import choice
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
"""

# list +

"""from random import *

palabra = 'pyyhon'
lista = []

for letra in palabra:
    lista.append((letra))
print(lista)

palabra = 'pyyhon'
lista = [letra for letra in palabra]
print(lista)

lista = [letra for letra in 'python']
print(lista)

lista = ([n for n in range(0, 21, 2)])
shuffle(lista)
print(lista)


lista = ([n for n in range(0, 21, 2) if n * 2 > 10])
print(lista)

lista2 = ([n if n * 2 > 10 else 'no' for n in range(0, 21, 2)])
print(lista2)

pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n % 2 == 0]

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((n-32)*(5/9)) for n in temperatura_fahrenheit]
"""



# match

"""serie = 'N-02'
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe ese producto')

cliente = {'nombre': 'Federico', 'edad': 45, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica': {'protagonista': 'Keanue', 'director': 'Lana y Lilly'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('No se que es esto')
"""
