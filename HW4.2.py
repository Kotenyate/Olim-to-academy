try:
    def evclalg(a,b):
        if a == 0 or b == 0:
            return a + b
        else:
            if a > b:
                a = a % b
            else:
                b = b % a
            return evclalg(a, b)

    a = int(input('введите целое число a '))
    b = int(input('введите целое число b '))
    if a == 0 and b == 0:
        print('Оба числа равны нулю, у нулей нет НОД')
    else:
        print(evclalg(a, b))
except ValueError:
    print('вы ввели не число, попробуйте еще раз')
