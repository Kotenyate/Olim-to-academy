
while True:
    n = input('Введите колличество строк в треугольнике ')
    if n.isdigit():
        N = int(n)
        a = 1
        s = 1
        for i in range(1, 1 + N):
            r = (N-s) * " " + '*' * a
            print(r)
            s = s + 1
            a = a + 2
        break
    else:
        print('Неккоректный ввод, попробуйте еще раз')
