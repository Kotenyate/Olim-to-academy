try:
    with open('cities.txt', 'r') as city:
        c0 = city.readlines()
        c0 = sorted(c0)
        c = []
        for i in range(len(c0)):
            c0[i] = c0[i].rstrip()
            c.append(c0[i].split(':'))
        print(c)
        n = int(input('минимальное значение количества житилей '))
        f = []
        for i in range(len(c)):
            if int(c[i][1]) >= n:
                f.append(c[i])
        print(f)
        with open('filtered_cities.txt', 'w') as fcity:
            for i in range(len(f)):
                fcity.write(f[i][0]+':'+f[i][1]+'\n')
except FileNotFoundError:
    print('This file does not exist. Please come back later')

