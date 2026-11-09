from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.sprite import Sprite
from Poluicao import *
from PPlay.window import Window
from GerenciadorDeHordas import GerenciadorHordas
from bancada import *

if TYPE_CHECKING:
    from PPlay.mouse import Mouse

class Quadrante(Sprite):
    def __init__(self, caminho_imagem, posX: float, posY: float, tipoTerreno: str, total_frames=1):
        super().__init__(caminho_imagem, total_frames)
        self.tipoTerreno = tipoTerreno

        self.set_position(posX, posY)
        self.planta = None

class Tabuleiro:
    def __init__(self, window: Window, mouse: Mouse, mapaTemplate, poluicoesTemplate: list[dict],plantasDaFase, larguraCasa: int, alturaCasa: int):
        self.window = window
        self.mouse = mouse
        self.linhas = len(mapaTemplate)
        self.colunas = len(mapaTemplate[0])
        self.alturaCasa = alturaCasa
        self.larguraCasa = larguraCasa
        self.assentamento = []
        self.gerenciadorDeHordas = GerenciadorHordas(poluicoesTemplate)
        self.tempoDecorrido = 0
        self.poluicoesVivas = []
        self.plantasVivas = []
        self.bancada = Bancada("resources/bancada.jpg", plantasDaFase, 10, window.altura, mouse)
        self.plantaSelecionada = None
        self.previewSprite = None


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

    def gameOver(self):
        for poluicao in self.poluicoesVivas:
            if (poluicao.x + poluicao.width) <= 0:
                return True
        return False

    def youWin(self):
        if (len(self.gerenciadorDeHordas.filaSpawnPoluicoes) == 0) and (len(self.poluicoesVivas) == 0):
            return True
        return False

    def passaTempo(self, deltaTime):
        self.tempoDecorrido += deltaTime
        self.bancada.cresceBrotos(deltaTime)
        novaSelecao = self.bancada.selectPlanta()
        if novaSelecao != None:
            self.plantaSelecionada = novaSelecao
            self.previewSprite = Sprite(novaSelecao.item)


    def plantar(self):
        line, col = self.selectQuadrante()
        if line != -1 and col != -1:
            self.plantarNoQuadrante(line, col)

    def selectQuadrante(self):
        if self.mouse.button_down(1):
            if self.plantaSelecionada != None:
                for i in range(len(self.assentamento)):
                    for j in range(len(self.assentamento[i])):
                        if self.mouse.is_over_object(self.assentamento[i][j]):
                            return i, j
        return -1, -1

    def plantarNoQuadrante(self, linIndex: int, colIndex: int):
        if self.plantaSelecionada != None:
            if self.plantaSelecionada.brotosNecessarios <= self.bancada.qtdBrotosAtuais:
                if self.assentamento[linIndex][colIndex].planta == None:
                    if (self.plantaSelecionada.tipo == (self.assentamento[linIndex][colIndex]).tipoTerreno):
                        novaPlanta = self.plantaSelecionada(linIndex, colIndex)
                        (self.assentamento[linIndex][colIndex]).planta = novaPlanta
                        self.plantasVivas.append(novaPlanta)
                        self.bancada.qtdBrotosAtuais -= self.plantaSelecionada.brotosNecessarios
                        self.plantaSelecionada = None
                        self.previewSprite = None

    def selecionaPlanta(self):
        if self.previewSprite == None:
            pass
        else:
            x, y = self.mouse.get_position()
            self.previewSprite.set_position(x, y)
    
    def draw(self):
        for linha in self.assentamento:
            for quadrante in linha:
                quadrante.draw()

                if quadrante.planta:
                    if quadrante.planta in self.plantasVivas:
                        quadrante.planta.plantaSetPosition(quadrante)
                        quadrante.planta.draw()
                    else:
                        quadrante.planta = None
            
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
                if poluicao.deveAndar() == True:
                    poluicao.moverPoluicao(deltaTime)

    def ataquePoluicoes(self, deltaTime):
        for poluicao in self.poluicoesVivas:
            poluicao.atacar(self.plantasVivas, deltaTime)

    def drawPoluicoes(self):
        for poluicao in self.poluicoesVivas:
            poluicao.draw()

    def atiraPlantas(self, deltaTime):
        for planta in self.plantasVivas:
            if planta.deveAtirar(self.poluicoesVivas, deltaTime):
                planta.atirar(self.alturaCasa, self.larguraCasa)
                
            planta.moverTiros(deltaTime)

    def tiroAcertou(self):
        for planta in self.plantasVivas:
            planta.acertouTiro(self.poluicoesVivas, self.plantasVivas)
    
    def drawTiros(self):
        for planta in self.plantasVivas:
            for tiro in planta.tiros:
                tiro.draw()

    def bancadaDraw(self):
        self.bancada.draw()
        self.bancada.drawItems()

    def drawPlantaSelecionada(self):
        if self.previewSprite == None:
            pass
        else:
            self.previewSprite.draw()