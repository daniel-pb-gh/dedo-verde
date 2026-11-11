from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.sprite import Sprite
from abc import ABC, abstractmethod
from HitBox import HitBox

if TYPE_CHECKING:
    from Poluicao import Poluicao
    from PPlay.gameobject import GameObject

class Planta(ABC, Sprite):
    pontosDeVida: int
    tipo: str
    linha: int
    coluna: int
    tiros: list[Sprite]
    dano = 10
    hitBox: GameObject
    item: str
    brotosNecessarios: int
    cooldownTime: float
    currentCooldown: float

    
    def __init__(self, caminho_imagem, total_frames=1):
        super().__init__(caminho_imagem, total_frames)


    def deveAtirar(self, poluicoesVivas: list[Poluicao], deltaTime):
        for poluicao in poluicoesVivas:
            if poluicao.linha == self.linha and self.currentCooldown <= 0 and float(poluicao.x) > float(self.x):
                self.currentCooldown = self.cooldownTime
                return True
        self.currentCooldown -= deltaTime
        return False

    def acertouTiro(self, poluicoesVivas: list[Poluicao], plantasVivas: list[Planta]):
        tirosParaRemover = set()
        for tiro in self.tiros:
            for poluicao in poluicoesVivas:
                if tiro.collided(poluicao):
                    tirosParaRemover.add(tiro)
                    poluicao.pontosDeVida -= self.dano
                    if poluicao.pontosDeVida <= 0:
                        poluicoesVivas.remove(poluicao)
                    break

        for tiro in tirosParaRemover:
            self.tiros.remove(tiro)

    @abstractmethod
    def atirar(self, larguraCasa, alturaCasa) -> None:
        pass

    @abstractmethod
    def moverTiros(self, deltaTime) -> None:
        pass
            
class Feijao(Planta):
    tipo = "terrestre"  
    item = "resources/feijaoItem.png"
    brotosNecessarios = 6
    
    def __init__(self, linha: int, coluna: int):
        super().__init__("resources/spriteFeijao.png")
        self.pontosDeVida = 100
        self.dano = 10
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.cooldownTime = 5
        self.currentCooldown = 0
        self.hitBox = HitBox(45, 100) # primeiro argumento largura, segundo altura.

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x + (quadrante.width / 4)
        posY = quadrante.y - (quadrante.height / 6)
        self.set_position(posX, posY)

        self.hitBox.x = posX
        self.hitBox.y = quadrante.y

    def atirar(self, larguraCasa: int, alturaCasa: int) -> None:
        tiroFeijao = Sprite("resources/tiroFeijao.png")
        self.tiros.append(tiroFeijao)
        xTiro = self.x + (self.width/2)
        yTiro = self.linha * alturaCasa
        tiroFeijao.set_position(xTiro, yTiro)

    def moverTiros(self, deltaTime):
        for tiro in self.tiros:
            tiro.x += 100 * deltaTime


class Guarana(Planta):
    tipo = "terrestre"  
    item = "resources/guaranaItem.png"
    brotosNecessarios = 6
    
    def __init__(self, linha: int, coluna: int):
        super().__init__("resources/spriteGuarana.png")
        self.pontosDeVida = 100
        self.dano = 1
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.cooldownTime = 1
        self.currentCooldown = 0
        self.hitBox = HitBox(66, 100) # primeiro argumento largura, segundo altura.

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x + 5
        posY = quadrante.y - (quadrante.height / 6)
        self.set_position(posX, posY)

        self.hitBox.x = posX
        self.hitBox.y = quadrante.y

    def atirar(self, larguraCasa: int, alturaCasa: int) -> None:
        tiroGuarana = Sprite("resources/tiroGuarana.png")
        self.tiros.append(tiroGuarana)
        xTiro = self.x + (self.width/2)
        yTiro = (self.linha * alturaCasa) + (alturaCasa/3)
        tiroGuarana.set_position(xTiro, yTiro)

    def moverTiros(self, deltaTime):
        for tiro in self.tiros:
            tiro.x += 100 * deltaTime


class VitoriaRegia(Planta):
    tipo = "aquatico"  
    item = "resources/vitoriaRegiaItem.png"
    brotosNecessarios = 5
    
    def __init__(self, linha: int, coluna: int):
        super().__init__("resources/spriteVitoriaRegia.png")
        self.pontosDeVida = 50
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.dano = float("inf")
        self.hitBox = HitBox(10, 10)

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