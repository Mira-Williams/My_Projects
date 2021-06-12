class Spaceship:
    def __init__(self, color, speed, vulnerable, width, height, image):
        self.color = color
        self.speed = speed
        self.vulnerable = vulnerable
        self.width = width
        self.height = height
        self.image = image

class Flag:
    def __init__(self, number, state, status, width, height, image):
        self.number = number
        self.state = state
        self.status = status
        self.width = width
        self.height = height
        self.image = image
        

red_spaceship = Spaceship('red', 5, False, 40, 55, 'spaceship_red.png')
yellow_spaceship = Spaceship('yellow', 5, False, 40, 55, 'spaceship_yellow.png')

nj_flag_1 = Flag(1, 'nj', 'start', 55, 40, 'nj_flag.png')
nj_flag_2 = Flag(2, 'nj', 'start', 55, 40, 'nj_flag.png')
ky_flag_1 = Flag(1, 'ky', 'start', 55, 40, 'ky_flag.png')
ky_flag_2 = Flag(2, 'ky', 'start', 55, 40, 'ky_flag.png')
