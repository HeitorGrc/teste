import pygame
from classes.steering import SteeringOutput

class Arrive:
    def __init__(self, agente, alvo_posicao, raio_alvo=5, raio_desaceleracao=100, tempo_para_alvo=0.1):
        self.agente = agente
        self.alvo_posicao = alvo_posicao
        self.raio_alvo = raio_alvo
        self.raio_desaceleracao = raio_desaceleracao
        self.tempo_para_alvo = tempo_para_alvo

    def get_steering(self):
        steering = SteeringOutput()
        direcao = self.alvo_posicao - self.agente.posicao
        distancia = direcao.length()

        if distancia < self.raio_alvo:
            self.agente.velocidade = pygame.math.Vector2(0, 0)
            return steering

        if distancia > self.raio_desaceleracao:
            vel_desejada = self.agente.vel_maxima
        else:
            vel_desejada = self.agente.vel_maxima * (distancia / self.raio_desaceleracao)

        vetor_vel_desejada = direcao.normalize() * vel_desejada
        steering.linear = (vetor_vel_desejada - self.agente.velocidade) / self.tempo_para_alvo

        if steering.linear.length() > self.agente.acel_maxima:
            steering.linear = steering.linear.normalize() * self.agente.acel_maxima

        return steering