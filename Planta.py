from __future__ import annotations
from PPlay.sprite import Sprite
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from HitBox import HitBox

if TYPE_CHECKING:
    from Poluicao import Poluicao
    from PPlay.gameobject import GameObject

class Planta(ABC, Sprite):
    pontosDeVida: int
    tipo: str
    linha: int
    coluna: int
    hitBox: GameObject

    def __init__(self, caminho_imagem, total_frames=1):
        super().__init__(caminho_imagem, total_frames)

    @abstractmethod
    def deveAtirar(self, poluicoesVivas: list[Poluicao], deltaTime) -> bool:
        pass

    @abstractmethod
    def atirar(self, larguraCasa, alturaCasa) -> None:
        pass

    @abstractmethod
    def moverTiros(self, deltaTime) -> None:
        pass
            
class Feijao(Planta):
    tipo = "terrestre"  
    
    def __init__(self, linha: int, coluna: int):
        super().__init__("resources/spriteFeijao.png")
        self.pontosDeVida = 100
        self.dano = 2
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.cooldownTime = 0
        self.hitBox = HitBox(100, 100)

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x + (quadrante.width / 4)
        posY = quadrante.y - (quadrante.height / 6)
        self.set_position(posX, posY)

        self.hitBox.x = posX
        self.hitBox.y = quadrante.y

    def deveAtirar(self, poluicoesVivas: list[Poluicao], deltaTime):
        for poluicao in poluicoesVivas:
            if poluicao.linha == self.linha and self.cooldownTime <= 0 and float(poluicao.x) > float(self.x):
                self.cooldownTime = 5
                return True
        self.cooldownTime -= deltaTime
        return False

    def atirar(self, larguraCasa: int, alturaCasa: int) -> None:
        tiroFeijao = Sprite("resources/tiroFeijao.png")
        self.tiros.append(tiroFeijao)
        xTiro = self.x + (self.width/2)
        yTiro = self.linha * alturaCasa
        tiroFeijao.set_position(xTiro, yTiro)

    def acertouTiro(self, poluicoesVivas: list[Poluicao], plantasVivas: list[Planta]):
        for tiro in self.tiros:
            for poluicao in poluicoesVivas:
                if tiro.collided(poluicao):
                    self.tiros.remove(tiro)
                    poluicao.pontosDeVida -= self.dano
                    if poluicao.pontosDeVida <= 0:
                        poluicoesVivas.remove(poluicao)

    def moverTiros(self, deltaTime):
        for tiro in self.tiros:
            tiro.x += 100 * deltaTime

class VitoriaRegia(Planta):
    def __init__(self, linha: int, coluna: int):
        super().__init__("resources/spriteVitoriaRegia.png")
        self.pontosDeVida = 50
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.dano = float("inf")
        self.hitbox = None

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x
        posY = quadrante.y
        self.set_position(posX, posY)

        #tiro
        tiro = Sprite("resources/invisible.png")
        tiro.set_position(self.x, self.y)
        self.tiros.append(tiro)

        #hitBox
        self.hitBox = tiro

    def deveAtirar(self, poluicoesVivas: list[Poluicao], deltaTime):
        for poluicao in poluicoesVivas:
            if poluicao.linha == self.linha:
                return True
        return False

    def atirar(self, larguraCasa, alturaCasa) -> None:
        pass

    def acertouTiro(self, poluicoesVivas: list[Poluicao], plantasVivas: list[Planta]):
        for tiro in self.tiros:
            for poluicao in poluicoesVivas:
                if tiro.collided(poluicao):
                    poluicoesVivas.remove(poluicao)
                    plantasVivas.remove(self)


    def moverTiros(self, deltaTime) -> None:
        pass

    tipo = "aquatico"  