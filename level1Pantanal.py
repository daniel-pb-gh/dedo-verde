from PPlay.window import Window
from PPlay.mouse import Mouse
from PPlay.sound import Music
from tabuleiro import Tabuleiro
from Planta import *

def level1Pantanal():

    window = Window(800, 600, "level1-amazônia")
    window.set_background_color((88,155,86))

    mouse = Mouse()

    musicaDaFase = Music("resources/Music/Ambient 8.ogg")
    musicaDaFase.play()

    mapaTemplate = [
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'A', 'A', 'A', 'T'],
        ['T', 'A', 'A', 'A', 'A', 'A']
    ]

    poluicoesTemplate = [
        {"tempo": 0.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 0.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 8.5, "linha": 1, "tipo": "oleo"},
        {"tempo": 13.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 19.0, "linha": 2, "tipo": "oleo"},
        {"tempo": 22.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 29.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 36.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 42.0, "linha": 0, "tipo": "oleo"}
        ]

    plantasDaFase = [VitoriaRegia, Guarana]
    assentamento = Tabuleiro(window, mouse, mapaTemplate, poluicoesTemplate, plantasDaFase, 120, 120)

    while True:
        assentamento.passaTempo(window.delta_time())
        assentamento.invocaPoluicao(window.delta_time())
        #assentamento.movePoluicoes(window.delta_time())
        assentamento.atiraPlantas(window.delta_time())
        assentamento.tiroAcertou()
        #assentamento.ataquePoluicoes(window.delta_time())
        assentamento.plantar()

        assentamento.selecionaPlanta()
        assentamento.draw()
        assentamento.progridePoluicoes(window.delta_time()) ##Função Nova
        
        #assentamento.drawPoluicoes()
        assentamento.drawTiros()
        assentamento.bancadaDraw()
        
        assentamento.drawPlantaSelecionada()
        if assentamento.gameOver():
            musicaDaFase.stop()
            return 0
        if assentamento.youWin():
            musicaDaFase.stop()
            return 1

        if window.delta_time() > 0:
            print(1/window.delta_time())

        window.update()