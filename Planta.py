from PPlay.sprite import Sprite
from Poluicao import Poluicao
from abc import ABC, abstractmethod

class Planta(ABC, Sprite):
    pontosDeVida: int
    tipo: str
    linha: int
    coluna: int

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
        self.linha = linha
        self.coluna = coluna
        self.tiros = []
        self.cooldownTime = 0

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x + (quadrante.width / 4)
        posY = quadrante.y - (quadrante.height / 6)
        self.set_position(posX, posY)

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

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x
        posY = quadrante.y
        self.set_position(posX, posY)

    def deveAtirar(self, poluicoesVivas: list[Poluicao], deltaTime):
        for poluicao in poluicoesVivas:
            if poluicao.linha == self.linha:
                return True
        return False

    def atirar(self, larguraCasa, alturaCasa) -> None:
        pass

    def moverTiros(self, deltaTime) -> None:
        pass

    tipo = "aquatico"  