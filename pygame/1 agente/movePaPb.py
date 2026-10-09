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
pausado = True
dt = 0
fonte = pygame.font.SysFont(None,20)

raio = 10

posicoes = []

for i in range(2):
    x_aleatorio = random.randint(0, largura_tela-raio)
    y_aleatorio = random.randint(0,altura_tela-raio)
    posicoes.append(pygame.math.Vector2(x_aleatorio, y_aleatorio))

x_rand = random.randint(0,largura_tela-raio)
y_rand = random.randint(0, altura_tela-raio)
posicao_x = pygame.math.Vector2(x_rand,y_rand)

speed = 100.0

distancia = []

distancia_0 = posicao_x.distance_to(posicoes[0])
distancia_1 = posicao_x.distance_to(posicoes[1])

if distancia_0 < distancia_1:
    vet_menor_dist = posicoes[0]
    vet_maior_dist = posicoes[1]
else:
    vet_menor_dist = posicoes[1]
    vet_maior_dist = posicoes[0]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausado = not pausado
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill("White")
                posicoes = []
                for i in range(2):
                    x_aleatorio = random.randint(raio, largura_tela - raio)
                    y_aleatorio = random.randint(50, altura_tela - raio)
                    posicoes.append(pygame.math.Vector2(x_aleatorio, y_aleatorio))
                
                x_rand = random.randint(raio, largura_tela - raio)
                y_rand = random.randint(50, altura_tela - raio)
                posicao_x = pygame.math.Vector2(x_rand, y_rand)
                
                speed = 100.0
                
                distancia_0 = posicao_x.distance_to(posicoes[0])
                distancia_1 = posicao_x.distance_to(posicoes[1])
                if distancia_0 < distancia_1:
                    vet_menor_dist = posicoes[0]
                    vet_maior_dist = posicoes[1]
                else:
                    vet_menor_dist = posicoes[1]
                    vet_maior_dist = posicoes[0]
        
    if not pausado:

        screen.fill("white")

        for i in range (2):
            pygame.draw.circle(screen,"Green", (posicoes[i]),raio)

        pygame.draw.circle(screen,"Red", (posicao_x),raio)

        direcao = vet_menor_dist - posicao_x
        dist_atual = direcao.length()

        if dist_atual > 1:
            direcao = direcao.normalize()
            posicao_x += direcao * speed * dt

        if dist_atual < 50:
            speed *= 0.95
        if speed < 10:
            speed = 20

        if dist_atual < 1:
            vet_menor_dist = vet_maior_dist
            speed = 100.0

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()