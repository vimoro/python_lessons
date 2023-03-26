def move():
    pass


class Animal:
    _is_wild = True

    def move(self):
        if self._is_wild:
            print(f'animal with color {self.color} is moving wildly')
        else:
            print(f'animal with color {self.color} is moving calmly')

    def __init__(self, color):
        self.color = color


class WildAnimal(Animal):
    _is_wild = True
    is_big = True
#
#
# # DRY - don't repeat yourself
#
# class Tr(WildAnimal):
#     food = 'grass'


class HomeAnimal(Animal):
    _is_wild = False

    def move(self):
        super().move()
        print('home animal move')

    def __init__(self, color, name):
        super().__init__(color)
        self.name = name
#
#
# s = Tr('gray')
# s.move()

# print(is_wild)
# print(color)


# public
# protected
# private

# my_animal = WildAnimal("orange")  # создали экземляр класса Animal
# # print(my_animal._is_wild)  # _ перед именем атрибута или метода означает, что его не предполагалось использовать вне класса
#
# print(WildAnimal.is_big)
# print(my_animal.is_big)
# WildAnimal.is_big = False
# print(WildAnimal.is_big)
# print(my_animal.is_big)
# my_animal.name = "some name"
# second_animal = WildAnimal('white')
# for animal in [my_animal, second_animal]:
#     print(animal.name)

# print(second_animal.color)
# print(my_animal.color)
# print(my_animal.is_wild)
# print(Animal.is_wild)
# print(Animal.color)

# my_animal.move()
# white_animal = WildAnimal('white')
# WildAnimal.move(white_animal)
# print(white_animal.color)

# tiger = WildAnimal('orange')
# cat = HomeAnimal('orange', 'nedikiy')
# animals = [tiger, cat]
# for animal in animals:
#     print(type(animal))
#     animal.move()


# class Car:
#     def move(self):
#         print('car moving')
#
#
# class Dog:
#     def move(self):
#         print('dog moving')


# duck typing, утиная типизация - Если что-то выглядит как утка,
# плавает как утка и крякает как утка, то, скорее всего, это утка.
# moving_thing = [Car(), Dog()]
# for thing in moving_thing:
#     print(type(thing))
#     thing.move()


# class SomeClass:
#     data = [1, 2, 3]
#
#
# some_class_object = SomeClass(1, 2)
# print(some_class_object.data)

# class WalkingAnimal:
#     def walk(self):
#         print('walk')
#
#
# class Bird(WalkingAnimal):
#     def fly(self):
#         print('fly')
#
#
# class WaterAnimal:
#     def swimm(self):
#         print('swimm')
#
#
# class Duck(Bird, WaterAnimal):
#     pass


# duck = Duck()
# duck.walk()
# duck.swimm()
# duck.fly()
# MRO - method resolution order, порядок разрешения методов
# print(Duck.__mro__)


from abc import ABC, abstractmethod


class IMovable(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(IMovable):
    def move(self):
        print('car moving')


class Dog(IMovable):
    def move(self):
        print('dog moving')


# moving_thing = [Car(), Dog()]
# for thing in moving_thing:
#     print(type(thing))
#     thing.move()


# dog = Dog()
# dog.make_sound()


# list_ = [1, 2, 3]
# print(len(list_))
# print(list_[1])  # __getitem__
# list_[1] = 100  # __setitem__
# print(list_[1])

# 1 -> 1
# 123 -> 3
class MyInt(int):
    def __len__(self):
        return len(str(self))

    def __getitem__(self, index):  # list_[1]
        if index >= len(self):
            print('error')
            return
        return str(self)[index]


number = MyInt(123)
print(number[0])
print(number[1])
# print(number)
# print(number + 5)
# print(len(number))
# print(len(MyInt("123")))
# print(len(1))



