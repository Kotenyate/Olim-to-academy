try:
    with open('input.txt', 'r') as file:
        f = file.readlines()
        for i in range(len(f)):
            f[i] = f[i].split(',')
        s = 0
        for i in range(len(f)):
            s = s + int(f[i][1])

        s = s / len(f)
        with open('output.txt', 'w') as output:
            for i in range(len(f)):
                if int(f[i][1]) > s:
                    print(f[i][0], file=output)
except FileNotFoundError:
    print('This file does not exist. Please come back later')

