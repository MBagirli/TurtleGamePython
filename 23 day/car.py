from turtle import Turtle
import random

COLORS = ['red','green','blue','orange','yellow','violet','indigo']

class Car():
    def __init__(self):
        self.speed = 5
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(320,random.randint(-150,150))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def add_speed(self):
        self.speed+=2