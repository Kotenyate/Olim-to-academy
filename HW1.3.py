def summir(n):
    s = 0
    for i in n:
        s = s + int(i)
    return s


while True:
    n = input('Введите целое положительное число ')
    s = 0
    if n.isdigit():
        s = summir(n)
        while s > 9:
            n = str(s)
            s = summir(n)
        print(s)

        break
    else:
        print('Неккоректный ввод, попробуйте еще раз')
