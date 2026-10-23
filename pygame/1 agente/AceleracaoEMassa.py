import pygame
import random
import math

from agenteMassaEAceleracao import Agente
from obstaculo import Obstaculo

pygame.init()
largura_tela = 1280
altura_tela = 720

screen = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
running = True
pausado = True
dt = 0
fonte = pygame.font.SysFont(None, 24)

r = 10 # Raio do agente
rr = 10 # Raio do obstaculo

def resetar():
    x_inc = random.randint(r, largura_tela - r)
    y_inc = random.randint(50, altura_tela - r)
    p_inicial = pygame.math.Vector2(x_inc, y_inc)
    
    x_f = random.randint(r, largura_tela - r)
    y_f = random.randint(50, altura_tela - r)
    p_final = pygame.math.Vector2(x_f, y_f)
    
    agente = Agente(screen, p_inicial, r, massa=1.0, vel_maxima=150.0)
        
    pos_obs = (p_inicial + p_final) / 2
    obs = Obstaculo(screen, pos_obs, rr)
        
    return agente, p_final, obs, 100.0

perseguidor, ponto_final, obstaculo, speed = resetar()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausado = not pausado
            elif event.key == pygame.K_r:
                screen.fill("White")
                perseguidor, ponto_final, obstaculo, speed = resetar()
            
            elif event.key == pygame.K_1:
                perseguidor.massa = 0.5
            elif event.key == pygame.K_2:
                perseguidor.massa = 1.5
            elif event.key == pygame.K_3:
                perseguidor.massa = 4.0

    if not pausado:
        screen.fill("white")

        perseguidor.atualizar_vetores(ponto_final, [obstaculo])
        perseguidor.move(speed, dt)

        pygame.draw.circle(screen, "Green", (int(ponto_final.x), int(ponto_final.y)), r)

        obstaculo.draw()

        perseguidor.draw()

        dist_atual = perseguidor.posicao.distance_to(ponto_final)

        if dist_atual < 5:
            speed = 0.0
        elif dist_atual < 50:
            speed *= 0.95
            if speed < 20:
                speed = 20

        txt_massa = fonte.render(f"Massa do Agente: {perseguidor.massa:.1f} (Pressione 1, 2 ou 3 para alterar)", True, (0, 0, 0))
        screen.blit(txt_massa, (10, 10))

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 320, 40))
        texto = fonte.render("PAUSADO - Pressione P para iniciar", True, (100, 100, 100))
        screen.blit(texto, (15, 20))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()