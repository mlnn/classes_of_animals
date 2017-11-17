class Animal(object):
    name, sound = '', ''
  
    def __init__(self, name):
        self.name = name

    def say(self):
        return self.sound


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Cow(Mammal):
    sound = 'Мууу'


class Goat(Mammal):
    sound = 'Мее'


class Pig(Mammal):
    sound = 'Хрю'
    

class Sheep(Mammal):
    sound = 'Бее'


class Duck(Bird):
    sound = 'Кря'


class Chicken(Bird):
    sound = 'Кукареку'
    

class Goose(Bird):
    sound = 'Куа'


my_cow = Cow(name='Зина')
my_pig = Pig(name='Борис')
my_chicken = Chicken(name='Глаша')
my_goat = Goat(name='Машка')
my_sheep = Sheep(name='Рита')
my_duck = Duck(name='Кира')
my_goose = Goose(name='Ганс')

for i in [my_cow, my_pig, my_chicken, my_goat, my_sheep, my_duck, my_goose]:
    if isinstance(i, Bird):
        print('Я птица, меня зовут {}, я говорю {}'.format(i.name, i.say()))
    if isinstance(i, Mammal):
        print('Я млекопитающее, меня зовут {}, я говорю {}'.format(i.name, i.say()))
