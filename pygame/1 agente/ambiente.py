import pygame
import random
import math

from circulo import Circulo

class Ambiente:
    def __init__(self, tela, largura, altura, raio_padrao, total_alvos):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.raio_padrao = raio_padrao
        self.total_alvos = total_alvos
        self.alvos = []
        
        self.gerar_alvos()

    def gerar_alvos(self):
        self.alvos = []
        for _ in range(self.total_alvos):
            x = random.randint(self.raio_padrao, self.largura - self.raio_padrao)
            y = random.randint(self.raio_padrao, self.altura - self.raio_padrao)
            vetor_pos = pygame.math.Vector2(x, y)
            
            alvo = Circulo(self.tela, "Green", vetor_pos, self.raio_padrao)
            self.alvos.append(alvo)

    def desenhar(self):
        for alvo in self.alvos:
            alvo.draw()