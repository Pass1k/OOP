import random


class Card:

    def __init__(self, other):
        self.suit = other[0][1]
        self.rang = other[0][0]
        self.value = other[1]

    def __repr__(self):
        return f"{self.suit} {self.rang}"

    def give_point(self):
        return self.value

    def give_rang(self):
        return self.rang


class Bot:
    list_card = []
    point = 0

    def __init__(self, other):
        self.name = 'Бот'
        self.other = other
        self.get_shuffle()

    def __repr__(self):
        return f"{self.name}: {self.list_card}"

    def get_shuffle(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.list_card.append(self.other.give_out_playing_card())
        for card in self.list_card:
            self.point += card.give_point()

    def bot_game(self):
        while self.point < 17:
            self.list_card.append(self.other.give_out_playing_card())
            self.point += self.list_card[-1].give_point()
            self.give_point()

    def give_point(self):
        flag = False
        temp_count = 0
        while self.point > 21:
            if flag and temp_count != 0:
                self.point -= 10
                break
            if flag:
                break
            for card in self.list_card:
                if card.give_rang() == 'Туз':
                    temp_count += 1
            if temp_count > 1:
                self.point -= ((temp_count - 1) * 10)
            flag = True

        return self.point


class Player:
    list_card = []
    point = 0

    def __init__(self, other):
        self.name = 'Вы'
        self.other = other
        self.get_shuffle()

    def __repr__(self):
        return f'{self.name}: {self.list_card}'

    def get_shuffle(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.list_card.append(self.other.give_out_playing_card())
        for card in self.list_card:
            self.point += card.give_point()

    def get_game_card(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.point += self.list_card[-1].give_point()

    def give_point(self):
        flag = False
        temp_count = 0
        while self.point > 21:
            if flag and temp_count != 0:
                self.point -= 10
                break
            if flag:
                break
            for card in self.list_card:
                if card.give_rang() == 'Туз':
                    temp_count += 1
            if temp_count > 1:
                self.point -= ((temp_count - 1) * 10)
            flag = True

        return self.point


class Deck:
    deck_cards = {}








