import math
import random
import pygame

from classes.steering import SteeringOutput
from classes.face import Face

class Wander:
    def __init__(self, agente, wander_offset = 80.0, wander_radius = 40.0, wander_rate = 0.5):
        self.agente = agente
        self.wander_offset = wander_offset
        self.wander_radius = wander_radius
        self.wander_rate = wander_rate
        
        self.wander_orientation = 0.0

    def random_binomial(self): 
        return random.random() - random.random()

    def get_steering(self):
        steering = SteeringOutput()

        self.wander_orientation += self.random_binomial() * self.wander_rate
        target_orientation = self.wander_orientation + self.agente.orientacao

        frente_agente = pygame.math.Vector2(math.cos(self.agente.orientacao), math.sin(self.agente.orientacao))
        circulo_centro = self.agente.posicao + frente_agente * self.wander_offset

        ponto_circulo = pygame.math.Vector2(math.cos(target_orientation), math.sin(target_orientation)) * self.wander_radius
        alvo_wander = circulo_centro + ponto_circulo

        delega_face = Face(self.agente, alvo_wander)
        steering_face = delega_face.get_steering()
        if steering_face is not None:
            steering.angular = steering_face.angular

        steering.linear = frente_agente * self.agente.acel_maxima

        return steering

