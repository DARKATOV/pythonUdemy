# ------------------------ DAY 2 ------------------------

# var --->  types of data, integer, floating, list, dic(key and value), tuples, sets , bool

"""
nombre = 'Juan'
print(nombre)

nombre = 'Laura'
print(nombre)

edad = 30
print(edad)

edad1 = 30
edad2 = 10
print(edad1+edad2)

nombre1 = 'Hola'
nombre2 = 'Mundo'
frase = nombre1 + ' '+ nombre2
print(frase)

nombre = input('Tu nombre es: ')
print(nombre)

nombre = 'Tony Soprano'
edad = 51

nombre = 'Julia'
apellido = 'Roberts'
nombrecompleto = nombre + ' ' + apellido

curso = 'Python'
print('Estás tomando un curso de '+curso)
"""

# names of vars ( always start with letter, never use a reserved words, snake_case )

# integers & floats

"""
nombre_de_estudiante = 'Juan'

mi_numero = 4
mi_numero = 8+9
print(mi_numero +mi_numero)

print(type(mi_numero))

mi_numero = 8.8
print(mi_numero)
print(type(mi_numero))

mi_numero = 5+8.8
print(mi_numero)
print(type(mi_numero))

mi_numero = 5.2+8.8
print(mi_numero)
print(type(mi_numero))

# all to add from input is string
edad = input('Dime tu edad: ') 
print('Tu edad es ' + edad)

nueva_edad = 1 + edad
print('Vas a cumplir ' + nueva_edad)
print(nueva_edad)

num_entero = 24
print(type(num_entero))

num_decimal = 3.14
print(type(num_decimal))

num1 = 7.5
num2 = 2.5
print(type(num1+num2))
"""

# casting ----> conversiones ( implicita / explicita )

"""
num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))


# not rounded, only erase the floats numbers

edad = input('Dime tu edad: ')
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad
print(type(nueva_edad))
print(nueva_edad)
print('Tu nueva edad va a ser: ' + str(nueva_edad))

num1 = 7.5
num1 = int(num1)
print(type(num1))

num2 = 10
num2 = float(num2)
print(type(num2))

num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))
"""

# format strings

"""
print('Mi auto es rojo y de matricula 266254 ')
color = 'rojo'
matricula = 266254
print('Mi auto es ' + color + ' y de matricula ' + str(matricula))
print('Mi auto es {} y de matricula {}'.format(color, matricula))
"""

# literal strings

"""
color = 'rojo'
matricula = 266254
print(f'Mi auto es {color} y de matricula {matricula}')

x = 8
y = 7
print(f'Mis numeros son {x} y {y}')
print(f'La suma de X y Y es igual a {x+y}')

color = 'azul'
medida = 'estandar'
print('El equipo es de modelo {} y de color {}'.format(medida, color))

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f'Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}')

puntos_nuevos = 350
puntos_totales = 1225
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')

puntos_anteriores = 875
puntos_nuevos = 350
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores+puntos_nuevos} puntos')
"""

# maths operators

"""
x = 6
y = 2
print(f'{x} mas {y} es igual a {x+y}')
print(f'{x} menos {y} es igual a {x-y}')
print(f'{x} por {y} es igual a {x*y}')
print(f'{x} entre {y} es igual a {x/y}')
z = 7

# division al piso ( cociente ) 
print(f'{z} dividido al piso de {y} es {z//y}')
# modulo
print(f'{z} modulo de {y} es igual {z%y}')
# el modulo de un numero por dos es 0 es par
print(f'{z} elevado a {y} es igual {z**y}')
print(f'{z} elevado a {3} es igual {z**3}')
print(f'La raiz cuadrada de {z} es igual a {z**0.5}')

print(f'{874//27}')

print(f'{456%33}')

print(f'{783**0.5}')
"""

# round ---> round(parameter1, parameter2)

"""
print(90/7)
print(round(90/7))

result = 90/7
print(round(result))

value = 8.8542121
value = round(value, 3)
print(value)
print(type(value))
value = round(value)
print(type(value))

print(round(10/3, 2))

valor = 10.676767
print(round(valor))

print(round(5**0.5, 4))

num1 = round(13/2, 0)
print(num1)
"""

# project

name = input('Nombre de empleado: ')
amount = float(input('Ingresos generados netos a la empresa: '))

print(f'Hola {name}, tus aportes a la empresa \nautoregistrados y liquidados son de\n{amount}, '
      f'por lo que el presente mes,\nte corresponden {round(amount*0.13,2)}')









