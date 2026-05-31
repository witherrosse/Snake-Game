from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20,"normal")


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        with open("data.txt", "r") as s:
            self.high_score = int(s.read())
        self.penup()
        self.color("white")
        self.goto ( 0 , 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):

        self.write(f" Score: {self.score} HighScore : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset (self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def game_over(self):

        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()



