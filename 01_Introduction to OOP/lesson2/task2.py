class Family:
    family_name = 'Тынысбеков'
    current_money: int = 100_000
    have_a_house = False

    def info(self):
        print('Family name: {}\nCurrent money: {}\nHave a house: {}'.format(
            self.family_name,
            self.current_money,
            self.have_a_house
        ))

    def earn(self, money):
        self.current_money += money

    def buy_a_house(self, price, discount=0):
        price -= price * discount / 100

        if price <= self.current_money:
            self.current_money -= price
            self.have_a_house = True
            print('Congrats')
        else:
            print('Do not have enough money')


my_fam = Family()
my_fam.info()

my_fam.earn(1_000_000)
my_fam.info()

my_fam.buy_a_house(600_000)
my_fam.info()


