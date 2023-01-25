class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = False


mon1 = Monitor()
mon2 = Monitor()
mon3 = Monitor()
mon4 = Monitor()

mon2.freq = 144
mon3.freq = 70

headphone2 = Headphones()
headphone3 = Headphones()

headphone2.micro = True
headphone3.micro = True