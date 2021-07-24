import turtle
import winsound

wn = turtle.Screen()  # creating a window in a wn variable
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# here the screen has width of 800 and height of 600 so the center is 0,0 left most is -400 right most is 400 uppermost is 300 and lowermost is -300
wn.tracer(0)  # it helps to update program manually which makes the game faster

# Score
score_a = 0
score_b = 0
# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # it sets the animation speed to maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # this doesn't allow the paddle to draw line(trace mark) which happens by default
paddle_a.goto((-350, 0))  # location of the paddle_a

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # animation speed not the speed of the paddle
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto((350, 0))

# Ball
ball = turtle.Turtle()
ball.speed(0)  # animation speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto((0, 0))
ball.dx = 0.20
ball.dy = -0.20

# Pen
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()  # to hide the pen
pen.goto(0, 260)  # location of score
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()  # to know the y coordinate of the paddle a
    y += 20
    paddle_a.sety(y)  # set the new value of y to the previous value of y


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # to know the y coordinate of the paddle a
    y += 20
    paddle_b.sety(y)  # set the new value of y to the previous value of y


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()  # to listen to the keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border chacking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # snd_async plays the sound in background

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()  # to clear the previsouly written scores
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()  # to clear the previsouly written scores
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # this doesnot let the paddles to go outside of the screen
    if paddle_a.ycor() > 290:
        paddle_a.goto((-350, 290))

    if paddle_a.ycor() < -290:
        paddle_a.goto((-350, -290))

    if paddle_b.ycor() > 290:
        paddle_b.goto((350, 290))

    if paddle_b.ycor() < -290:
        paddle_b.goto((350, -290))

    # Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > - 350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
