# ------------------------ DAY 2 ------------------------

# index() ---> ( e index invertido )

"""
mi_texto = 'hola'
final = mi_texto.index('o')
print(final)

mi_texto = 'hola'
final = mi_texto[-2]
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.index('j')
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.index('mij')
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.index('o')
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.index('o', 5)
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.index('o', 5, 14)
print(final)

mi_texto = 'hola meu amijo'
final = mi_texto.rindex('o')
print(final)

palabra = "ordenador"
print(palabra[4])

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index('práctica'))
"""

# slicing ( extract sub-string)

"""
mi_variable = 'esta palabra sera extraida'
final = mi_variable[5:8]
print(final)

mi_variable = 'esta palabra sera extraida'
final = mi_variable[5:]
print(final)


mi_variable = 'esta palabra sera extraida'
final = mi_variable[:8]
print(final)

mi_variable = 'esta palabra sera extraida'
final = mi_variable[2:10:2]
print(final)

mi_variable = 'esta palabra sera extraida'
final = mi_variable[::3]
print(final)

mi_variable = 'esta palabra sera extraida'
final = mi_variable[::-1]
print(final)

mi_variable = 'esta palabra sera extraida'
final = mi_variable[::-2]
print(final)

frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])
"""

# upper, lower, split, join , find , replace

"""
texto = 'YO soy TU padre.Tu eres MI HIJO'
resultado = texto
print(resultado)

# upper
resultado = texto.upper()
print(resultado)

# lower
resultado = texto.lower()
print(resultado)

# split
# por defecto toma los espacios vacios
resultado = texto.split()
print(resultado)

resultado = texto.split('T')
print(resultado)

# join
a = 'antonio'
b = 'gilberto'
c = 'genesis'
d = 'miguel'
e = ''.join([a, b, c, d])
print(e)

e = '-'.join([a, b, c, d])
print(e)

# find --> ( a diferencia de index, si no consigue el valor devuelve -1)
resultado = texto.find('padre')
print(resultado)

# replace
resultado = texto.replace('HIJO', 'hija')
print(resultado)

resultado = texto.replace('e', 'xxx')
print(resultado)

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

lista_palabras = ["La","legibilidad","cuenta."]
print(' '.join(lista_palabras))

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
frase = frase.replace('difícil', 'fácil')
frase = frase.replace('mala', 'buena')
print(frase)

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
frase = frase.replace('difícil', 'fácil').replace('mala', 'buena')
print(frase)
"""

# stings properties  ---> strings are immutable

'''
mi_texto = 'Hola\nmundo'
mi_texto2 = 'Hola
mundo'
print(mi_texto + ' ' + mi_texto2)

n1 = 'Kari'
n2 = 'na'
print(n1+n2)

print(n1*10)

poema = Mil peces blancos 
como si hirviera
el color del agua 

print(poema)

'''

# in

"""
print('agua' in poema)
print('sol' in poema)
print('sol' not in poema)
print('agua' not in poema)
"""

# len

"""sentence = 'El carro rojo corre hace arriba'
print(len(sentence))"""

"""
text = 'Repetición'
print(text*15)

poem = '''Tierra mojada
mis recuerdos de viaje,
entre las lluvias'''
print('agua' not in poem)

print(len('electroencefalografista'))
"""

# lists

"""
a = 'aa'
mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

print(len(mi_lista))

print(mi_lista[0])
print(mi_lista[0:2])

mi_lista2 = ['d', 'e', 'f']
print(mi_lista+mi_lista2)
print((mi_lista+mi_lista2)[0:3])

mi_lista3 = mi_lista+mi_lista2

mi_lista3[0] = '&'
print(mi_lista3)
"""

# append & pop

"""
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']

mi_lista3 = mi_lista+mi_lista2
mi_lista3.append('%')
print(mi_lista3)

mi_lista3.pop()
print(mi_lista3)

mi_lista3.pop(3)
print(mi_lista3)
"""

# sort & reverse

"""
list_final = ['a', 'z', 'd', 'h', 'z', 'p']

list_final.sort()

print(list_final)
print(type(list_final.sort()))

list_final.reverse()
print(list_final)

mi_lista = [True, 'hola', 369, 0, 'ato']

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)


"""

# dictionary --> ( claves y valores. Do not have order inside like arrays )

