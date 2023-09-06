class Quadrado():
    def __init__(self,lado):

        self.lado = lado

    def mudar_lado(self, lado):

        self.lado = lado

    def val_lado(self):

        return self.lado
    
    def resultado(self):
        self.result = self.lado * self.lado

        return self.result

lado = int(input("tamanho do lado: "))
quadra = Quadrado(lado)
quest = input("deseja mudar o lado: 's' ou 'n' :  ")

if quest == 's' or quest == 'S':
    lado = int(input("tamanho do lado: "))
    quadra.mudar_lado(lado)
    print(f"o resultado é: {quadra.resultado()}")
    print(f"o lado é: {quadra.val_lado()}")
elif quest == 'n' or quest == 'N' :
    print(f"o resultado é: {quadra.resultado()}")
    print(f"o lado é: {quadra.val_lado()}")
else:
    print("favor digitar: 's' ou 'n'")  

