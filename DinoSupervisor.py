__author__ = 'Laura'

from Dinosaur import dinosaur
from Weather import weather

def main():
    new_day = weather()
    new_day.random_weather()
    new_day.weatherman()

    t_rex=dinosaur()
    velociraptor=dinosaur()
    t_rex.react(new_day)
    t_rex.roar()
    velociraptor.react(new_day)
    velociraptor.roar()

main()

