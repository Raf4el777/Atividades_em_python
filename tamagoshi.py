"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que
devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não
devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""

class Tamagoshi():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = (self.saude + self.fome) / 2

    def fomes(self):
        self.fome = 100
        self.humor = (self.saude + self.fome) / 2

    def saudes(self):
        self.saude = 100
        self.humor = (self.saude + self.fome) / 2

    def cansado(self):
        self.fome = self.fome - 20
        self.saude = self.saude - 20
        self.humor = (self.saude + self.fome) / 2
        pass

bicho = Tamagoshi("tomy", 40, 70, 13)
print(vars(bicho))




print("""TABELA DE OPCOES:
      OPCAO 1: ALIMENTAR
      OPCAO 2: BRINCAR
      OPCAO 3: CANTAR
      OPCAO 4: DANCAR
      digita 0 para terminar""")


fim = True
cont = 0
while fim == True :
    opcao = int(input("escreva a opcao:"))
    
    
    
        

    if opcao == 1:
        bicho.fomes()
        print(vars(bicho))
    elif opcao == 2:
        bicho.saudes()
        print(vars(bicho))
    elif opcao == 3:
        cont = 3
        
    elif opcao == 4:
        cont = 3
                  
    else:
        break


    if cont == 3:
        bicho.cansado()
        print(vars(bicho))
        cont = 0