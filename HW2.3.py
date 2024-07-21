try:
    with open('input.txt', 'r') as file1:
        f1 = file1.readlines()
        with open('input2.txt', 'r') as file2:
            f2 = file2.readlines()
            f = f1 + f2
            f = sorted(f)
            print(f)
            print(f1)

            with open('output.txt', 'w') as output:
                for i in range(len(f)):
                    print(f[i].strip('\n'), file=output)
except FileNotFoundError:
    print('This file does not exist. Please come back later')