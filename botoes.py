from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.window import Window
from PPlay.sprite import Sprite
from level1Pantanal import level1Pantanal
from level2_amazonia import level2amazonia
from level3Pampa import level3Pampa
from level4Caatinga import level4Caatinga


if TYPE_CHECKING:
    from PPlay.window import Window

def inicializaMapa():
    fases = []
    fases.append(Sprite("resources/mapas/mapaInicial.jpeg"))
    fases.append(Sprite("resources/mapas/primeiraFase.jpeg"))
    fases.append(Sprite("resources/mapas/segundaFase.jpeg"))
    fases.append(Sprite("resources/mapas/terceiraFase.jpeg"))
    fases.append(Sprite("resources/mapas/mapaCompleto.jpeg"))
    return fases

def inicializaFases(window: Window):
    fases = []

    pantanal = Sprite("resources/botoes/pantanal.png")
    pantanal.x = (1 * window.largura/4) - pantanal.width/2
    pantanal.y = (1 * window.altura/4) - pantanal.height/2

    amazonia = Sprite("resources/botoes/amazonia.png")
    amazonia.x = (1 * window.largura/4) - amazonia.width/2
    amazonia.y = (3 * window.altura/4) - amazonia.height/2

    pampa = Sprite("resources/botoes/pampa.png")
    pampa.x = (3 * window.largura/4) - pampa.width/2
    pampa.y = (1 * window.altura/4) - pampa.height/2

    caatinga = Sprite("resources/botoes/caatinga.png")
    caatinga.x = (3 * window.largura/4) - caatinga.width/2
    caatinga.y = (3 * window.altura/4) - amazonia.height/2

    fases.append(pantanal)
    fases.append(amazonia)
    fases.append(pampa)
    fases.append(caatinga)

    return fases

def inicializaBotoes(window: Window):
    banner = Sprite("resources/mapas/banner.jpeg")
    start = Sprite("resources/botoes/start.png")
    start.x = (window.largura/2 - start.width/2) - 6.5
    start.y = (3 * window.altura/5) - start.height/2
    mapa = Sprite("resources/botoes/mapa.png")
    mapa.x = window.largura/2 - mapa.width/2
    mapa.y = (2 * window.altura/7) - mapa.height/2
    info = Sprite("resources/botoes/info.png")
    info.x = window.largura/2 - info.width/2
    info.y = (5 * window.altura/7) - info.height/2

    return start, mapa, info, banner

def inicializaNiveis():
    niveis = []
    niveis.append(level1Pantanal)
    niveis.append(level2amazonia)
    niveis.append(level3Pampa)
    niveis.append(level4Caatinga)

    return niveis

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