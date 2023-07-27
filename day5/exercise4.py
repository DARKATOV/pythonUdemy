

def contar_primos(num):
    if num == 1 or num == 0:
        return 0
    else:
        contador = 0
        rango = range(2, num + 1)
        cortado = range(2, num)
        print(rango, cortado)
        for digito in rango:
            print(digito)
            for divisor in range(2, digito):
                print(digito, divisor)
                if (digito % divisor) == 0:
                    print('+1')
                    contador += 1
                    break
                else:
                    pass

    return num-1-contador
    return 'hola'

print(contar_primos(100))
