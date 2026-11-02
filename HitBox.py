from PPlay.gameobject import GameObject

class HitBox(GameObject):
    def __init__(self, largura, altura):
        super().__init__()
        self.width = largura
        self.height = altura