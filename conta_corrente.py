class Conta():
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def  deposito_e_saque(self, valor):
        self.saldo = self.saldo + valor
        print(f"seu saldo agora é de: {self.saldo}")

        pass
    
numero = int(input("numero da conta"))
nome = input("nome da conta: ")
saldo = float(input("saldo da conta: "))
usuario = Conta(numero, nome, saldo) 

print(vars(usuario))
escolha = input("quer fazer um deposito ou saque: 'd' para deposito / 's' para saque: ")

if escolha == 's':
    valor = float(input("digite valor do saque: "))
    if valor > saldo:
        print("o valor escolhido é maior que o saldo, operação não realizada")
    else:    
        valor = valor - valor * 2
        usuario.deposito_e_saque(valor)
elif escolha == 'd':
     valor = float(input("digite valor do deposito: "))
     usuario.deposito_e_saque(valor)
else:
    print("erro você pode digitar apenas: 'd' ou 's'")     