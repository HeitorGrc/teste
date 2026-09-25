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

raio = 15

x = random.randint(raio,1280-raio)
y = random.randint(raio,720-raio)
pos = pygame.math.Vector2(x,y)

speed = 200

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
                pos.x = random.randint(raio,1280-raio)
                pos.y = random.randint(raio,720-raio)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                speed *= 2
            if event.button == 3:
                speed /= 2

    if not pausado:

        screen.fill("White")

        pygame.draw.circle(screen,"BLACK",(int(pos.x),int(pos.y)),raio+2)
        pygame.draw.circle(screen,"GRAY",pos,raio)

        mouse_x,mouse_y = pygame.mouse.get_pos()
        mouse = pygame.math.Vector2(mouse_x,mouse_y)

        direcao = mouse - pos
        dist = direcao.length()

        if dist > 0:
            direcao = direcao.normalize()
            pos += direcao * speed * dt
        
        pygame.draw.rect(screen,"white",(0,0 ,largura_tela, 50))

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()