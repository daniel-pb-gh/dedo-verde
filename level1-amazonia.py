from PPlay.window import Window
from PPlay.mouse import Mouse
from tabuleiro import Tabuleiro
from Planta import Feijao, VitoriaRegia


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
    {"tempo": 0.0, "linha": 0, "tipo": "plastico"},
    {"tempo": 8.5, "linha": 1, "tipo": "plastico"},
    {"tempo": 13.0, "linha": 3, "tipo": "plastico"},
    {"tempo": 19.0, "linha": 2, "tipo": "plastico"},
    {"tempo": 22.0, "linha": 0, "tipo": "plastico"},
    {"tempo": 29.0, "linha": 0, "tipo": "plastico"},
    {"tempo": 36.0, "linha": 0, "tipo": "plastico"},
    {"tempo": 42.0, "linha": 0, "tipo": "plastico"}
    ]


assentamento = Tabuleiro(window, mapaTemplate, poluicoesTemplate, 120, 120)
feijao1 = Feijao(1, 1)
feijao2 = Feijao(0, 2)
vitoriaRegia1 = VitoriaRegia(2, 2)
vitoriaRegia2 = VitoriaRegia(3, 1)
assentamento.plantar(feijao1, 1, 1)
assentamento.plantar(feijao2, 0, 2)
assentamento.plantar(vitoriaRegia1, 2, 2)
assentamento.plantar(vitoriaRegia2, 3, 1)

while True:
    assentamento.passaTempo(window.delta_time())
    assentamento.invocaPoluicao(window.delta_time())
    assentamento.movePoluicoes(window.delta_time())
    assentamento.atiraPlantas(window.delta_time())
    

    assentamento.draw()
    assentamento.drawPoluicoes()
    assentamento.drawTiros()

    window.update()