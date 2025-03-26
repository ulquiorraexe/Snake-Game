from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(x= 0, y= 270)
        self.update()

    def update(self):
        self.write(f"Score = {self.score} High Score: {self.high_score}", align="center")


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update()

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

