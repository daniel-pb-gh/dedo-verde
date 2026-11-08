from __future__ import annotations
from PPlay.sprite import Sprite
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Planta import Planta

class Poluicao(ABC, Sprite):
    def __init__(self, caminho_imagem, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        self.linha = None
        self.pontosDeVida: float
        self.estado = "andando"
        self.dano: int
        self.cooldownTime: int
        self.currentCooldown: float
        self.pace: int


    @classmethod
    def fabricaPoluicao(cls, poluicao: dict):
        novaPoluicao = None
        match poluicao["tipo"]:
            case "plastico":
                return Plastico(poluicao["linha"])
            case "oleo":
                return Oleo(poluicao["linha"])
            case error:
                print("não tem essa poluicao")   
                return None 

    def deveAndar(self):
        if self.estado == "andando":
            return True
        return False

    def ataque(self, planta: Planta):
        planta.pontosDeVida -= self.dano

    def atacar(self, plantasVivas: list[Planta], deltaTime):
        self.estado = "andando"
        
        if self.currentCooldown > 0:
            self.currentCooldown -= deltaTime

        for planta in plantasVivas:
            if self.collided(planta.hitBox):
                self.estado = "atacando"
                if self.currentCooldown <= 0:
                    self.ataque(planta)
                    self.currentCooldown = self.cooldownTime
                    if planta.pontosDeVida <= 0:
                        plantasVivas.remove(planta)
                break

    def moverPoluicao(self, deltaTime):
        self.x -= self.pace * deltaTime


class Plastico(Poluicao):
    def __init__(self, linha: int):
        super().__init__("resources/spritePlastico.png")
        self.pontosDeVida = 40
        self.linha = linha
        self.dano = 75
        self.cooldownTime = 2
        self.currentCooldown = 0
        self.pace = 50

class Oleo(Poluicao):
    def __init__(self, linha: int):
        super().__init__("resources/spriteOleo.png")
        self.pontosDeVida = 30
        self.linha = linha
        self.dano = 90
        self.cooldownTime = 3
        self.currentCooldown = 0
        self.pace = 30