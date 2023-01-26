import random


class Warrior:
    def __init__(self, name,health_poit):
        self.name = name
        self.health_poit = health_poit

    def hit(self):
        res = random.randint(1, 2)
        if res == 1:
            self.health_poit -= 20
        else:
            print('Miss shot')


warrior_1 = Warrior('Godfrey, The First Elden Lord', 100)
warrior_2 = Warrior('Malenia, Blade of Miquella', 100)

while True:
    question = int(input(f'Who is hitting?\n1. {warrior_1.name}\n2. {warrior_2.name}\n'))

    if question == 1:
        print(f'{warrior_1.name} is hitting {warrior_2.name}')
        warrior_2.hit()
        print(f'{warrior_2.name} left {warrior_2.health_poit} health_poit')
    elif question == 2:
        print(f'{warrior_2.name} is hitting {warrior_1.name}')
        warrior_1.hit()
        print(f'{warrior_1.name} left {warrior_1.health_poit} health_poit')

    if warrior_1.health_poit <= 0:
        print(f'Fighting is over! {warrior_2.name} won!')
        break
    elif warrior_2.health_poit <= 0:
        print(f'Fighting is over! {warrior_1.name} won!')
        break

    print()

