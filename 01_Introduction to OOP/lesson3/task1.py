class Toyota:

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent_speed: {}'.format(
            self.color,
            self.price,
            self.max_speed,
            self.current_speed
        ))

    def change_speed(self, speed):
        self.current_speed = speed


car1 = Toyota('Green', 1_000_000, 300, 0)
car1.info()