class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def resultado(self):
        area = (self.base * self.altura) / (1/2)
        perimetro = 2 * (self.altura + self.base)
        print(f"base: {self.base}, altura: {self.altura}, area: {area}, perimetro: {perimetro}")
        pass

base = float(input("valor da base: "))
altura = float(input("valor da altura: "))

ret = Retangulo(base, altura)
ret.resultado()
