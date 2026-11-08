from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.sprite import Sprite

if TYPE_CHECKING:
    from Planta import *
    from PPlay.mouse import Mouse

class Bancada(Sprite):
    def __init__(self, caminho_imagem, plantasDaFase, posicaoX, alturaJanela, mouse: Mouse, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        posicaoY = (alturaJanela - (self.height) - 7)
        self.set_position(posicaoX, posicaoY)
        self.plantasDaFase = plantasDaFase
        self.maxBrotos = 15
        self.qtdBrotosAtuais = 7
        self.spriteBroto = Sprite("resources/mudaSprite.png")
        self.timerBrotos = 0
        self.mouse = mouse
        self.classePlantas_sprites = {}

        lastSprite = None
        for i in range(len(plantasDaFase)):
            if lastSprite == None:
                classePlanta = plantasDaFase[i]
                sprite = Sprite(classePlanta.item)
                spriteX = (self.x + 25)
                spriteY = (self.y + 7)
                sprite.set_position(spriteX, spriteY)
                self.classePlantas_sprites[classePlanta] = sprite
                lastSprite = sprite
            else:
                classePlanta = plantasDaFase[i]
                sprite = Sprite(classePlanta.item)
                spriteX = ((lastSprite.x + lastSprite.width) + 10)
                spriteY = (self.y + 7)
                sprite.set_position(spriteX, spriteY)
                self.classePlantas_sprites[classePlanta] = sprite
                lastSprite = sprite

    def cresceBrotos(self, deltaTime):
        if self.qtdBrotosAtuais < self.maxBrotos:
            if self.timerBrotos <= 0:
                self.qtdBrotosAtuais += 1
                self.timerBrotos = 0.5
            else:
                self.timerBrotos -= deltaTime

    def selectPlanta(self):
        if self.mouse.button_down(1):
            for classePlanta, sprite in self.classePlantas_sprites.items():
                if self.mouse.is_over_object(sprite):
                    return classePlanta
        
    def drawItems(self):
        self.draw()

        for i in range(self.qtdBrotosAtuais):
            brotoX = (self.x + 25) + (25 * i)
            brotoY = self.y + (71)
            self.spriteBroto.set_position(brotoX, brotoY)
            self.spriteBroto.draw()

        for sprite in self.classePlantas_sprites.values():
            sprite.draw()