class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def pname(self):
        print('Это - {}, имя животного - {}'.format(self.type, self.name))


class Mammal(Animal):
    def __init__(self, name):
        super().__init__('Млекопитающее', name)


class Bird(Animal):
    def __init__(self, name):
        super().__init__('Птица', name)


class Cow(Mammal):
    def __init__(self):
        super().__init__('Зина')


class Goat(Mammal):
    def __init__(self):
        super().__init__('Машка')


class Sheep(Mammal):
    def __init__(self):
        super().__init__('Рита')


class Pig(Mammal):
    def __init__(self):
        super().__init__('Борис')


class Duck(Bird):
    def __init__(self):
        super().__init__('Кира')


class Chicken(Bird):
    def __init__(self):
        super().__init__('Глаша')


class Goose(Bird):
    def __init__(self):
        super().__init__('Ганс')

cow = Cow()
goat = Goat()
sheep = Sheep()
pig = Pig()
duck = Duck()
chicken = Chicken()
goose = Goose()

cow.pname()
goat.pname()
sheep.pname()
pig.pname()
duck.pname()
chicken.pname()
goose.pname()
