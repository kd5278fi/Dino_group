__author__ = 'Laura'

from random import randint
class weather(object):

    def __init__(self, stormy = False, blizzard = False, sunny = False, meteor_shower = False):
        self.stormy = stormy
        self.blizzard = blizzard
        self.sunny = sunny
        self.meteor_shower = meteor_shower

    def random_weather(self):
        self.reset()
        counter = randint(1,4)
        if counter == 1:
            self.stormy = True
        elif counter == 2:
            self.blizzard = True
        elif counter == 3:
            self.sunny = True
        elif counter == 4:
            self.meteor_shower = True

    def reset(self):
        self.stormy = False
        self.blizzard = False
        self.sunny = False
        self.meteor_shower = False

    def weatherman(self):
        if self.stormy == True:
            print("It's a dreary, stormy day.")
        elif self.blizzard == True:
            print("It's a cold, snowy day.")
        elif self.sunny == True:
            print("It's a beautiful, sunny day.")
        elif self.meteor_shower == True:
            print("It's the end of the world.")
        else:
            print("It's unremarkable today.")