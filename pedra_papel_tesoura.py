from random import randint
import os

jogadas=["pedra","papel","tesoura"]
pontos=0
def clear():
    os.system('cls')

def sortear():
    sopa = randint(0,2)
    return sopa

def errou():
    print("VOCE PERDEU!")


    

def menu():
    print("---------------PEDRA-PAPEL-TESOURA-----------------")
    print("1- iniciar jogo")
    print("2- ver pontuação")
    print("3- sair do jogo")
    print("---------------------------------------------------")
    chat = input("digite sua opção : ")
    if chat == "1":
        pass
    elif chat == "2":
        clear()
        print("voce tem :",pontos," pontos")
        v=input("digite menu para voltar para o menu")
        clear()
        menu()
    elif chat == "3":
        clear()
        print("programa finalizado!")

def checagem():
    if jog == bot:
        print(f"{jog} X {bot} - EMPATE")
        return 3
    elif jog == "pedra" and bot=="papel":
        print(f"{jog} X {bot} - DERROTA")
        return 1
    elif jog == "pedra" and bot=="tesoura":
        print(f"{jog} X {bot} - VITÓRIA")
        return 2
    elif jog == "tesoura" and bot=="pedra":
        print(f"{jog} X {bot} - DERROTA")
        return 1
    elif jog == "tesoura" and bot=="papel":
        print(f"{jog} X {bot} - VITÓRIA")
        return 2
    elif jog == "papel" and bot=="tesoura":
        print(f"{jog} X {bot} - DERROTA")
        return 1
    elif jog == "papel" and bot=="pedra":
        print(f"{jog} X {bot} - VITÓRIA")
        return 2
    elif jog == "menu":
        clear()
        menu()

menu()

while True:
    bot=jogadas[sortear()]
    sortear()
    jog=input("escolha sua jogada pedra , papel ou tesoura e menu caso deseje voltar: ")

    if checagem() == 2:
        pontos=pontos+1
    