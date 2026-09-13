from PPlay.sprite import Sprite
from Planta import Planta

class Quadrante(Sprite):
    def __init__(self, caminho_imagem, posX: float, posY: float, tipoTerreno: str, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        self.tipoTerreno = tipoTerreno

        self.set_position(posX, posY)
        self.planta = None
        self.poluicoes = []

class Tabuleiro:
    def __init__(self, mapaTemplate, larguraCasa: int, alturaCasa: int):
        self.linhas = len(mapaTemplate)
        self.colunas = len(mapaTemplate[0])
        self.assentamento = []

        for l in range(self.linhas):
            linhaAtual = []
            for c in range(self.colunas):
                x = (larguraCasa * c)
                y = (alturaCasa * l)

                novaCasa = None
                tipoCasa = mapaTemplate[l][c]
                if tipoCasa == 'A':
                    novaCasa = Quadrante("resources/spriteQAquatico.png", x, y, tipoTerreno="aquatico")
                else:
                    novaCasa = Quadrante("resources/spriteQTerrestre.png", x, y, tipoTerreno="terrestre")
                    
                linhaAtual.append(novaCasa)
            self.assentamento.append(linhaAtual)

    def draw(self):
        for linha in self.assentamento:
            for quadrante in linha:
                quadrante.draw()

                if quadrante.poluicoes:
                    for poluicao in quadrante.poluicoes:
                        poluicao.draw()

                if quadrante.planta:
                    quadrante.planta.plantaSetPosition(quadrante)
                    quadrante.planta.draw()

    def plantar(self, planta: Planta, linIndex: int, colIndex: int):
        if (planta.tipo == (self.assentamento[linIndex][colIndex]).tipoTerreno):
            (self.assentamento[linIndex][colIndex]).planta = planta
