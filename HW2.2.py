try:
    with open('input.txt', 'r') as file:
        f = file.readlines()
        s = input('Какие символы вы хотите удалить? (запишите без пробелов) ')
        s = s + ';' + '\n'
        for i in range(len(f)):
            f[i] = f[i].rstrip(s)
            f[i] = f[i][::-1]

        with open('output.txt', 'w') as output:
            for i in range(len(f)):
                print(f[i], file=output)
except FileNotFoundError:
    print('This file does not exist. Please come back later')