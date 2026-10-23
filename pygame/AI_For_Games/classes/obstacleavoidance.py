import pygame
from classes.steering import SteeringOutput
from classes.seek import Seek

class ObstacleAvoidance:
    def __init__(self, agente, obstaculos, distancia_lookahead=100, distancia_evitar=40):
        self.agente = agente
        self.obstaculos = obstaculos
        self.distancia_lookahead = distancia_lookahead
        self.distancia_evitar = distancia_evitar

    def get_steering(self):
        if self.agente.velocidade.length() > 0:
            direcao_frente = self.agente.velocidade.normalize()
        else:
            direcao_frente = pygame.math.Vector2(1, 0)

        obstaculo_mais_proximo = None
        menor_distancia = float('inf')

        for obs in self.obstaculos:
            dist = self.agente.posicao.distance_to(obs.posicao)
            if dist < (obs.raio + self.agente.raio + self.distancia_lookahead):
                if dist < menor_distancia:
                    menor_distancia = dist
                    obstaculo_mais_proximo = obs

        if not obstaculo_mais_proximo:
            return SteeringOutput()

        fuga_normal = (self.agente.posicao - obstaculo_mais_proximo.posicao)
        if fuga_normal.length() == 0:
            fuga_normal = pygame.math.Vector2(1, 0)
        else:
            fuga_normal = fuga_normal.normalize()

        perpendicular = pygame.math.Vector2(-fuga_normal.y, fuga_normal.x)
        
        if direcao_frente.dot(perpendicular) < 0:
            perpendicular = -perpendicular

        direcao_desvio = (fuga_normal + perpendicular * 0.8).normalize()

        alvo_temporario = obstaculo_mais_proximo.posicao + direcao_desvio * (obstaculo_mais_proximo.raio + self.distancia_evitar + self.agente.raio)

        delega_seek = Seek(self.agente, alvo_temporario)
        return delega_seek.get_steering()