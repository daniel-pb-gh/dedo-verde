

class GerenciadorHordas():
    def __init__(self, poluicoesTemplate: list[dict]):
        self.tempoPercorrido = 0
        self.filaSpawnPoluicoes = poluicoesTemplate.copy()
        #pra ficar em ordem de quem sai primeiro
        self.filaSpawnPoluicoes.sort(key=lambda Item: Item["tempo"])
        
    def processarSpawns(self, deltaTime):
        self.tempoPercorrido += deltaTime
        poluicoesParaSpawn = []

        while (len(self.filaSpawnPoluicoes) > 0) and (self.tempoPercorrido > self.filaSpawnPoluicoes[0]["tempo"]):
            novaPoluicao = self.filaSpawnPoluicoes.pop(0)
            poluicoesParaSpawn.append(novaPoluicao)

        return poluicoesParaSpawn
        