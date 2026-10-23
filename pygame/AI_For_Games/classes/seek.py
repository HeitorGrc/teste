import pygame
from classes.steering import SteeringOutput

class Seek:
    def __init__(self, agente, alvo_posicao):
        self.agente = agente
        self.alvo_posicao = alvo_posicao

    def get_steering(self):
        steering = SteeringOutput()
        direcao = self.alvo_posicao - self.agente.posicao

        if direcao.length() > 0:
            steering.linear = direcao.normalize() * self.agente.acel_maxima

        steering.angular = 0.0
        return steering