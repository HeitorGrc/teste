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
fonte = pygame.font.SysFont(None,20)

raio = 20

x = random.randint(raio,1280-raio)
y = random.randint(raio,720-raio)


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
                x = random.randint(raio,1280-raio)
                y = random.randint(raio,720-raio)

    if not pausado:

        pygame.draw.circle(screen,"BLACK",(x,y),raio+2)
        pygame.draw.circle(screen,"GRAY",(x,y),raio)

        x += random.randint(-10,10)
        y += random.randint(-10,10)

        pygame.draw.rect(screen,"white",(0,0 ,largura_tela, 50))

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()