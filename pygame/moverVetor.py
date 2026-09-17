# Example file showing a circle moving on screen
import pygame
import random
import math

# pygame setup
pygame.init()
largura_tela = 1280
altura_tela = 720
screen = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
running = True
dt = 0

bola_og = pygame.image.load("circulo_preto.png")
x_og = pygame.image.load("x_vermelho.png")

novo_tam = [50,50]

bola = pygame.transform.scale(bola_og,novo_tam)
x = pygame.transform.scale(x_og,novo_tam)

altura_bola = bola.get_height()
largura_bola = bola.get_width()

altura_x = x.get_height()
largura_x = x.get_width()

bolas_posicoes = []

for _ in range(2):
    x_aleatorio = random.randint(0, largura_tela-largura_bola)
    y_aleatorio = random.randint(0,altura_tela-altura_bola)
    bolas_posicoes.append(pygame.math.Vector2(x_aleatorio,y_aleatorio))

x_rand = random.randint(0,largura_tela-largura_x)
y_rand = random.randint(0, altura_tela-altura_x)
posicao_x = pygame.math.Vector2(x_rand,y_rand)

velocidade_x = 100

distancia = []

for i in range(2):
    distancia_x = abs(bolas_posicoes[i].x - posicao_x.x)
    distancia_y = abs(bolas_posicoes[i].y - posicao_x.y)
    distancia.append(math.sqrt((distancia_x**2)+(distancia_y**2)))

menor_distancia = distancia[0]
vet_menor_dist = bolas_posicoes[0]
if distancia[1] < menor_distancia:
    menor_distancia = distancia[1]
    vet_menor_dist = bolas_posicoes[1]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    direcao = vet_menor_dist - posicao_x
    dist_atual = direcao.length()

    if dist_atual > 1:
        direcao = direcao.normalize()
        posicao_x += direcao * velocidade_x * dt

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    for posicao in bolas_posicoes:
        screen.blit(bola,(posicao.x,posicao.y))

    screen.blit(x,(posicao_x.x,posicao_x.y))



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()