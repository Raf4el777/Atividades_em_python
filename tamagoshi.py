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
        self.humor = saude + fome

    #def fome(self):

    #def saude(self):

    #def humor(self):


        pass

    