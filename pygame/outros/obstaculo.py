import pygame
import random
import math

class Obstaculo:
    def __init__(self, tela, posicao, raio):
        self.tela = tela
        self.posicao = posicao
        self.raio = raio
        self.cor = "Red"

    def draw(self):
        pygame.draw.circle(self.tela, self.cor, self.posicao, self.raio)