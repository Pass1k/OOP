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

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class Car(Transport):

    def ride_on_earth(self):
        print('Едем по земле')


class Boat(Transport):

    def ride_on_water(self):
        print('Едем по воде')


class Amphibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amphibian()
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
