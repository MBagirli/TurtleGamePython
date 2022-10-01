from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0,y=-180)
        self.setheading(90)

    def Up(self):
        self.setheading(90)
        self.forward(20)

    def Down(self):
        self.setheading(270)
        self.forward(20)

    def Left(self):
        self.setheading(180)
        self.forward(20)

    def Right(self):
        self.setheading(0)
        self.forward(20)

    def reset_coordinate(self):
        self.goto(x=0,y=-180)