from turtle import Turtle

class Level_Bar(Turtle):
    def __init__(self):
        super(Level_Bar, self).__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-180,160)
        self.resetScore()

    def resetScore(self):
        self.clear()
        self.write(f"Level: {self.score}",align='center', font=('Arial', 20, 'normal'))

    def winning(self):
        self.score+=1
        self.resetScore()

    def lose(self):
        self.clear()
        self.write(f"You Lose ({self.score})",align='center', font=('Arial', 20, 'normal'))