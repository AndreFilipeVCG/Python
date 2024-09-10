import os

def clear():
    os.system('cls')    

lista=[]
som=1
class Tarefas:
    def __init__(self,task,descrição):
        self.task=task
        self.descrição=descrição
        self.concluida=False
    def __str__(self):
        estado = "concluida" if self.concluida else "não concluida"
        return f"------------------\ntarefa : {self.task} \ndescrição: {self.descrição}  \nestado : {estado}\n------------------"
    
def menu():
    print("-----------------MENU--------------------")
    print("1-adicionar nova tarefa")
    print("2-marcar tarefa como concluida")
    print("3-remover tarefa da lista")
    print("4-mostrar toda a lista")
    print("5-sair")
    print("-----------------------------------------")
    chat=input("escolha sua opção ! : ")
    clear()
    if chat == "1":
        opção1()
    elif chat =="2":
        som=1
        opção2(som)
    elif chat == "3":
        som=1
        opção3(som)
    elif chat == "4":
        opção4()
    elif chat == "5":
        opção5()
    else:
        menu()
def opção1():
    print("------------ADD-TASKS---------------")
    título=input("Dígite o nome de sua tarefa : ")
    descr=input("digite a descrição de sua tarefa : ")
    taks=Tarefas(título,descr)
    clear()
    lista.append(taks)
    menu()

def opção2(cont):
    print("------------DONE-TASKS---------------")
    for x in lista:
        print(cont,x)
        cont=cont+1
    op=int(input("digite o número da tarefa que deseja marcar como concluida : "))
    num=op-1
    lista[num].concluida = True
    clear()
    menu()

def opção3(cont):
    print("------------REMOVE-TASK---------------")
    for x in lista:
       
        print(cont,x)
        cont=cont+1
    ex=int(input("digite o número da tarefa que deseja excluir : "))
    num = ex-1
    lista.pop(num)
    clear()
    menu()



def opção4():
    print("------------ALL-TASKS---------------")
    for x in lista:
        print(x)
    volt=input("digite voltar para voltar para o menu : ")    
    while volt != "voltar":
        volt=input("digite voltar para voltar para o menu : " )
    if volt=="voltar":
        clear()
        menu()

def opção5():
    print("------PROGRAMA FINALIZADO------")


def iniciar():
    menu()
####################
iniciar() 
