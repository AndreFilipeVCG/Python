#classe pai
class veiculos:
    def __init__(self,marca,preço,ano):
        self.marca=marca
        self.preço=preço
        self.ano=ano

#classe filha
class carro(veiculos):
    def __init__(self, marca, preço, ano,portas):
        super().__init__(marca, preço, ano)
        self.portas=portas
    def info(self):
        print("-------informaçoes---------")
        print("marca:",str(self.marca))
        print("preço:",str(self.preço))
        print("ano:",str(self.ano))
        print("portas:",str(self.portas))

carlist=[]

c1 = carro("audi",1000000,1997,4)
c2 = carro("audi",800000,2002,4)
c3 = carro("ferrari",12000000,2023,4)
c4 = carro("honda",50000,1999,4)
carlist.append(c1)
carlist.append(c2)
carlist.append(c3)
carlist.append(c4)



for x in carlist:
    print(x.marca)
    x.info()