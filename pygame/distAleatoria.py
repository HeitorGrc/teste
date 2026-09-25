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
pausado = True
dt = 0

cor = (0,0,0)
raio = 10

fonte = pygame.font.SysFont(None,20)

screen.fill("white")

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

    if not pausado:

        x = random.randint(raio, largura_tela - raio)
        y = int(altura_tela / 2)

        diametro = raio * 2
        screen_aux = pygame.Surface((diametro, diametro), pygame.SRCALPHA)

        #13/255
        screen_aux.set_alpha(26)

        pygame.draw.circle(screen_aux,cor,(raio,raio),raio)

        screen.blit(screen_aux,(x-raio,y-raio))

        pygame.draw.rect(screen,"white",(0,0 ,largura_tela, 50))

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()