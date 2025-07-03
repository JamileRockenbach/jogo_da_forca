# jogo da forca!
import os, time
from funcoes import limparTela, aguarde

forca = [
    '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    '''
]

def salvar_ranking(vencedor, perdedor, palavra):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Vencedor: {vencedor} | Perdedor: {perdedor} | Palavra: {palavra}\n")

while True:
    limparTela()
    desafiante = input("Digite o nome do desafiante: ")
    competidor = input("Digite o nome do competidor: ")
    print(f"{desafiante} vs. {competidor}, boa sorte!")
    aguarde(3)
    limparTela()

    while True:
        palavra_chave = input(f"{desafiante}, qual é a palavra-chave: ")
        palavra_chave = palavra_chave.upper()
        if len(palavra_chave) < 3:
            print("A palavra tem que ser pelo menos 3 letras!!")
            aguarde(3)
        else:
            break

    secreta = ""
    for letra in palavra_chave:
        if letra != " ":
            secreta += "*"
        else:
            secreta += "-"

    while True:
        dica1 = input(f"{desafiante}, digite a primeira dica: ")
        dica2 = input(f"{desafiante}, digite a segunda dica: ")
        dica3 = input(f"{desafiante}, digite a terceira dica: ")
        if dica1 == dica2 or dica1 == dica3 or dica2 == dica3:
            print("As dicas NÃO podem ser iguais :)")
            aguarde(3)
        else:
            break

    while True:
        contador_dicas = 0
        erros = 0
        letras_erradas = []

        while True:
            limparTela()
            print("Palavra-chave:", secreta)
            print("Total de erros:", erros)
            print(forca[erros])
            print("Letras erradas:", " ".join(letras_erradas))
            print("(1) Jogar!")
            print("(2) Dicas!")
            print("(3) Desistir.")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Jogando...")
                letra = input(f"Digite uma letra ou palavra {competidor}: ").upper()
                if len(letra) > 1:
                    if letra == palavra_chave:
                        print("Você acertou a palavra!!")
                        break
                    else:
                        print("Palavra incorreta!")
                        erros += 1
                else:
                    acertou = False
                    secreta = list(secreta)
                    posicao = 0
                    for letraPalavra in palavra_chave:
                        if letra == letraPalavra:
                            acertou = True
                            secreta[posicao] = letra
                        posicao += 1
                    secreta = "".join(secreta)

                    if acertou:
                        print("Você acertou a letra!")
                        if "*" not in secreta:
                            print("Você ganhou!")
                            salvar_ranking(competidor, desafiante, palavra_chave)
                            break

                    else:
                        if letra not in letras_erradas:
                            letras_erradas.append(letra)
                        erros += 1
                        print("Você errou a letra!")

                if erros >= len(forca) - 1:
                    print(forca[erros])
                    print("Você perdeu!")
                    print(f"A palavra era: {palavra_chave}")
                    salvar_ranking(desafiante, competidor, palavra_chave)
                    break

            elif opcao == "2":
                contador_dicas += 1
                print("Dicas:")
                if contador_dicas == 1:
                    print(f"Dica 1: {dica1}")
                elif contador_dicas == 2:
                    print(f"Dica 2: {dica2}")
                elif contador_dicas == 3:
                    print(f"Dica 3: {dica3}")
                else:
                    print("Você já usou todas as dicas.")
                aguarde(2)

            elif opcao == "3":
                print("Você desistiu do jogo.")
                print(f"A palavra era: {palavra_chave}")
                break
            else:
                print("Opção inválida. Tente novamente.")
                aguarde(2)

        opcao = input("Deseja jogar novamente? (n-não e qualquer coisa para sim): ")
        if opcao.lower() == "n":
            print("Obrigado por jogar!")
            print("\n===== RANKING =====")
            try:
                with open("ranking.txt", "r", encoding="utf-8") as arquivo:
                    print(arquivo.read())
                    aguarde(7)
            except FileNotFoundError:
                print("Nenhuma partida registrada ainda.")
                aguarde(7)
            break