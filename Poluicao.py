from PPlay.sprite import Sprite
from abc import ABC

class Poluicao(ABC, Sprite):
    def __init__(self, caminho_imagem, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        self.linha = None

    @classmethod
    def fabricaPoluicao(self, poluicao: dict):
        novaPoluicao = None
        match poluicao["tipo"]:
            case "plastico":
                return Plastico(poluicao["linha"])
            case error:
                print("não tem essa poluicao")   
                return None 

    def moverPoluicao(self, deltaTime):
        self.x -= 50 * deltaTime


class Plastico(Poluicao):
    def __init__(self, linha: int):
        super().__init__("resources/spritePlastico.png")
        self.linha = linha
