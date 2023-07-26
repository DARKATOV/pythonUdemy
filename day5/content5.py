# ------------------------ DAY 5 ------------------------


# functions, methods,

"""
dic = {'clave1': 100, 'clave2': 500}
print(dic.popitem())
print(dic)

x = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
text = x.lstrip()
print(text)

x = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
modify = x.lstrip(',:%_#')
print(f'{modify}')

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
"""


# functions
"""def saludar_persona():
    print('Hola')


saludar_persona()


def saludar_persona(nombre):
    print(f'Hola {nombre}')


saludar_persona('Fernando')
saludar_persona('Miguel')


def saludar():
    print('¡Hola mundo!')


saludar()


def bienvenida(nombre):
    print(f'¡Bienvenido {nombre}!')


nombre_persona = 'Antonio'
bienvenida(nombre_persona)


def cuadrado (numero):
    print(numero*numero)


un_numero = 10
cuadrado(un_numero)


def sumar(numb1, numb2):
    return numb1+numb2


numbers = [1, 2]
print(sumar(numbers[0], numbers[1]))


def sumar(numb1, numb2):
    total = numb1 + numb2
    return total


numbers = [1, 2]
print(sumar(numbers[0], numbers[1]))


def potencia(base, exponente):
    return base**exponente


def usd_a_eur(USD):
    return USD * 0.90


dolares = 11000


def invertir_palabra(elemento):
    return elemento.upper()[::-1]


palabra = 'batman'
"""

# dinamycs functions


"""def chequear_3_cifras(numero):
    return numero in range(100, 1000)


suma = 50 + 500
print(chequear_3_cifras(suma))


def chequear_3_cifras(elementos):

    lista_aprobados = []

    for number in elementos:
        if number in range(100, 1000):
            lista_aprobados.append(number)
        else:
            pass
    return lista_aprobados


lista = [100, 500, 500]
print(chequear_3_cifras(lista))


def todos_positivos(elementos):
    for number in elementos:
        if number < 0:
            return False
        else:
            pass
    return True


lista_numeros = [0, -50, 52, -5, -69, 47, -966]


def suma_menores(elementos):
    suma = 0

    for number in elementos:
        if number <= 0 or number > 1000:
            pass
        else:
            suma += number
    return suma


lista_numeros = [0, -50, 52, -5, -69, 47, -966]


def cantidad_pares(elementos):
    cantidad = 0
    for number in elementos:
        if number%2==0:
            cantidad += 1
        else:
            pass
    return cantidad


lista_numeros = [0, -50, 52, -5, -69, 47, -966]


precios_cafe = [('capuccino', 1.5), ('moca', 2), ('expresso', 1.2)]

for cafe, precio in precios_cafe:
    print(cafe)


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro1 = ''
    for cafe1, precio1 in lista_precios:
        if precio1 > precio_mayor:
            precio_mayor = precio1
            cafe_mas_caro1 = cafe1
        else:
            pass
    return cafe_mas_caro1, precio_mayor


print(cafe_mas_caro(precios_cafe))"""


# lista inicial

from random import shuffle

"""palitos = ['-', '--', '---', '----']


def mezclar(lista1):
    shuffle(lista1)
    return lista1


def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del uno al cuatro: ')

    return int(intento)


def chequear_intento(lista2, intento):
    if lista2[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Te salvaste')

    print(f'Te ha tocado {lista2[intento-1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)
"""


"""from random import *


def lanzar_dados():
    dado1 = randint(1, 7)
    dado2 = randint(1, 7)
    suma_dados = dado1 + dado2
    print(suma_dados)
    return suma_dados


def evaluar_jugada(suma_dados):
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


print(evaluar_jugada(lanzar_dados()))



from random import *

def lanzar_dados():
    dado1 = randint(1, 7)
    dado2 = randint(1, 7)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


lanzo = lanzar_dados()
print(lanzo)
evaluar= evaluar_jugada(lanzo[0], lanzo[1])


lista_numeros = [1, 2, 34, 44, 5, 46, 44, 44, 57, 85, 11, 78, 78, 1, 111, 111, 111]


def reducir_lista(lista):
    lista_nueva = list(set(lista))
    mayor = max(lista)
    lista_nueva.remove(mayor)
    return lista_nueva


lista_generada = reducir_lista(lista_numeros)
print(lista_generada)


def promedio(lista):
    count = 0
    long = len(lista)
    print(long)
    for number in lista:
        count = count + number
    return count/long


promedio_generado = promedio(lista_generada)
print(promedio_generado)



import random


lista_numeros = [1, 2, 34, 5, 11, 44, 46, 78, 85, 57]


def lanzar_moneda():
    resultado = ['Cara', 'Cruz']
    hola = random.choice(resultado)
    return hola


pre_select = lanzar_moneda()

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print('La lista se autodestruirá')
        lista.clear()
        return lista
    else:
        print('La lista fue salvada')
        return lista



total = probar_suerte(pre_select, lista_numeros)
print(total)


"""

# args , kwargs


"""
def suma(a,b):
    num = a + b
    return num



def sum(*numeros):

    count = 0
    for elemento in numeros:
        count = count + elemento
    return count



print(sum( 50, 20, 64, 78, 85))


def sume(*numbers):

    return sum(numbers)

print(sume(50, 20, 64, 78, 85))



def suma_cuadrados(*valores):
    count = 0
    for valor in valores:
        count += valor**2
    return count



def suma_absolutos(*valores):
    count = 0
    for element in valores:
        if element < 0:
            converted = element * -1
            count += converted
        else:
            count += element
    return count


def numeros_persona(name, *numeros):
    count = 0
    for elemento in numeros:
        count += elemento
    return f'{name}, la suma de tus números es {count}'
    
"""

# kwargs


def suma(**kwargs):
    total = 0
    for item in kwargs:
        print(type(kwargs))
    for clave2, valor in kwargs.items():
        print(f'{clave2} = {valor}')
        total += valor
    return total


print(suma(x=3, y=5, z=9))


def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    total = 0

    for elemento in args:
        print(f'{elemento}')

    for llave, valor in kwargs.items():
        print(f'{llave} = {valor}')


prueba(15, 2000, 4552, 455, 500, 700, 800,  x=3, y=5, z=9)


def cantidad_atributos(**kwargs):
    total = 0
    for elemento in kwargs:
        total += 1
    return total


def lista_atributos(**kwargs):
    lista = []
    for elemento in kwargs:
        lista.append(elemento)
    return lista


def lista_atributos(**kwargs):
    lista = []
    for elemento, valor in kwargs.items():
        lista.append(valor)
    return lista


def describir_persona(name, **kwargs):
    print(f'Características de: {name}')
    for caracte, valor in kwargs.items():
        print(f'{caracte}: {valor}')


describir_persona('Antonio', color_ojos='azul', color_pelo='gris')
