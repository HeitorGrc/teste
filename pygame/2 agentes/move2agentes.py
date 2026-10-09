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

x_inicio = random.randint(r, largura_tela - r)
y_inicio = random.randint(50, altura_tela - r)
ponto_inicial = pygame.math.Vector2(x_inicio, y_inicio)

x_fim = random.randint(r, largura_tela - r)
y_fim = random.randint(50, altura_tela - r)
ponto_final = pygame.math.Vector2(x_fim, y_fim)

perseguidor = Agente(screen, ponto_inicial, r)

pos_obstaculo = (ponto_inicial + ponto_final) / 2
obstaculo = Obstaculo(screen, pos_obstaculo, rr)

speed = 100.0

x_inicio2 = random.randint(r, largura_tela - r)
y_inicio2 = random.randint(50, altura_tela - r)
ponto_inicial2 = pygame.math.Vector2(x_inicio2, y_inicio2)

x_fim2 = random.randint(r, largura_tela - r)
y_fim2 = random.randint(50, altura_tela - r)
ponto_final2 = pygame.math.Vector2(x_fim2, y_fim2)

perseguidor2 = Agente(screen, ponto_inicial2, r)

pos_obstaculo2 = (ponto_inicial2 + ponto_final2) / 2
obstaculo2 = Obstaculo(screen, pos_obstaculo2, rr)

obstaculos = [
    obstaculo,obstaculo2
]

speed2 = 100.0



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausado = not pausado
            elif event.key == pygame.K_r:
                screen.fill("White")
                    
                x_inc = random.randint(r, largura_tela - r)
                y_inc = random.randint(50, altura_tela - r)
                ponto_inicial = pygame.math.Vector2(x_inc, y_inc)
                
                x_f = random.randint(r, largura_tela - r)
                y_f = random.randint(50, altura_tela - r)
                ponto_final = pygame.math.Vector2(x_f, y_f)
                
                perseguidor = Agente(screen, ponto_inicial, r)
                    
                pos_obs = (ponto_inicial + ponto_final) / 2
                obstaculo = Obstaculo(screen, pos_obs, rr)

                speed = 100.0

                x_inicio2 = random.randint(r, largura_tela - r)
                y_inicio2 = random.randint(50, altura_tela - r)
                ponto_inicial2 = pygame.math.Vector2(x_inicio2, y_inicio2)

                x_fim2 = random.randint(r, largura_tela - r)
                y_fim2 = random.randint(50, altura_tela - r)
                ponto_final2 = pygame.math.Vector2(x_fim2, y_fim2)

                perseguidor2 = Agente(screen, ponto_inicial2, r)

                pos_obstaculo2 = (ponto_inicial2 + ponto_final2) / 2
                obstaculo2 = Obstaculo(screen, pos_obstaculo2, rr)

                obstaculos = [
                    obstaculo,obstaculo2
                ]

                speed2 = 100.0

    if not pausado:
        screen.fill("white")

        perseguidor.atualizar_vetores(ponto_final, obstaculos)
        perseguidor.move(speed, dt)

        pygame.draw.circle(screen, "Green", (int(ponto_final.x), int(ponto_final.y)), r)

        obstaculo.draw()

        perseguidor.draw()

        dist_atual = perseguidor.posicao.distance_to(ponto_final)

        if dist_atual < 50:
            speed *= 0.95
            if speed < 20:
                speed = 20

        perseguidor2.atualizar_vetores(ponto_final2,obstaculos)
        perseguidor2.move(speed2, dt)
        
        pygame.draw.circle(screen, "Green", (int(ponto_final2.x), int(ponto_final2.y)), r)
        
        obstaculo2.draw()
        
        perseguidor2.draw()
        
        dist_atual2 = perseguidor2.posicao.distance_to(ponto_final2)
        
        if dist_atual2 < 50:
            speed2 *= 0.95
            if speed2 < 20:
                speed2 = 20

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()