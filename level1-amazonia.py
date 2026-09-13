from PPlay.window import Window
from PPlay.mouse import Mouse
from tabuleiro import Tabuleiro
from Planta import Feijao, VitoriaRegia


window = Window(800, 600, "level1-amazônia")
window.set_background_color((88,155,86))

mouse = Mouse()

mapaTemplate = [
    ['T', 'T', 'T', 'T'],
    ['T', 'T', 'T', 'T'],
    ['T', 'T', 'A', 'A'],
    ['T', 'A', 'A', 'A']
]

assentamento = Tabuleiro(mapaTemplate, 120, 100)
feijao = Feijao()
vitoriaRegia = VitoriaRegia()
assentamento.plantar(feijao, 1, 1)
assentamento.plantar(feijao, 0, 2)
assentamento.plantar(vitoriaRegia, 2, 2)
assentamento.plantar(vitoriaRegia, 3, 1)

while True:
    assentamento.draw()
    window.update()