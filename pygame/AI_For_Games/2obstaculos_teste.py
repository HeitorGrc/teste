import pygame
import random
import math

from classes.agente import Agente
from classes.obstaculo import Obstaculo
from classes.arrive import Arrive
from classes.obstacleavoidance import ObstacleAvoidance
from classes.lookwhereyouregoing import LookWhereYoureGoing
from classes.wander import Wander
from classes.steering import SteeringOutput

pygame.init()
largura_tela = 1280
altura_tela = 720

screen = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
running = True
pausado = False
dt = 0
fonte = pygame.font.SysFont(None, 24)

r = 10   # Raio do agente
rr = 50  # Raio do obstáculo

modo = 'ALVO'

def resetar():
    x_inc = random.randint(r, largura_tela - r)
    y_inc = random.randint(50, altura_tela - r)
    p_inicial = pygame.math.Vector2(x_inc, y_inc)
    
    x_f = random.randint(r, largura_tela - r)
    y_f = random.randint(50, altura_tela - r)
    p_final = pygame.math.Vector2(x_f, y_f)
    
    agente = Agente(screen, p_inicial, r, vel_maxima=150.0, acel_maxima=300.0)
        
    pos_obs1 = p_inicial + (p_final - p_inicial) * 0.33
    pos_obs2 = p_inicial + (p_final - p_inicial) * 0.66

    lista_obs = [
        Obstaculo(screen, pos_obs1, rr),
        Obstaculo(screen, pos_obs2, rr)
    ]
        
    return agente, p_final, lista_obs

agente, ponto_final, obstaculos = resetar()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausado = not pausado
            elif event.key == pygame.K_r:
                agente, ponto_final, obstaculos = resetar()
            elif event.key == pygame.K_1:
                modo = 'ALVO'
            elif event.key == pygame.K_2:
                modo = 'WANDER'

    if not pausado:
        screen.fill("white")

        steering_final = SteeringOutput()

        comportamento_desvio = ObstacleAvoidance(agente, obstaculos, distancia_lookahead=80, distancia_evitar=40)
        steering_desvio = comportamento_desvio.get_steering()

        if modo == 'ALVO':
            comportamento_chegada = Arrive(agente, ponto_final, raio_alvo=5, raio_desaceleracao=120)
            steering_chegada = comportamento_chegada.get_steering()

            if steering_desvio is not None and steering_desvio.linear.length() > 0:
                steering_final.linear = steering_desvio.linear * 0.85 + steering_chegada.linear * 0.15
            elif steering_chegada is not None:
                steering_final.linear = steering_chegada.linear

            steering_olhar = LookWhereYoureGoing(agente).get_steering()
            if steering_olhar is not None:
                steering_final.angular = steering_olhar.angular

        elif modo == 'WANDER':
            comportamento_wander = Wander(agente, wander_offset=80, wander_radius=40, wander_rate=0.4)
            steering_wander = comportamento_wander.get_steering()

            if steering_desvio is not None and steering_desvio.linear.length() > 0:
                steering_final.linear = steering_desvio.linear
                steering_olhar = LookWhereYoureGoing(agente).get_steering()
                if steering_olhar is not None:
                    steering_final.angular = steering_olhar.angular
            elif steering_wander is not None:
                steering_final.linear = steering_wander.linear
                steering_final.angular = steering_wander.angular

        if steering_final.linear.length() > agente.acel_maxima:
            steering_final.linear = steering_final.linear.normalize() * agente.acel_maxima

        agente.update(steering_final, dt)

        if modo == 'ALVO':
            pygame.draw.circle(screen, "Green", (int(ponto_final.x), int(ponto_final.y)), r)

        for obs in obstaculos:
            obs.draw()

        agente.draw()

        txt_info = fonte.render(f"Modo: {modo} | [1] Ir ao Alvo  [2] Wander  [R] Reset  [P] Pausa", True, (0, 0, 0))
        screen.blit(txt_info, (10, 10))

    else:
        pygame.draw.rect(screen, "grey", (10, 10, 300, 40))
        texto = fonte.render("PAUSADO - Pressione P", True, (100, 100, 100))
        screen.blit(texto, (15, 15))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()