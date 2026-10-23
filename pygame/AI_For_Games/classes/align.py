import math
from classes.steering import SteeringOutput

class Align:
    def __init__(self, agente, alvo_orientacao, raio_alvo = 0.01, raio_desaceleracao = 0.5, tempo_para_alvo = 0.1):
        self.agente = agente
        self.alvo_orientacao = alvo_orientacao
        self.raio_alvo = raio_alvo
        self.raio_desaceleracao = raio_desaceleracao
        self.tempo_para_alvo = tempo_para_alvo

    def mapear_para_intervalo(self, angulo):
        while angulo > math.pi:
            angulo -= 2 * math.pi
        while angulo < -math.pi:
            angulo += 2 * math.pi
        return angulo

    def get_steering(self):
        steering = SteeringOutput()

        rotation = self.alvo_orientacao - self.agente.orientacao
        rotation = self.mapear_para_intervalo(rotation)
        rotation_size = abs(rotation)

        if rotation_size < self.raio_alvo:
            self.agente.rotacao = 0.0
            return steering

        if rotation_size > self.raio_desaceleracao:
            rotacao_desejada = self.agente.rot_maxima
        else:
            rotacao_desejada = self.agente.rot_maxima * (rotation_size / self.raio_desaceleracao)

        rotacao_desejada *= (rotation / rotation_size)

        steering.angular = (rotacao_desejada - self.agente.rotacao) / self.tempo_para_alvo

        if abs(steering.angular) > self.agente.acel_angular_maxima:
            steering.angular = (steering.angular / abs(steering.angular)) * self.agente.acel_angular_maxima

        return steering

