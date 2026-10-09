import pygame
import random
import math

class Agente: 
    def __init__(self, tela, posicao, raio, raio_visao=13):
        self.tela = tela
        self.posicao = posicao
        self.raio = raio
        self.raio_visao = raio_visao
        self.direcao = pygame.math.Vector2(1, 0)
        
        self.vetor_alvo = pygame.math.Vector2(0, 0)
        self.vetor_repulsao = pygame.math.Vector2(0, 0)
        self.vetor_resultante = pygame.math.Vector2(0, 0)

    def atualizar_vetores(self, pos_alvo, obstaculos):
        self.vetor_alvo = pos_alvo - self.posicao
        if self.vetor_alvo.length() > 0:
            self.vetor_alvo = self.vetor_alvo.normalize()

        self.vetor_repulsao = pygame.math.Vector2(0, 0)
        for obs in obstaculos:
            dist_centro = self.posicao.distance_to(obs.posicao)
        
            dist_borda = dist_centro - obs.raio
            
            distancia_minima = self.raio
            
            if dist_borda < self.raio_visao:
                fuga = self.posicao - obs.posicao
                if fuga.length() > 0:
                    perpendicular = pygame.math.Vector2(-fuga.y, fuga.x).normalize()
                    
                    forca = (self.raio_visao - dist_borda) / (self.raio_visao - distancia_minima)
                    forca = max(0.0, forca) * 2.5
                    
                    self.vetor_repulsao += (fuga.normalize() + perpendicular * 0.5) * forca

        self.vetor_resultante = self.vetor_alvo + self.vetor_repulsao
        if self.vetor_resultante.length() > 0:
            self.vetor_resultante = self.vetor_resultante.normalize()
            self.direcao = self.vetor_resultante.copy()

    def move(self, velocidade_escalar, dt):
        if self.vetor_resultante.length() > 0:
            self.posicao += self.vetor_resultante * velocidade_escalar * dt

    def draw(self):

        pygame.draw.circle(self.tela, (150, 150, 150), self.posicao, self.raio_visao, 1)

        pygame.draw.circle(self.tela, "Red", self.posicao, self.raio)

        escala_vetor = 40

        if self.vetor_alvo.length() > 0:
            fim_alvo = self.posicao + self.vetor_alvo * escala_vetor
            pygame.draw.line(self.tela, "Green", self.posicao, fim_alvo, 2)

        if self.vetor_repulsao.length() > 0:
            fim_rep = self.posicao + self.vetor_repulsao * escala_vetor
            pygame.draw.line(self.tela, (255, 128, 0), self.posicao, fim_rep, 2)

        if self.vetor_resultante.length() > 0:
            fim_res = self.posicao + self.vetor_resultante * escala_vetor
            pygame.draw.line(self.tela, "Blue", self.posicao, fim_res, 3)