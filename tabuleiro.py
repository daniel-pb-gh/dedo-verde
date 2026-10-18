from PPlay.sprite import Sprite
from Planta import Planta
from Poluicao import *
from PPlay.window import Window
from GerenciadorDeHordas import GerenciadorHordas

class Quadrante(Sprite):
    def __init__(self, caminho_imagem, posX: float, posY: float, tipoTerreno: str, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        self.tipoTerreno = tipoTerreno

        self.set_position(posX, posY)
        self.planta = None

class Tabuleiro:
    def __init__(self, window: Window, mapaTemplate, poluicoesTemplate: list[dict],larguraCasa: int, alturaCasa: int):
        self.window = window
        self.linhas = len(mapaTemplate)
        self.colunas = len(mapaTemplate[0])
        self.alturaCasa = alturaCasa
        self.larguraCasa = larguraCasa
        self.assentamento = []
        self.gerenciadorDeHordas = GerenciadorHordas(poluicoesTemplate)
        self.tempoDecorrido = 0
        self.poluicoesVivas = []
        self.plantasVivas = []


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

    
    def passaTempo(self, deltaTime):
        self.tempoDecorrido += deltaTime
    
    def draw(self):
        for linha in self.assentamento:
            for quadrante in linha:
                quadrante.draw()

                if quadrante.planta:
                    quadrante.planta.plantaSetPosition(quadrante)
                    quadrante.planta.draw()

            
    def invocaPoluicao(self, deltaTime):
        poluicoesParaSpawn = self.gerenciadorDeHordas.processarSpawns(deltaTime)
        
        for poluicao in poluicoesParaSpawn:

            novaPoluicao = Poluicao.fabricaPoluicao(poluicao)
            if novaPoluicao == None:
                return None
            
            linhaPoluicao = poluicao["linha"]
            yPoluicao = linhaPoluicao * self.alturaCasa - (self.alturaCasa/6)
            novaPoluicao.set_position(self.window.largura, yPoluicao)
            self.poluicoesVivas.append(novaPoluicao)

    def movePoluicoes(self, deltaTime):
        if len(self.poluicoesVivas) > 0:
            for poluicao in self.poluicoesVivas:
                poluicao.moverPoluicao(deltaTime)

    def drawPoluicoes(self):
        for poluicao in self.poluicoesVivas:
            poluicao.draw()

    def atiraPlantas(self, deltaTime):
        for planta in self.plantasVivas:
            if planta.deveAtirar(self.poluicoesVivas, deltaTime):
                planta.atirar(self.alturaCasa, self.larguraCasa)
                
            planta.moverTiros(deltaTime)

    def drawTiros(self):
        for planta in self.plantasVivas:
            for tiro in planta.tiros:
                tiro.draw()

    def plantar(self, planta: Planta, linIndex: int, colIndex: int):
        if (planta.tipo == (self.assentamento[linIndex][colIndex]).tipoTerreno):
            (self.assentamento[linIndex][colIndex]).planta = planta
            self.plantasVivas.append(planta)