"""
diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'juan', 'apellido': 'fuentes', 'peso': 45, 'talla': 1.76}
print(cliente['apellido'])
print(cliente['talla'])

dic = {'c1': 565, 'c2': ['a', 'b', 'c'], 'c3': {'s1': 'hola', 's2': 'mundo'}}
print(dic)
print(type(dic))

dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2)
print(dic2['c2'][1].upper())

dic2 = {'c1': 'a', 'c2': 'f'}
dic2['c3'] = 'g'
print(dic2)

dic2[2] = 'E'
print(dic2)

dic2['c2'] = 'E'
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())

mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'
"""

# tuples, count & index of tuples

"""
mi_tuple = (1, 2, 3, 4)
mi_tuple2 = 1, 2, 3, 4
print(type(mi_tuple))
print(type(mi_tuple2))

print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple = (1, 2, 3, 4, (1, 2, 3, 4))
print(mi_tuple[4][2])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))


mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1, 2, 3)
x, y, z = t
print(x, y, z)

t = (1, 2, 3, 1)

print(len(t))

print(t.count(1))
print(t.index(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
"""

# sets ( no se pueden añadir list or dictionaries en los sets)

"""
mi_set = set([1, 2, 3, 4])
{1, 2, 3, 4, 5}

print(mi_set)
print(type(mi_set))

mi_set2 = set([1, 2, 3, 4, 5])
print(mi_set2)
mi_set2 = set({1, 2, 3, 4, 5})
print(mi_set2)
mi_set2 = set((1, 2, 3, 4, 5))
print(mi_set2)

otro_set = {1, 2, 3, 4}
print(otro_set)

mi_set2 = set((1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4))
print(mi_set2)

mi_set2 = set((1, 2, 3, 4, (5, 5, 5), 5, 5, 4, 4))
print(mi_set2)
print(len(mi_set2))
print(2 in mi_set2)

s3 = mi_set2.union(mi_set)
print(s3)

s3.add(8)
print(s3)

s3.remove((5, 5, 5))
print(s3)

s3.remove(2)
print(s3)

s3.remove(2)
print(s3)

s3.discard(20)
print(s3)

s3.discard(1)
print(s3)


set3 = set((2, 3, 4, 5))

variable = set3.pop()
print(variable)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
variable = sorteo.pop()

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add('Damián')
"""

# booleans

"""
var1 = True
var2 = False
print(type(var1), type(var2))

numero = 5 > 3+5
print(numero)

numero = 5 == 2+3
print(numero)

numero = bool(5 < 3)
print(numero)

numero = bool()

lista = [1, 2, 3, 4]
control = 5 in lista
print(type(control), control)

prueba = 0 < 501000000000000000

print(bool((17834 / 34) > (87 * 56)))

print(bool((25**0.5)==5))
"""

# project

text = input('Introduce un texto: ').lower()

print('Introduce tres letras que sean de tu interes')

letter1 = input('Primera letra: ').lower()
while len(letter1) != 1:
    print("Tiene que ser una sola letra, no repetirse ya seleccionadas y no quedar en blanco")
    letter1 = input("Intentalo de nuevo: ")

letter2 = input('Segunda letra: ').lower()
while len(letter2) != 1 or letter2 == letter1:
    print("Tiene que ser una sola letra, no repetirse ya seleccionadas y no quedar en blanco")
    letter2 = input("Intentalo de nuevo: ")


letter3 = input('Tercera letra: ').lower()
while len(letter3) != 1 or letter3 == letter1 or letter3 == letter2:
    print("Tiene que ser una sola letra, no repetirse ya seleccionadas y no quedar en blanco")
    letter3 = input("Intentalo de nuevo: ")

letters = [letter1, letter2, letter3]
print(f'Tus letras son "{letter1}", "{letter2}","{letter3}"')

print(f'La cantidad de veces que aparece la letra "{letter1}" es: {(len(text.split(letter1))-1)}')
print(f'La cantidad de veces que aparece la letra "{letter2}" es: {(len(text.split(letter2))-1)}')
print(f'La cantidad de veces que aparece la letra "{letter3}" es: {(len(text.split(letter3))-1)}')

text2 = text.split()
print(f'La cantidad de palabras ingresadas es: {len(text2)}')

print(f'La primera letra del texto ingresado es: {text2[0][:1]}')
print(f'La última letra del texto ingresado es: {text2[-1][-1]}')

booleans_answers = {'-1': False,'0': True }
search_motor = text.find('python')

processed_answer = booleans_answers[f'{search_motor}']

print(f'Se encuentra la palabra python presente en el texto ingresado: {processed_answer}\nGracias por usar nuestra app')














