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


    @classmethod
    def fabricaPoluicao(cls, poluicao: dict):
        novaPoluicao = None
        match poluicao["tipo"]:
            case "plastico":
                return Plastico(poluicao["linha"])
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
            else:
                self.estado = "andando"

    def moverPoluicao(self, deltaTime):
        self.x -= 50 * deltaTime


class Plastico(Poluicao):
    def __init__(self, linha: int):
        super().__init__("resources/spritePlastico.png")
        self.pontosDeVida = 40
        self.linha = linha
        self.dano = 75
        self.cooldownTime = 2
        self.currentCooldown = 0