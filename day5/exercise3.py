def negas(*args):
    condition_init = False
    condition_final = False

    for number in args:
        if condition_init:
            if number == 0:
                condition_final = True
            else:
                condition_init = False
        else:
            if number == 0:
                condition_init = True
            else:
                condition_init = False

    return condition_final


print(negas(1, 2, 5, 78, 0, 45, 45, 22, 0, 25, 0, 5, 0, 5, 0, 0))
print(negas(1, 2, 5, 78, 0, 45, 45, 22, 0, 25, 5, 0))
print(negas(1, 2, 5, 78, 0, 0, 45, 45, 22, 0, 25, 5, 0))

