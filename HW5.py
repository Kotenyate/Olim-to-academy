import random

food = 0


class Animal:
    def __init__(self,animalID, name, max_age, hunger, size, sex, place, age=0):
        self.name = name
        self.max_age = max_age
        self.hunger = hunger
        self.size = size
        self.age = age
        self.sex = sex
        self.place = place
        self.alive = True
        self.animalID = animalID


    def growing(self):
        self.age += 1
        if self.age > self.max_age:
            self.death()

    def death(self):
        global food
        food += self.size
        self.alive = False

    def noteating(self):
        self.hunger -= 9
        if self.hunger < 10:
            self.death()


class Predator(Animal):
    def __init__(self, animalID, name, max_age, hunger, size, sex, place, tipe_food, age=0):
        super().__init__(animalID, name, max_age, hunger, size, sex, place, age)
        self.tipe_food = tipe_food
        self.type = 'predator'

    def eating(self):
        chanse = random.choice([0, 1])
        if chanse == 0:
            self.hunger += 53
            if self.hunger > 100:
                self.hunger = 100
            return True
        else:
            self.hunger -= 16
            if self.hunger < 10:
                self.death()
            return False


class Herbivorous(Animal):
    def __init__(self, animalID, name, max_age, hunger, size, sex, place, age=0):
        super().__init__(animalID, name, max_age, hunger, size, sex, place, age)
        self.type = 'herbivorous'

    def eating(self):
        global food
        if food > 0:
            self.hunger += 26
            if self.hunger > 100:
                self.hunger = 100
            food -= 1
        else:
            self.noteating()


all = {
    'bober': [],
    'platypus': [],
    'blob fish': [],
    'pegasus': [],
    'flying squirrel': [],
    'unicorn': [],
    'gnome': [],
    'narwhal': [],
    'penguin': [],
    'daddy shark': [],
    'shrek': [],
    'donkey': []
}


class Bober(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='bober', max_age=20, hunger=73, size=4, sex=sex, place='ground', age=0)


class Platypus(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='platypus', max_age=25, hunger=23, size=4, sex=sex, place='water', tipe_food='blob fish',
                         age=0)


class BlobFish(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='blob fish', max_age=5, hunger=23, size=2, sex=sex, place='water', age=0)


class Pegasus(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='pegasus', max_age=30, hunger=64, size=10, sex=sex, place='air', age=0)


class FlyingSquirrel(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='flying squirrel', max_age=21, hunger=64, size=5, sex=sex, place='air',
                         tipe_food='pegasus', age=0)


class Unicorn(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='unicorn', max_age=32, hunger=73, size=11, sex=sex, place='ground', tipe_food='gnome',
                         age=0)


class Gnome(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='gnome', max_age=10, hunger=73, size=4, sex=sex, place='ground', tipe_food='bober',
                         age=0)


class Narwhal(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='narwhal', max_age=40, hunger=23, size=20, sex=sex, place='water', age=0)


class Penguin(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='penguin', max_age=25, hunger=64, size=9, sex=sex, place='air',
                         tipe_food='daddy shark', age=0)


class DaddyShark(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='daddy shark', max_age=26, hunger=23, size=2, sex=sex, place='water', age=0)


class Shrek(Predator):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='shrek', max_age=70, hunger=73, size=25, sex=sex, place='ground', tipe_food='donkey',
                         age=0)

class Donkey(Herbivorous):
    def __init__(self, animalID, sex):
        super().__init__(animalID, name='donkey', max_age=35, hunger=64, size=9, sex=sex, place='air', age=0)


ep = [Shrek(0, 0), Penguin(0,0), Gnome(0,0), Unicorn(0,0), FlyingSquirrel(0,0), Platypus(0,0)]
eh = [Donkey(0,0), DaddyShark(0,0), Narwhal(0,0), Pegasus(0,0), BlobFish(0,0), Bober(0,0)]
for i in ep:
    print(f'Вид: {i.name}, хищник, ест: {i.tipe_food}, размер: {i.size}, максмальный возраст: {i.max_age}')
for i in eh:
    print(f'Вид: {i.name}, травоядный, размер: {i.size}, максмальный возраст: {i.max_age}')
