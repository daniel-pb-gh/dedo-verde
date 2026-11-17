from PPlay.window import Window
from PPlay.mouse import Mouse
from PPlay.sound import Music
from tabuleiro import Tabuleiro
from Planta import *

def level4Caatinga():

    window = Window(800, 600, "level1-amazônia")
    window.set_background_color((191,165,123))

    mouse = Mouse()

    musicaDaFase = Music("resources/Music/Ambient 3.ogg")
    musicaDaFase.play()

    mapaTemplate = [
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T'],
        ['T', 'T', 'T', 'T', 'T', 'T']
    ]

    poluicoesTemplate = [
        {"tempo": 1.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 5.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 9.0, "linha": 0, "tipo": "plastico"},
        {"tempo": 14.0, "linha": 1, "tipo": "oleo"},
        {"tempo": 18.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 23.0, "linha": 2, "tipo": "oleo"},
        {"tempo": 27.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 31.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 36.0, "linha": 3, "tipo": "plastico"},
        {"tempo": 40.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 46.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 50.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 54.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 60.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 64.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 70.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 74.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 80.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 84.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 90.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 94.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 96.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 98.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 102.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 105.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 110.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 113.0, "linha": 1, "tipo": "plastico"},
        {"tempo": 116.0, "linha": 0, "tipo": "oleo"},
        {"tempo": 120.0, "linha": 2, "tipo": "plastico"},
        {"tempo": 122.0, "linha": 3, "tipo": "oleo"},
        {"tempo": 124.0, "linha": 1, "tipo": "plastico"}
    ]

    plantasDaFase = [Feijao, Seringueira, VitoriaRegia, Guarana]
    assentamento = Tabuleiro(window, mouse, mapaTemplate, poluicoesTemplate, plantasDaFase, "resources/quadranteCaatinga.png", 120, 120)

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
