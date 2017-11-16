class Animal(object):
  name = ''


class Mammal(Animal):
  type = 'Млекопитающее'
  def __init__(self, name):
    self.name = name


class Bird(Animal):
  type = 'Птица'
  def __init__(self, name):
    self.name = name


cow = Mammal(name='Зина')
goat = Mammal(name='Машка')
sheep = Mammal(name='Рита')
pig = Mammal(name='Борис')
duck = Bird(name='Кира')
chicken = Bird(name='Глаша')
goose = Bird(name='Ганс')

print(cow.type, cow.name)
print(goat.type, goat.name)
print(sheep.type, sheep.name)
print(pig.type, pig.name)
print(duck.type, duck.name)
print(chicken.type, chicken.name)
print(goose.type, goose.name)
