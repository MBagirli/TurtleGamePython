from turtle import Screen
from player import Player
from levelbar import Level_Bar
from car import Car
import time

#Screen
screen = Screen()
screen.setup(width=600,height=400)
screen.tracer(0)
#Player
player = Player()

#Level Bar
level_bar = Level_Bar()

#car
car = Car()


screen.listen()
screen.onkey(fun=player.Up,key="Up")
screen.onkey(fun=player.Down,key="Down")
screen.onkey(fun=player.Left,key="Left")
screen.onkey(fun=player.Right,key="Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if player.ycor() > 200:
        player.reset_coordinate()
        level_bar.winning()
        car.add_speed()

    for item in car.cars:
        if player.distance(item) < 20:
            game_is_on = False
            level_bar.lose()

screen.exitonclick()