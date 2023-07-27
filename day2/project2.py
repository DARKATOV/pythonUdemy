nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")

# project

name = input('Nombre de empleado: ')
amount = float(input('Ingresos generados netos a la empresa: '))

print(f'Hola {name}, tus aportes a la empresa \nautoregistrados y liquidados son de\n{amount}, '
      f'por lo que el presente mes,\nte corresponden {round(amount*0.13,2)}')
