#listas
listcpf=[]
listcnpj=[]

#classe pai
class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

#classe filho cpf
class Pessoacpf(Pessoa):
    def __init__(self, nome, idade,cpf):
        super().__init__(nome, idade)
        self.cpf=cpf
    def __str__(self):
        return f"nome:{self.nome} - idade: {self.idade}- cpf:{self.cpf}"
    
#classe filho cnpj
class Pessoacnpj(Pessoa):
    def __init__(self, nome, idade,cnpj):
        super().__init__(nome, idade)
        self.cnpj=cnpj
    def __str__(self):
        return f"nome:{self.nome} - idade: {self.idade}- cnpj:{self.cnpj}"

#registrar cpf
def registrar_cpf():
    nome=input("digite seu nome:")
    idade = input("digite sua idade")
    cpf=input("digite seu cpf")
    p=Pessoacpf(nome,idade,cpf)
    listcpf.append(p)


#registrar cnpj
def registrar_cnpj():
    nome=input("digite seu nome:")
    idade = input("digite sua idade")
    cnpj=input("digite seu cnpj")
    p=Pessoacpf(nome,idade,cnpj)
    listcnpj.append(p)
    
#mostrar resultados
def mostrar():
    print("----------cpf----------")
    for x in listcpf:
        print(x)
    print("----------cnpj----------")
    for y in listcnpj:
        print(y)

#inicio
choose=input("digite cpf ou cnpj para decidir a forma de registro e digite fim para sair")
while choose != "fim":
    
    if choose == "cpf":
        registrar_cpf()
    elif choose== "cnpj":
        registrar_cnpj()
    elif choose =="sair":
        break
    elif choose=="mostrar":
        mostrar()
    choose=input("digite cpf ou cnpj para decidir a forma de registro e digite fim para sair")

