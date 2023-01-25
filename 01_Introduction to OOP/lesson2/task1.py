class Toyota:
    color = 'черный'
    price = 11_000_000
    max_speed = 350
    current_speed = 0

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent_speed: {}'.format(
            self.color,
            self.price,
            self.max_speed,
            self.current_speed
        ))

    def change_speed(self, speed):
        self.current_speed = speed


car_1 = Toyota()
car_1.info()
car_1.change_speed(123)
print(car_1.current_speed)
car_1.info()