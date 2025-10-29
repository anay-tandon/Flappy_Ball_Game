import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)

CLR = R, G, B #Create a color using random RGB values (CLR is a tuple)
#Blue = (0, 128, 255)

GRAVITY = 2000.0 # pixels per second squared

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 20
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50, 100)
ball1 = Ball(200, 100)

def draw():
    screen.clear()
    ball.draw()
    ball1.draw()

def update(dt):
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

pgzrun.go()
