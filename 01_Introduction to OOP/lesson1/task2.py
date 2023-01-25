import random


class Toyota:
    color = 'черный'
    price = 11_000_000
    max_speed = 350
    current_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()

car_1.current_speed = random.randint(0, 350)
car_2.current_speed = random.randint(0, 350)
car_3.current_speed = random.randint(0, 350)

print(car_1.current_speed)
print(car_2.current_speed)
print(car_3.current_speed)