import sys, pygame, time
pygame.init()

size = width, height = 1728, 972
speed = [1,1]
black = 0,0,0

sped = [2,2]

i = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

ba = pygame.image.load("intro_ball.gif")
barect = ba.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    barect = barect.move(sped)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if barect.left < 0 or barect.right > width:
        sped[0] = -sped[0]
    if barect.top < 0 or barect.bottom > height:
        sped[1] = -sped[1]

    if i > 5 and (barect.left == ballrect.right or barect.right == ballrect.left):
        sped[0] = -sped[0]
        speed[0] = -speed[0]
    if i > 5 and (barect.top == ballrect.bottom or barect.bottom == ballrect.top):
        sped[1] = -sped[1]
        speed[1] = -speed[1]

    i = i + 1

    screen.fill(black)
    screen.blit(ball,ballrect)
    screen.blit(ba,barect)
    pygame.display.flip()