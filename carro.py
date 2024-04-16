class Carro:
    def _init_(self, marca, modelo, cor, ano):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def exibir_informacoes(self):
        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("cor: ", self.cor)
        print("ano: ", self.ano)

carro1 = Carro("Toyota", "corolla", "Prata", 2002)
carro2 = Carro("Honda", "Civic", "Preto", 2023)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()