class contaBancaria:
    def __init__(self,numero,titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor 

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)     

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Lhe falta bufunfas.")  

#aqui estou criando ua instancia do objeto contaBancaria
#com o nome de conta_do_Luan
numero_conta = input("Digite o numero da conta")
titular_conta = input("Digite o tiular da conta:")
saldo_inicial = float(input("Digite o saldo inicial da sua conta:").replace(",","."))

conta_do_Luan = contaBancaria(numero_conta, titular_conta, saldo_inicial)
#usando os metodos do objeto contaBancaria
valor_deposito = float(input("Digite o valor de depósito: ").replace(",","."))
valor_saque = float(input("Digite o valor a ser sacado").replace(",","."))


conta_do_Luan.depositar(valor_deposito)
conta_do_Luan.sacar(valor_saque)

conta_do_Luan.exibir_detalhes()
