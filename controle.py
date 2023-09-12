class Controle():
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, numero):
        self.canal = numero

    def aumentar(self, volume):
        self. volume = self.volume + volume
        if self.volume <= 100 :
            print(f"o volume está no: {self.volume}") 
        else:
            self.volume = 100
            print("volume no maximo")    

    def diminuir(self, volume):
        self.volume = self.volume - volume
        if self.volume > 0:
            print(f"o volume esta no: {self.volume}")
        else:
            print("está no mudo")   

        pass

canal = int(input("que canal quer ver: "))
volume = int(input("defina seu volume: "))
user = Controle(canal, volume)   
print(vars(user))
while True:
    
    cond = input("deseja mudar de canal 's' ou 'n': ")

    if cond == 's':
        num = int(input("numero do canal: "))
        user.mudar_canal(num)
        print(vars(user))
    else:
        print("continuamos na SBT")

    cond = input("deseja mudar de volume ('a' para aumentar) ou ('d' para diminuir): ")  

    if cond == 'a':
        num = int(input("+"))
        user.aumentar(num) 
        print(vars(user))     
    elif cond == 'd':
        num = int(input("-"))
        user.diminuir(num)
        print(vars(user))

    cond = input("deseja parar a execulsão 's' ou 'n': ")

    if cond == 's':
        print("paramos por aqui")
        break  
    else:
        print("execulsão continua")             