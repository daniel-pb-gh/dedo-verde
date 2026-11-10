from __future__ import annotations
from PPlay.sprite import Sprite
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Planta import Planta

class Poluicao(ABC, Sprite):
    def __init__(self, caminho_imagem, total_frames=1, animacoes=None):
        super().__init__(caminho_imagem, total_frames)
        self.linha = None
        self.pontosDeVida: float
        self.estado = "andando"
        self.dano: int
        self.cooldownTime: int
        self.currentCooldown: float
        self.pace: int

        # estado -> (frame_inicial, frame_final, segundos_por_frame) ## "estado" é a chave do dicionario
        self.animacoes = animacoes or {"andando": (0, total_frames - 1, 0.1)}
        # cada objeto é 1 spritesheet cheio de animações, então só tocam as partes certas dependendo da animação
        self._estadoAnimado = None   # último estado que configurou a animação


    @classmethod
    def fabricaPoluicao(cls, poluicao: dict):
        novaPoluicao = None
        match poluicao["tipo"]:
            case "plastico":
                return Plastico(poluicao["linha"])
            case "oleo":
                return Oleo(poluicao["linha"])
            case error:
                print("não tem essa poluicao")   
                return None 

    def deveAndar(self):
        if self.estado == "andando":
            return True
        return False

    def ataque(self, planta: Planta):
        planta.pontosDeVida -= self.dano

    def atacar(self, plantasVivas: list[Planta], deltaTime):
        self.estado = "andando"
        
        if self.currentCooldown > 0:
            self.currentCooldown -= deltaTime

        for planta in plantasVivas:
            if self.collided(planta.hitBox):
                self.estado = "atacando"
                if self.currentCooldown <= 0:
                    self.ataque(planta)
                    self.currentCooldown = self.cooldownTime
                    if planta.pontosDeVida <= 0:
                        plantasVivas.remove(planta)
                break

    def moverPoluicao(self, deltaTime):
        self.x -= self.pace * deltaTime

    def atualizarAnimacao(self): ## TEM QUE SER CHAMADA DEPOIS DE ATACAR
        if self.estado != self._estadoAnimado:
            self._estadoAnimado = self.estado
            inicio, fim, tempo = self.animacoes.get(
                self.estado, self.animacoes["andando"])
            self.set_intervalo_frames(inicio, fim)  # trecho da folha
            self.set_curr_frame(inicio)             # recomeça do início
            self.tempo_por_frame = tempo            # velocidade deste estado
            self.tempo_acumulado = 0
            self.rodando = True
        self.update()  # avança os quadros (Animation.update)


class Plastico(Poluicao):
    def __init__(self, linha: int):
        super().__init__(
            "resources/spritePlastico.png",
            total_frames=999,
            animacoes={
                "andando": (0, 3, 0.15),
                "atacando": (4, 6, 0.10),
            },           
        )
        self.pontosDeVida = 40
        self.linha = linha
        self.dano = 75
        self.cooldownTime = 2
        self.currentCooldown = 0
        self.pace = 50

class Oleo(Poluicao):
    def __init__(self, linha: int):
        super().__init__(
            "resources/spriteOleo.png",
            total_frames=8,
            animacoes={
                "andando":  (0, 3, 0.20),
                "atacando": (4, 6, 0.15),
            },
        )
        self.pontosDeVida = 30
        self.linha = linha
        self.dano = 90
        self.cooldownTime = 3
        self.currentCooldown = 0
        self.pace = 30