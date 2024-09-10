class Livros():
    def __init__(self,nome):
        self.autor=""
        self.genero=""


biblioteca={}

def mostrar():
    pass

def iniciar():
    
    chat= input("Digite o nome do livro, ou fim para sair:")
    while chat != "fim":
        autor=input("digite o autor")
        genero=input("digite o genero")
        chat = Livros(chat)
        chat.autor=autor
        chat.genero=genero
        biblioteca[chat]= autor , genero
        chat= input("Digite o nome do livro, ou fim para sair:")
      

#começo do programa
iniciar()
for k , v in biblioteca.items():
    print(k , v , v )
