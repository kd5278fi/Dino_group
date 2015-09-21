__author__ = 'Laura'

from Weather import weather

class dinosaur(object):
    def __init__(self, status = "Fine"):
        self.status = status

    def roar(self):

        print("Everybody do the dinosaur!")

        print("Blrblrblrblr!")

    def react(self, weather_object):
        if weather_object.stormy == True:
            print("I am wet.")
        elif weather_object.blizzard == True:
            print("I am cold.")
        elif weather_object.sunny == True:
            print("I am warm.")
        elif weather_object.meteor_shower == True:
            print("I am dead.")