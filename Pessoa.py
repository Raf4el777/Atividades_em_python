class Pessoa():
    def __init__(self,nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        self.idade = self.idade + anos
        if self.idade < 21:
            self.altura = self.altura + 0.05
        

    def engordar(self, k):
        self.peso = self.peso + k

    def emagreceer(self, k):
        self.peso = self.peso - k

    def crescer(self, metros):
        self.altura = self.altura + metros

        pass

p = Pessoa("Manuel gomes", 19, 75, 1.80)
print(vars(p))
p.envelhecer(1)
print(vars(p))
p.engordar(5)
print(vars(p))
p.emagreceer(1)
print(vars(p))
p.crescer(0.01)
print(vars(p))