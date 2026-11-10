from PPlay.window import Window
from PPlay.mouse import Mouse
from tabuleiro import Tabuleiro
from Planta import *

def level1amazonia():

    window = Window(800, 600, "level1-amazônia")
    window.set_background_color((88,155,86))

    mouse = Mouse()

    mapaTemplate = [
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'A', 'A', 'A', 'T'],
        ['T', 'A', 'A', 'A', 'A', 'A']
    ]

    poluicoesTemplate = [
        {"tempo": 0.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 0.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 8.5, "linha": 1, "tipo": "plastico"},
        {"tempo": 13.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 19.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 22.0, "linha": 0, "tipo": "plastico"},
        {"tempo": 29.0, "linha": 0, "tipo": "plastico"},
        {"tempo": 36.0, "linha": 0, "tipo": "plastico"},
        {"tempo": 42.0, "linha": 0, "tipo": "plastico"}
        ]

    plantasDaFase = [Feijao, VitoriaRegia, Guarana]
    assentamento = Tabuleiro(window, mouse, mapaTemplate, poluicoesTemplate, plantasDaFase, 120, 120)

    while True:
        assentamento.passaTempo(window.delta_time())
        assentamento.invocaPoluicao(window.delta_time())
        #assentamento.movePoluicoes(window.delta_time())
        assentamento.atiraPlantas(window.delta_time())
        assentamento.tiroAcertou()
        #assentamento.ataquePoluicoes(window.delta_time())
        assentamento.plantar()

        assentamento.progridePoluicoes(window.delta_time()) ##Função Nova

        assentamento.draw()
        #assentamento.drawPoluicoes()
        assentamento.drawTiros()
        assentamento.bancadaDraw()
        assentamento.selecionaPlanta()
        assentamento.drawPlantaSelecionada()
        if assentamento.gameOver():
            return 0
        if assentamento.youWin():
            return 1

        window.update()

def youWin():
    window = Window(800, 600, "you Win")
    screen = Sprite("resources/results/youWin.jpg")
    timer = 2
    currentTime = 0

    while True:
        screen.draw()
        if currentTime >= timer:
            return
        currentTime += window.delta_time()
        window.update()

def gameOver():
    window = Window(800, 600, "you Win")
    screen = Sprite("resources/results/gameOver.jpg")
    timer = 2
    currentTime = 0

    while True:
        screen.draw()
        if currentTime >= timer:
            return
        currentTime += window.delta_time()
        window.update()