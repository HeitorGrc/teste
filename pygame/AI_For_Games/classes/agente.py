import pygame
import math

class Agente:
    def __init__(self, tela, posicao, raio, massa=1.0, vel_maxima=150.0, acel_maxima=300.0, rot_maxima = math.pi * 2, acel_angular_maxima = math.pi * 4):
        self.tela = tela
        self.posicao = pygame.math.Vector2(posicao)
        self.velocidade = pygame.math.Vector2(0, 0)
        self.orientacao = 0.0
        self.rotacao = 0.0
        
        self.raio = raio
        self.massa = massa
        self.vel_maxima = vel_maxima
        self.acel_maxima = acel_maxima
        self.rot_maxima = rot_maxima
        self.acel_angular_maxima = acel_angular_maxima

    def update(self, steering, dt):
        if steering is None:
            return

        # Integração Física (Newton-Euler) do Livro
        self.posicao += self.velocidade * dt
        self.orientacao += self.rotacao * dt

        self.velocidade += steering.linear * dt
        self.rotacao += steering.angular * dt

        if self.velocidade.length() > 0:
            self.orientacao = math.atan2(self.velocidade.y, self.velocidade.x)

        if self.velocidade.length() > self.vel_maxima:
            self.velocidade = self.velocidade.normalize() * self.vel_maxima

        if abs(self.rotacao) > self.rot_maxima:
            self.rotacao = (self.rotacao / abs(self.rotacao)) * self.rot_maxima

    def draw(self):
        pygame.draw.circle(self.tela, "Red", self.posicao, self.raio)

        frente = pygame.math.Vector2(math.cos(self.orientacao), math.sin(self.orientacao))
        lado = pygame.math.Vector2(-frente.y, frente.x)

        pico = self.posicao + frente * (self.raio + 12)
        esquerda = self.posicao + frente * self.raio + lado * 6
        direita = self.posicao + frente * self.raio - lado * 6

        pygame.draw.polygon(self.tela, "Black", [pico, esquerda, direita])