try:
    with open('input.txt', 'r') as file:
        f0 = file.readlines()
        f1 = []
        for i in range(len(f0)):
            f0[i] = f0[i].strip(' \n,')
            f1.append(f0[i].split(':'))

        f = {}
        for i in range(len(f1)):
            f1[i][1] = f1[i][1].strip(' ')
            f[f1[i][0]] = f1[i][1].split(', ')
        print(f)
        a = input('Введите название курса с большой буквы')
        r = []
        for i in f.keys():
            if a in f[i]:
                print(i)
except FileNotFoundError:
    print('This file does not exist. Please come back later')