import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(0, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(383, 0)


def paddle_a_down():
	x = paddle_a.xcor()
	x -= 20
	paddle_a.setx(x)

def paddle_a_up():
	x = paddle_a.xcor()
	x += 20
	paddle_a.setx(x)

def paddle_a_jump():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_jumpw():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "d")
wn.onkeypress(paddle_a_down, "a")
wn.onkeypress(paddle_a_jump, "w")
wn.onkeypress(paddle_a_jumpw, "s")

while True:
    wn.update()


    if paddle_a.ycor() > 290:
        paddle_a.sety(290)

    if paddle_a.ycor() < -290:
        paddle_a.sety(-290)
        paddle_a.dy *= -1

    if paddle_a.xcor() > 390:
        paddle_a.goto(0, 0)
        paddle_a.dx *= -1

    if paddle_a.xcor() < -390:
        paddle_a.goto(0, 0)
        paddle_a.dx *= -1