from __future__ import annotations
from typing import TYPE_CHECKING
from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.sound import Music
from botoes import *
from arquivo import *
from level1_amazonia import youWin, gameOver

window = Window(800, 600, "menu")

#janela
window.set_background_color((103, 199, 100))

#musica
musicaMenu = Music("resources/Music/Ambient 9.ogg")
musicaMenu.play()

start, mapa, info = inicializaBotoes(window)

mapas = inicializaMapa()
numeroMapaAtual = 0
mapaAtual = mapas[numeroMapaAtual]

fases = inicializaFases(window)

niveis = inicializaNiveis()
nivelSelecionado = 0
niveisVencidos = 0

#flag
gameState = "start"

#input
keyboard = Keyboard()
mouse = Mouse()

while True:

    if gameState == "start": 
        start.draw()
        window.update()
        if mouse.button_down(1):
            if ((mouse.is_over_object(start))):
                gameState = "menu"
                window.update()

    elif gameState == "menu":
        mapa.draw()
        info.draw()
        window.update()

        if mouse.button_down(1):
            if ((mouse.is_over_object(mapa))):
                gameState = "mapa"
                window.update()
            elif ((mouse.is_over_object(info))):
                gameState = "info"
                window.update()

    elif gameState == "mapa":
        niveisVencidos = fasesConcluidas()
        mapaAtual = mapas[niveisVencidos]
        mapaAtual.draw()

        for fase in fases:
            fase.draw()
        if mouse.button_down(1):
            for i in range(niveisVencidos + 1):
                if ((mouse.is_over_object(fases[i]))):
                        gameState = "game"
                        nivelSelecionado = i
                        window.update()
        
        window.update()

    elif gameState == "info":
        window.update()

    elif gameState == "game":
        musicaMenu.pause()
        venceu = niveis[nivelSelecionado]()

        if venceu == 1:
            youWin()
            escreveFase(nivelSelecionado + 1)
        else:
            gameOver()

        gameState = "mapa"
        musicaMenu.play()
        window.update()