import os
from random import randint

palavras=["pierre"]
letras=[]
num=5

def clear():
    os.system('cls')
def adicionar():
    chat=input("\ndigite uma letra : " )
    letras.append(chat)

while num > 0:
    adicionar()
    clear()
    for x in palavras[0]:
        if x in letras:
            print(x,end="")
        else:
            print("_",end="")
    num=num+1