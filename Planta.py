from PPlay.sprite import Sprite
from abc import ABC

class Planta(ABC, Sprite):
    tipo = None
    def __init__(self, caminho_imagem, total_frames=1):
        super().__init__(caminho_imagem, total_frames)

class Feijao(Planta):
    def __init__(self):
        super().__init__("resources/spriteFeijao.png")

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x + (quadrante.width / 4)
        posY = quadrante.y - (quadrante.height / 6)
        self.set_position(posX, posY)


    tipo = "terrestre"  

class VitoriaRegia(Planta):
    def __init__(self):
        super().__init__("resources/spriteVitoriaRegia.png")

    def plantaSetPosition(self, quadrante):
        posX = quadrante.x
        posY = quadrante.y
        self.set_position(posX, posY)

    tipo = "aquatico"  