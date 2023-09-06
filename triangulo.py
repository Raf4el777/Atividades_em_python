class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, base, altura):
        self.base = base
        self.altura = altura
    
    def resultado(self):
        area = (self.base * self.altura) / (1/2)
        perimetro = 2 * (self.altura + self.base)
        print(f"a area: {area} e o perimetro: {perimetro}")
        pass

