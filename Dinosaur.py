__author__ = 'Laura'

class dinosaur(object):
    def __init__(self, name):
        self.name = name

    def roar(self):
        print "I AM " + self.name.upper() + "!!!"