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
"""

lista_numeros = [1, 2, 34, 44, 5, 46, 44, 44, 57, 85, 11, 78, 78, 1, 111, 111, 111]


def reducir_lista(lista):
    count = 0
    mayor = max(lista)
    while count == 0:
        seter = set(lista)
        if len(seter) == len(lista):
            count = 0
        else:
            count = 1
    seter.remove(mayor)
    nueva_lista = []
    for number in seter:
        index = 0
        nueva_lista.append(number[index])
    return nueva_lista


reducir = reducir_lista(lista_numeros)
print(reducir)

def promedio(lista_simplificada):
    suma = 0
    for number in list:
        print(number)
        suma = suma + number

    promedio
    return suma/len(lista_simplificada)


prome = promedio(reducir)
print(prome)







