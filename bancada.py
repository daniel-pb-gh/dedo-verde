from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.sprite import Sprite

if TYPE_CHECKING:
    from Planta import *

class Bancada(Sprite):
    def __init__(self, caminho_imagem, plantasDaFase, posicaoX, alturaJanela, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        posicaoY = (alturaJanela - (self.height) - 7)
        self.set_position(posicaoX, posicaoY)
        self.plantasDaFase = plantasDaFase
        self.spritesDasPLantas = []
        self.maxBrotos = 15
        self.qtdBrotosAtuais = 7
        self.brotosAtuais = []
        self.timerBrotos = 0

        for i in range(self.qtdBrotosAtuais):
            broto = Sprite("resources/mudaSprite.png")
            brotoX = (self.x + 25) + (25 * i)
            brotoY = self.y + (71)
            broto.set_position(brotoX, brotoY)
            self.brotosAtuais.append(broto)

        for i in range(len(plantasDaFase)):
            sprite = Sprite((plantasDaFase[i]).item)
            spriteX = (self.x + 25) + (50 * i)
            spriteY = (self.y + 7)
            sprite.set_position(spriteX, spriteY)
            self.spritesDasPLantas.append(sprite)

    def cresceBrotos(self, deltaTime):
        if self.qtdBrotosAtuais < self.maxBrotos:
            if self.timerBrotos <= 0:
                broto = Sprite("resources/mudaSprite.png")
                brotoX = (self.x + 25) + (25 * self.qtdBrotosAtuais)
                brotoY = self.y + (71)
                broto.set_position(brotoX, brotoY)
                self.brotosAtuais.append(broto)
                self.qtdBrotosAtuais += 1
                self.timerBrotos = 2.5
            else:
                self.timerBrotos -= deltaTime

    def drawItems(self):
        self.draw()

        for broto in self.brotosAtuais:
            broto.draw()

        for planta in self.spritesDasPLantas:
            planta.draw()