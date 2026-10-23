import math
from classes.steering import SteeringOutput
from classes.align import Align

class LookWhereYoureGoing:
    def __init__(self, agente, raio_alvo = 0.01, raio_desaceleracao = 0.5, tempo_para_alvo = 0.1):
        self.agente = agente
        self.raio_alvo = raio_alvo
        self.raio_desaceleracao = raio_desaceleracao
        self.tempo_para_alvo = tempo_para_alvo

    def get_steering(self):
        if self.agente.velocidade.length() == 0:
            return SteeringOutput()

        alvo_orientacao = math.atan2(self.agente.velocidade.y, self.agente.velocidade.x)

        delega_align = Align(
            self.agente,
            alvo_orientacao,
            raio_alvo = self.raio_alvo,
            raio_desaceleracao = self.raio_desaceleracao,
            tempo_para_alvo = self.tempo_para_alvo
        ) 
        return delega_align.get_steering()