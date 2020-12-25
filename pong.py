# game of Pong

# import
import turtle

# screen to play
wn = turtle.Screen()
wn.title("Bhagya\'s first program")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# game code
# player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("white")
player1.penup()
player1.goto(-350, 0)

# player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("white")
player2.penup()
player2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# scoreboard
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player 1: {score1} Player 2: {score2}", align = "center", font=("Courier", 24, "normal"))

# game functions


def player1_up():  # player 1 up
    y = player1.ycor()
    y += 20
    player1.sety(y)


def player1_down():  # player 1 down
    y = player1.ycor()
    y -= 20
    player1.sety(y)


def player2_up():  # player 2 up
    y = player2.ycor()
    y += 20
    player2.sety(y)


def player2_down():  # player 2 down
    y = player2.ycor()
    y -= 20
    player2.sety(y)


# keyboard binding
wn.listen()  # this checks what key was clicked
# runs the specified fucntion when key is clicked
wn.onkeypress(player1_up, "w")  # 1 up
wn.onkeypress(player1_down, "s")  # 1 down
wn.onkeypress(player2_up, "Up")  # 2 up
wn.onkeypress(player2_down, "Down")  # 2 down


# game loop
while True:
    wn.update()

    # ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # broder chekcing
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player 2: {score2}", align = "center", font=("Courier", 24, "normal"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player 2: {score2}", align = "center", font=("Courier", 24, "normal"))


    # paddle intersection check
    # player 1 (leftside)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > player1.ycor() - 40 and ball.ycor() < player1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
    
    # player 2 (rightside)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() > player2.ycor() - 40 and ball.ycor() < player2.ycor() + 40):
        ball.setx(340)
        ball.dx *= -1
