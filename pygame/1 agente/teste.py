import sys, pygame
pygame.init()

size = width, height = 1280, 720
speed = [1.0, 1.0]
black = 0, 0, 0

desaceleracao = 0.99
aceleracao = 1.1

vel_max = 8.0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        speed[0] *= aceleracao
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        speed[1] *= aceleracao
    if speed[0] > vel_max:
        speed[0] = vel_max
    if speed[1] > vel_max:
         speed[1] = vel_max

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()