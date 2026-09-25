import pygame
import random
import math

from circulo import Circulo

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

for i in range(3):
    x_aleatorio = random.randint(0, largura_tela-raio)
    y_aleatorio = random.randint(0,altura_tela-raio)
    vetor_pos = pygame.math.Vector2(x_aleatorio, y_aleatorio)

    alvo = Circulo(screen,"Green",vetor_pos,raio)

    posicoes.append(alvo)

x_rand = random.randint(0,largura_tela-raio)
y_rand = random.randint(0, altura_tela-raio)
posicao_x = pygame.math.Vector2(x_rand,y_rand)

perseguidor = Circulo(screen,"Red",posicao_x,raio)

speed = 0.0

distancia = []

distancia_0 = posicao_x.distance_to(posicoes[0].posicao)
distancia_1 = posicao_x.distance_to(posicoes[1].posicao)
distancia_2 = posicao_x.distance_to(posicoes[2].posicao)

if distancia_0 < distancia_1 and distancia_0 < distancia_2:
    vet_menor_dist = posicoes[0].posicao
elif distancia_1 < distancia_0 and distancia_1 < distancia_2:
    vet_menor_dist = posicoes[1].posicao
else:
    vet_menor_dist = posicoes[2].posicao

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
                for i in range(3):
                    x_aleatorio = random.randint(0, largura_tela-raio)
                    y_aleatorio = random.randint(0,altura_tela-raio)
                    vetor_pos = pygame.math.Vector2(x_aleatorio, y_aleatorio)

                    alvo = Circulo(screen,"Green",vetor_pos,raio)

                    posicoes.append(alvo)

                x_rand = random.randint(0,largura_tela-raio)
                y_rand = random.randint(0, altura_tela-raio)
                posicao_x = pygame.math.Vector2(x_rand,y_rand)

                perseguidor = Circulo(screen,"Red",posicao_x,raio)

                speed = 0.0

                distancia = []

                distancia_0 = posicao_x.distance_to(posicoes[0].posicao)
                distancia_1 = posicao_x.distance_to(posicoes[1].posicao)
                distancia_2 = posicao_x.distance_to(posicoes[2].posicao)

                if distancia_0 < distancia_1 and distancia_0 < distancia_2:
                    vet_menor_dist = posicoes[0].posicao
                elif distancia_1 < distancia_0 and distancia_1 < distancia_2:
                    vet_menor_dist = posicoes[1].posicao
                else:
                    vet_menor_dist = posicoes[2].posicao
                
                speed = 0.0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                mouse = pygame.math.Vector2(mouse_x,mouse_y)
                speed = 100.0
                distancia_0 = mouse.distance_to(posicoes[0].posicao)
                distancia_1 = mouse.distance_to(posicoes[1].posicao)
                distancia_2 = mouse.distance_to(posicoes[2].posicao)

                if distancia_0 < distancia_1 and distancia_0 < distancia_2:
                    vet_menor_dist = posicoes[0].posicao
                elif distancia_1 < distancia_0 and distancia_1 < distancia_2:
                    vet_menor_dist = posicoes[1].posicao
                else:
                    vet_menor_dist = posicoes[2].posicao
        
    if not pausado:

        screen.fill("white")

        for i in range (3):
            posicoes[i].draw()

        perseguidor.draw()

        direcao = vet_menor_dist - perseguidor.posicao
        dist_atual = direcao.length()

        if dist_atual > 1:
            direcao = direcao.normalize()
            perseguidor.move(direcao * speed * dt)

        if dist_atual < 50:
            speed *= 0.95
            if speed < 20:
                speed = 20    

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