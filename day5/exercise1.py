def devolver_distintos(*numbers):
    total = 0
    lista = []

    for number in numbers:
        total += number
        lista.append(number)

    maximu = max(lista)
    minimu = min(lista)

    intermedio = total - maximu - minimu

    print(total, minimu, maximu)

    if total > 15:
        return f'El numero mayor es: {maximu}'
    elif total < 10:
        return f'El numero menor es: {minimu}'
    else:
        return f'El numero intermedio es: {intermedio}'


print(devolver_distintos(1, 2, 10))
