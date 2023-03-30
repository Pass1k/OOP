from abc import ABC, abstractmethod


class MusicMixin:

    def play_music(self):
        print("""
                I see trees of green
                Red roses too
                I see them bloom
                For me and for you
                And I think to myself
                What a wonderful world
                """)


class Transport(ABC):

    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @abstractmethod
    def ride_on_water(self):
        pass

    @abstractmethod
    def ride_on_earth(self):
        pass

    def signal(self):
        print('Сигнал')


class Boat(Transport):

    def ride_on_water(self):
        print('Walking on water')


class Car(Transport):

    def ride_on_earth(self):
        print('Waling on earth')


class Mix(Boat, Car, MusicMixin):
    pass


mix = Mix('Blue', 200)
mix.ride_on_earth()
mix.ride_on_water()
mix.play_music()
print(mix.color)
mix.color = 'Black'
print(mix.color)


