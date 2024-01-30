
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import time

class CarManager():

    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        random_num = random.randint(1,6)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(300,340), random.randint(-250,250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT