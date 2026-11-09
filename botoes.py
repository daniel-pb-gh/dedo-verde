from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.sprite import Sprite
from level1_amazonia import level1amazonia

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
    start = Sprite("resources/botoes/start.png")
    start.x = window.largura/2 - start.width/2
    start.y = window.altura/2 - start.height/2
    mapa = Sprite("resources/botoes/mapa.png")
    mapa.x = window.largura/2 - mapa.width/2
    mapa.y = (2 * window.altura/7) - mapa.height/2
    info = Sprite("resources/botoes/info.png")
    info.x = window.largura/2 - info.width/2
    info.y = (5 * window.altura/7) - info.height/2

    return start, mapa, info

def inicializaNiveis():
    niveis = []
    niveis.append(level1amazonia)
    niveis.append(level1amazonia)
    niveis.append(level1amazonia)
    niveis.append(level1amazonia)

    return niveis