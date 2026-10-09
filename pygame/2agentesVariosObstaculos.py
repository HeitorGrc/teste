import pygame
import random
import math

from agente import Agente
from obstaculo import Obstaculo

pygame.init()
largura_tela = 1280
altura_tela = 720

screen = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
running = True
pausado = True
dt = 0
fonte = pygame.font.SysFont(None, 20)

r = 10 #Raio do agente
rr = 10 #Raio do obstaculo
qtd_obstaculos = 30

def gerar_obstaculos_aleatorios(qtd, raio, largura, altura):
    lista = []
    for _ in range(qtd):
        x = random.randint(raio, largura - raio)
        y = random.randint(50, altura - raio)
        pos = pygame.math.Vector2(x, y)
        lista.append(Obstaculo(screen, pos, raio))
    return lista

def resetar_cenario():
    #agente 1
    x_inc = random.randint(r, largura_tela - r)
    y_inc = random.randint(50, altura_tela - r)
    p_inicial1 = pygame.math.Vector2(x_inc, y_inc)
    
    x_f = random.randint(r, largura_tela - r)
    y_f = random.randint(50, altura_tela - r)
    p_final1 = pygame.math.Vector2(x_f, y_f)
    
    agente1 = Agente(screen, p_inicial1, r)

    #agente 2
    x_inc2 = random.randint(r, largura_tela - r)
    y_inc2 = random.randint(50, altura_tela - r)
    p_inicial2 = pygame.math.Vector2(x_inc2, y_inc2)

    x_f2 = random.randint(r, largura_tela - r)
    y_f2 = random.randint(50, altura_tela - r)
    p_final2 = pygame.math.Vector2(x_f2, y_f2)

    agente2 = Agente(screen, p_inicial2, r)

    lista_obs = gerar_obstaculos_aleatorios(qtd_obstaculos, rr, largura_tela, altura_tela)

    return agente1, p_final1, 100.0, agente2, p_final2, 100.0, lista_obs

perseguidor, ponto_final, speed, perseguidor2, ponto_final2, speed2, obstaculos = resetar_cenario()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausado = not pausado
            elif event.key == pygame.K_r:
                screen.fill("White")
                    
                perseguidor, ponto_final, speed, perseguidor2, ponto_final2, speed2, obstaculos = resetar_cenario()

    if not pausado:
        screen.fill("white")

        for obs in obstaculos:
            obs.draw()

        perseguidor.atualizar_vetores(ponto_final, obstaculos)
        perseguidor.move(speed, dt)

        pygame.draw.circle(screen, "Green", (int(ponto_final.x), int(ponto_final.y)), r)

        gerar_obstaculos_aleatorios(qtd_obstaculos,rr,largura_tela,altura_tela)

        perseguidor.draw()

        dist_atual = perseguidor.posicao.distance_to(ponto_final)

        if dist_atual < 50:
            speed *= 0.95
            if speed < 20:
                speed = 20
        if dist_atual < 1:
                speed = 0

        perseguidor2.atualizar_vetores(ponto_final2, obstaculos)
        perseguidor2.move(speed2, dt)
        
        pygame.draw.circle(screen, "Green", (int(ponto_final2.x), int(ponto_final2.y)), r)
        
        perseguidor2.draw()


        
        dist_atual2 = perseguidor2.posicao.distance_to(ponto_final2)
        
        if dist_atual2 < 50:
            speed2 *= 0.95
            if speed2 < 20:
                speed2 = 20
        if dist_atual2 < 1:
            speed2 = 0

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()