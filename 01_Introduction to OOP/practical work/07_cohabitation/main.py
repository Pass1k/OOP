import random


class Human:
    def __init__(self, name, satiety=50, food=50, money=0):
        self.name = name
        self.satiety = satiety
        self.food = food
        self.money = money

    def day(self, action):
        if self.satiety < 20 and self.food >= 10:
            self.satiety += 10
            self.food -= 10
        elif self.food < 10 and self.money > 0:
            self.food += 20
            self.money -= 10
        elif action == 1:
            self.money += 50
            print(f'{self.name} is working')
        elif action == 2:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} is eating')
        else:
            self.satiety -= 10
            print(f'{self.name} is playing')


class Result:
    def __init__(self, man_1, man_2):
        self.man_1 = man_1
        self.man_2 = man_2

    def life_death(self):
        if self.man_1.satiety == 0 or self.man_2.satiety == 0:
            return True, print('Кто-то умер от голода')


man1 = Human('Артём')
man2 = Human('Александр')

result = Result(man1, man2)
count_day = 0

while True:
    count_day += 1
    if count_day == 365:
        print('Эксперимент удался, все выжали.')
        break
    elif result.life_death():
        break
    else:
        r = random.randint(1, 6)
        man1.day(r)
        man2.day(r)

print(count_day)









