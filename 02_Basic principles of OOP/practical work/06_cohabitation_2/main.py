import random


class House:
    many = 100
    food = 50
    cat_food = 30
    dirt = 0
    fur_coat = 0
    earned = 0
    food_eaten = 0
    cat_ate = 0

    def __init__(self, family):
        self.family = family

    def pollution(self):
        House.dirt += 5

    def life(self):
        for i_resident in self.family:
            if House.dirt >= 90 and not isinstance(i_resident, Cat):
                i_resident.happiness -= 10

            if isinstance(i_resident, Cat) and House.cat_food >= 20 <= i_resident.satiety:
                cat.eat()
                print('Кот поел')
                House.cat_ate += 10

            elif isinstance(i_resident, Cat):
                if random.randint(1, 2) == 1:
                    House.dirt += 5
                    print('Кот подрал обои')
                else:
                    cat.satiety -= 10
                    print('Кот спит')
            elif House.food >= 60 and i_resident.satiety <= 30:
                i_resident.eat()
                print(i_resident.name, 'поел')
                House.food_eaten += 30

            elif isinstance(i_resident, Husband):
                if House.many <= 150:
                    Husband.work_day()
                    print('Экстренная работа')
                    House.earned += 150
                elif Husband.happiness <= 50:
                    Husband.game()
                    print('Расслабляется')
                elif Husband.happiness <= 70:
                    Husband.petting_cat()
                    print('Гладит кота')
                else:
                    Husband.work_day()
                    print('Обычная работа')
                    House.earned += 150

            elif isinstance(i_resident, Wife):
                if House.food <=60 and House.many > 100:
                    Wife.buy_food()

                elif House.cat_food <= 20:
                    Wife.buy_cat_food()

                elif House.dirt >= 50:
                    Wife.cleaning()
                    print('Приборка')

                elif Wife.happiness <= 70:
                    Wife.petting_cat()

                elif House.many > 450:
                    Wife.purchase()
                    print('Покупка шуба')
                    House.fur_coat += 1
                else:
                    Wife.petting_cat()
                    print('Гладит кота')


class Residents:
    def __init__(self, name=None, satiety=None, happiness=None):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        self.satiety += 30
        House.food -= 30


class Husband(Residents):
    def __init__(self, name, satiety=30, happiness=100, work=150):
        super().__init__(name, satiety, happiness)
        self.work = work

    def work_day(self):
        House.many += self.work
        self.satiety -= 10
        print('Работа')

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def game(self):
        self.happiness += 20
        self.satiety -= 10


class Wife(Residents):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def buy_food(self):
        House.many -= 100
        House.food += 100

    def buy_cat_food(self):
        House.many -= 50
        House.cat_food += 50

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def purchase(self):
        House.many -= 350
        self.happiness += 60
        self.satiety -= 10

    def cleaning(self):
        House.dirt -= 100
        self.satiety -= 10


class Cat(Residents):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10

    def shitting(self):
        House.dirt += 5


def life_dead(family):
    for i_elem in family:
        if i_elem.satiety <= 0:
            print('Кто-то умер от голода')
            return True

        elif i_elem.happiness == 0 and not isinstance(i_elem, Cat):
            print('Кто-то в дипрессии')
            return True

        else:
            return True


husband = Husband('Парасат')
wife = Wife('Somebody')
cat = Cat('Панда')
family_list = [husband, wife, cat]
house = House(family_list)


for i_day in range(365):
    print(f'День {i_day}')
    house.pollution()
    if life_dead(family_list):
        print('Провал')
    elif i_day == 365:
        print(f'Все живы')
        break
    else:
        house.life()

print(f'\nЗа год:\nКупленно шуб: {House.fur_coat}\nЗаработано: {House.earned}\nСьендено: {House.food_eaten}\nКот сьел: {House.cat_ate}')
