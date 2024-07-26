def options(n):
    global a
    if len(a) <= n:
        a.append(options(n - 1) + a[-2])
    return a[n]


a = [1, 1]
print(options(int(input('Введите колличество ступенек :) '))))
