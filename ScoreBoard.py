from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0

        ####Read the saved high score from file ###

        with open("data.txt", "r") as s:
            self.high_score = int(s.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)   ### Place at top center of screen ###
        self.hideturtle()
        self.update_scoreboard()

    ###Show current score and high score on screen ###

    def update_scoreboard(self):

        self.write(f" Score: {self.score} HighScore : {self.high_score}", align=ALIGNMENT, font=FONT)

    ### Reset score for new game, save high score if needed ###

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

            ## Save new high score to file ##

            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

    ## Show game over message in the center ##

    def game_over(self):

        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    ### Add one point to score and update display ###

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()




