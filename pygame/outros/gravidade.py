# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

x = 640
y = 360

vel_x = 0.0
vel_y = 0.0

aceleracao = 1.0
velocidade_maxima = 8.0

atrito = 0.95
atritoB = 0.6

gravidade = 0.1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    speed = [vel_x,vel_y]

    posrect = pygame.draw.circle(screen, "red", [int(x),int(y)], 40)

    posrect = posrect.move(speed)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        vel_y -= aceleracao
    if keys[pygame.K_s]:
        vel_y += aceleracao
    if keys[pygame.K_a]:
        vel_x -= aceleracao
    if keys[pygame.K_d]:
        vel_x += aceleracao

    if not keys[pygame.K_d] and not keys[pygame.K_a]:
        vel_x *= atrito
    if not keys[pygame.K_w] and not keys[pygame.K_s]:
        vel_y *= atrito

    if vel_x > velocidade_maxima:
        vel_x = velocidade_maxima
    if vel_x < -velocidade_maxima:
        vel_x = -velocidade_maxima
    if vel_y > velocidade_maxima:
        vel_y = velocidade_maxima
    if vel_y < -velocidade_maxima:
        vel_y = -velocidade_maxima

    x += vel_x
    y += vel_y

    if posrect.top < 0:
        vel_y = -vel_y
        y = 40
    if posrect.bottom > 720:
        vel_y = -vel_y
        y = 720 - 40
    if posrect.left < 0:
        vel_x = -vel_x
        x = 40
    if posrect.right > 1280:
        vel_x = -vel_x
        x = 1280 - 40

    vel_y += gravidade

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()