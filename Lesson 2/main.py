import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

GRAVITY = 2000.0 # pixels per second squared

class Ball:
    def __init__(self, initial_x, initial_y, CLR, radius):
        self.color = CLR
        self.x = initial_x
        self.y = initial_y
        self.vx = 20
        self.vy = 0
        self.radius = radius

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

ball = Ball(50, 100, (randint(0,255), randint(0,255), randint(0,255)), randint(20, 50))
ball1 = Ball(200, 100, (randint(0,255), randint(0,255), randint(0,255)), randint(20, 50))
ball2 = Ball(350, 100, (randint(0,255), randint(0,255), randint(0,255)), randint(20, 50))

def draw():
    screen.clear()
    ball.draw()
    ball1.draw()
    ball2.draw()

def update(dt):
    #a)
    #Constant acceleration formula downward
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    #detect and handle bounce
    if ball.y > HEIGHT - ball.radius: # we've bounced
        ball.y = HEIGHT - ball.radius # fix the position
        ball.vy = -ball.vy * 0.9 # inelastic collision

    ball.x += ball.vx * dt
    if ball.x > WIDTH or ball.x < ball.radius:
        ball.vx = -ball.vx

    #b)
    #Constant acceleration formula downward
    uy = ball1.vy
    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt

    #detect and handle bounce
    if ball1.y > HEIGHT - ball1.radius: # we've bounced
        ball1.y = HEIGHT - ball1.radius # fix the position
        ball1.vy = -ball1.vy * 0.9 # inelastic collision

    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500
        ball1.vy = -500

pgzrun.go()
