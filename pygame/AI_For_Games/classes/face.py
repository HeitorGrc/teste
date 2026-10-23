import math
from classes.steering import SteeringOutput
from classes.align import Align

class Face:
    def __init__(self, agente, alvo_posicao):
        self.agente = agente
        self.alvo_posicao = alvo_posicao

    def get_steering(self):
        direcao = self.alvo_posicao - self.agente.posicao

        if direcao.length() == 0:
            return SteeringOutput()

        alvo_orientacao = math.atan2(direcao.y, direcao.x)

        delega_align = Align(self.agente, alvo_orientacao)
        return delega_align.get_steering()