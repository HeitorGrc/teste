import pygame
import random
import math

class Circulo: 
    def __init__(self, tela, cor, posicao, raio):
        self.tela = tela
        self.cor = cor
        self.posicao = posicao
        self.raio = raio
    def draw(self):
        pygame.draw.circle(self.tela,self.cor, self.posicao,self.raio)
    def move(self,velocidade):
        self.posicao += velocidade