class Bola():
    def __init__(self, cor, circunferancia, material):
        self.cor = cor
        self.circunferencia = circunferancia
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor       

bola1 = Bola("branco","10","couro")
print(bola1.mostraCor())
bola1.trocarCor("preto")
print(bola1.mostraCor())