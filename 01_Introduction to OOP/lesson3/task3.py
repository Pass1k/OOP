class Potato:
    states = {
        0: 'Отсутсвтует',
        1: 'Росток',
        2: 'Зеленая',
        3: 'Зрелая'
    }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i in self.potatoes:
            i.grow()

    def are_all_right(self):
        for i in self.potatoes:
            if not i.is_ripe():
                print('Картошка еще не созрела')
                break
        else:
            print('Вся картошка созрела можно их собрать!')


my_garden = PotatoGarden(5)

for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_right()