a = 7
while a != 0:
    for i in all.keys():
        alive_animals = []
        for j in range(len(all[i])):
            if all[i][j].alive:
                alive_animals.append(all[i][j])
        all[i] = alive_animals

    a = int(input('''Что вы хотите сделать?: 
    0 - закончить, 
    1 - добавить новое животное, 
    2 - увеличить запас растительной пищи на планете, 
    3 - посмотреть характеристики животных, 
    4 - размножить особей одного вида, 
    5 - смоделировать движение времени
    '''))
    if a == 1:
        kind = input(f'Введите название вида, особь которого вы хотите добавить:{', '.join(all.keys())} ')
        s = input(f'Введите какого пола m - Male или f - Female существо вы хотите создать ')
        name = input('Введите уникальное имя особи ')
        if kind == 'bober':
            all[kind].append(Bober(name, s))
        elif kind == 'platypus':
            all[kind].append(Platypus(name, s))
        elif kind == 'blob fish':
            all[kind].append(BlobFish(name, s))
        elif kind == 'pegasus':
            all[kind].append(Pegasus(name, s))
        elif kind == 'flying squirrel':
            all[kind].append(FlyingSquirrel(name, s))
        elif kind == 'unicorn':
            all[kind].append(Unicorn(name, s))
        elif kind == 'gnome':
            all[kind].append(Gnome(name, s))
        elif kind == 'narwhal':
            all[kind].append(Narwhal(name, s))
        elif kind == 'penguin':
            all[kind].append(Penguin(name, s))
        elif kind == 'daddy shark':
            all[kind].append(DaddyShark(name, s))
        elif kind == 'shrek':
            all[kind].append(Shrek(name, s))
        elif kind == 'donkey':
            all[kind].append(Donkey(name, s))

    elif a == 2:
        food += 1
        print('Количество еды увеличено на 1')
        print(f'Текущее значение еды = {food}')
    elif a == 3:
        for i in all.keys():
            for j in range(len(all[i])):
                print(f'Вид: {i}, Имя: {all[i][j].animalID}, Возраст: {all[i][j].age}, Сытость: {all[i][j].hunger}, Пол: {all[i][j].sex}')
    elif a == 4:
        kind = input(f'Введите название вида, особьей которого вы хотите размножить:{', '.join(all.keys())} ')
        list_male = []
        list_female = []
        for i in all[kind]:
            if i.sex == 'f':
                list_female.append(i)
            else:
                list_male.append(i)
        print('Особи мужского пола:')
        for i in list_male:
            print(i.animalID)
        print('Особи женского пола:')
        for i in list_female:
            print(i.animalID)
        nf = input('Имя особи женского пола:')
        nm = input('Имя особи мужского пола:')
        for i in all[kind]:
            if nf == i.animalID:
                nf = i
                break
        for i in all[kind]:
            if nm == i.animalID:
                nm = i
                break
        if nf.place == nm.place == 'water':
            if nf.hunger > 50 and nm.hunger > 50:
                for i in range(10):
                    s = random.choice(['f','m'])
                    if kind == 'platypus':
                        all[kind].append(Platypus(input('Введите имя родившейся особи '), s))
                    elif kind == 'blob fish':
                        all[kind].append(BlobFish(input('Введите имя родившейся особи '), s))
                    elif kind == 'narwhal':
                        all[kind].append(Narwhal(input('Введите имя родившейся особи '), s))
                    elif kind == 'daddy shark':
                        all[kind].append(DaddyShark(input('Введите имя родившейся особи '), s))
            else:
                print('Особи не соответсвуют нормам')
        elif nf.place == nm.place == 'air':
            if nf.hunger > 42 and nm.hunger > 42 and nf.age > 3 and nm.age > 3:
                for i in range(4):
                    s = random.choice(['f', 'm'])
                    if kind == 'pegasus':
                        all[kind].append(Pegasus(input('Введите имя родившейся особи '), s))
                    elif kind == 'flying squirrel':
                        all[kind].append(FlyingSquirrel(input('Введите имя родившейся особи '), s))
                    elif kind == 'penguin':
                        all[kind].append(Penguin(input('Введите имя родившейся особи '), s))
                    elif kind == 'donkey':
                        all[kind].append(Donkey(input('Введите имя родившейся особи '), s))
            else:
                print('Особи не соответсвуют нормам')
        else:
            if nf.hunger > 20 and nm.hunger > 20 and nf.age > 5 and nm.age > 5:
                for i in range(2):
                    s = random.choice(['f', 'm'])
                    if kind == 'bober':
                        all[kind].append(Bober(input('Введите имя родившейся особи '), s))
                    elif kind == 'unicorn':
                        all[kind].append(Unicorn(input('Введите имя родившейся особи '), s))
                    elif kind == 'gnome':
                        all[kind].append(Gnome(input('Введите имя родившейся особи '), s))
                    elif kind == 'shrek':
                        all[kind].append(Shrek(input('Введите имя родившейся особи '), s))
            else:
                print('Особи не соответсвуют нормам')

    elif a == 5:
        for i in all:
            for j in all[i]:
                if j.alive:
                    j.growing()
                    if j.type == 'predator':
                        if j.eating():
                            random.choice(all[j.tipe_food]).alive = False
                    else:
                        j.eating()
