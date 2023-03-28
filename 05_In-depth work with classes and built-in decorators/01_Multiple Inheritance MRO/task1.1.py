class Robot:
    def __init__(self, model):
        self.model = model

    def operate(self):
        print('Я - Робот')


class FlingRobot(Robot):
    def __init__(self, model, height=0, speed = 0):
        super().__init__(model=model)
        self.height = height
        self.speed = speed

    def takeoff(self):
        print('Влетаю')

    def fly(self):
        print('Лечу')

    def land(self):
        print('Приземляюсь')


class ScoutDrone(FlingRobot):
    def operate(self):
        print('Введу разведку с воздуха')
        self.fly()


class MilitaryRobot(FlingRobot):
    def operate(self):
        print('Защищаю военный обьект с воздуха с помощью оружия')
        self.takeoff()
        self.fly()
        self.land()

robot = Robot('Обычный робот')
robot.operate()

drone = ScoutDrone('Развелывательный дрон', height=100, speed=50)
drone.operate()

militraty_robot = MilitaryRobot('Военный робот', height=200, speed=100)
militraty_robot.operate()
















