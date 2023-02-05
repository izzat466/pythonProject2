# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.



class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10
    def shopping_for_cat(self):
        print("кто то купил еды для кота")
        self.house.cat_food += 50
        self.house.money -= 30

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif self.house.cat_food < 10:
            self.shopping_for_cat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0


    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, корм кота{}'.format(
            self.food, self.money, self.cat_food)


class Cat:


    def __init__(self, name):
        self.name = name
        self.catfullness = 0
        self.house = None
    def __str__(self):
        return ('я кошка')

    def play(self):
        self.catfullness -= 20

    def sleep(self):
        self.catfullness -= 10

    def eat(self):
        self.catfullness += 20
        self.house.cat_food -= 20

    def act(self):
        if self.catfullness < 10:
            print("кот покушал")
            self.eat()
        elif self.catfullness > 10:
            print("кот поиграл")
            self.play()
        elif self.catfullness > 20:
            print('кот поспал')
            self.sleep()
    def go_to_the_house(self, house):
        self.house = house
        print('{} Вьехал в дом'.format(self.name))






citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
    Cat(name='tom')
]


y_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=y_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()

    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(y_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.