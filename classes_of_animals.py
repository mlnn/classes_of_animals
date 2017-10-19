class Animal:
    legs = 0
    wings = False
    sounds = ''

    def born(self):
        print('Оно родилось')

    def death(self):
        print('Оно умерло')

    def leg(self, add_leg):
        self.legs = self.legs + add_leg

    def wing(self, add_wing):
        self.wings = add_wing

    def sound(self, add_sound):
        self.sounds = add_sound

    def info(self):
        if self.wings:
            print('У этого животного есть крылья, {} ноги и оно издает звук "{}"'.format(self.legs, self.sounds))
        else:
            print('У этого животного {} ноги и оно издает звук "{}"'.format(self.legs, self.sounds))


class Cow(Animal):
    def __init__(self):
        super().sound('Муу')
        super().leg(4)
        super().wing(False)


class Goat(Animal):
    def __init__(self):
        super().sound('Мее')
        super().leg(4)
        super().wing(False)


class Sheep(Animal):
    def __init__(self):
        super().sound('Бее')
        super().leg(4)
        super().wing(False)


class Pig(Animal):
    def __init__(self):
        super().sound('Хрю')
        super().leg(4)
        super().wing(False)


class Duck(Animal):
    def __init__(self):
        super().sound('Кря')
        super().leg(2)
        super().wing(True)


class Chicken(Animal):
    def __init__(self):
        super().sound('Ко-ко-ко')
        super().leg(2)
        super().wing(True)


class Goose(Animal):
    def __init__(self):
        super().sound('Куа')
        super().leg(2)
        super().wing(True)

cow = Cow()
cow.born()
cow.info()
cow.death()

goat = Goat()
goat.born()
goat.info()
goat.death()

sheep = Sheep()
sheep.born()
sheep.info()
sheep.death()

pig = Pig()
pig.born()
pig.info()
pig.death()

duck = Duck()
duck.born()
duck.info()
duck.death()

chicken = Chicken()
chicken.born()
chicken.info()
chicken.death()

goose = Goose()
goose.born()
goose.info()
goose.death()
