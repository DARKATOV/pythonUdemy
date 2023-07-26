def negas(*args):
    condition_init = False
    condition_final = False

    for number in args:
        if condition_init:
            if number == 0:
                condition_final = True
            else:
                pass
        else:




        print(number)
        if condition_init:
            if number == 0:
                condition_final = True
            else:
                pass
        elif number == 0:
            condition_init = True
        else:
            condition_init = False


    return condition_final


list1 = [1, 2, 5, 78, 0, 45, 45, 22, 0, 25, 0]
list2 = [1, 2, 5, 78, 0, 45, 45, 22, 0, 25, 0, 0]

print(negas(list1))
print(negas(list2))
