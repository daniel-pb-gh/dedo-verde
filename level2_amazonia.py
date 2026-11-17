from PPlay.window import Window
from PPlay.mouse import Mouse
from PPlay.sound import Music
from tabuleiro import Tabuleiro
from Planta import *

def level2amazonia():

    window = Window(800, 600, "level1-amazônia")
    window.set_background_color((88,155,86))

    mouse = Mouse()

    musicaDaFase = Music("resources/Music/Ambient 3.ogg")
    musicaDaFase.play()

    mapaTemplate = [
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'A', 'A'],
        ['T', 'T', 'T', 'A', 'A', 'A']
    ]

    poluicoesTemplate = [
        {"tempo": 1.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 3.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 5.0, "linha": 0, "tipo": "plastico"},
        {"tempo": 7.5, "linha": 1, "tipo": "oleo"},
        {"tempo": 10.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 14.0, "linha": 2, "tipo": "oleo"},
        {"tempo": 17.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 20.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 23.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 24.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 26.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 29.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 32.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 33.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 36.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 38.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 40.5, "linha": 2, "tipo": "plastico"},
        {"tempo": 43.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 46.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 49.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 52.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 55.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 57.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 60.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 61.0, "linha": 2, "tipo": "plastico"},
        ]

    plantasDaFase = [Seringueira, VitoriaRegia, Guarana]
    assentamento = Tabuleiro(window, mouse, mapaTemplate, poluicoesTemplate, plantasDaFase, "resources/spriteQTerrestre.png", 120, 120)

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

        window.update()
