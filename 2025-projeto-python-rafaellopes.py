'''
Avaliação prof berssa
Rafael Lopes
2025/07/02
'''

import random  # Importa o módulo para escolher palavra aleatória

# Lista de palavras para o jogo
palavras = ['python', 'banana', 'computador', 'carro', 'gato']

# Escolhe uma palavra aleatória da lista
palavra = random.choice(palavras)

tentativas = 6  # Número de chances para errar
letras_certas = []  # Lista para guardar as letras que o jogador acertou

print("Jogo da Forca")  # Mensagem inicial

while tentativas > 0:
    mostrar = ""  # String para mostrar o progresso da palavra

    # Monta a palavra mostrando letras acertadas e _ para as não acertadas
    for letra in palavra:
        if letra in letras_certas:
            mostrar += letra  # Mostra a letra acertada
        else:
            mostrar += "_"  # Mostra underline para letra não descoberta

    print(mostrar)  # Exibe a palavra formatada

    # Se a palavra estiver completa, jogador venceu
    if mostrar == palavra:
        print("Você ganhou!")
        break  # Sai do loop

    tentativa = input("Digite uma letra: ")  # Pede uma letra ao jogador

    if tentativa in palavra:
        letras_certas.append(tentativa)  # Adiciona letra correta na lista
    else:
        tentativas -= 1  # Diminui as tentativas se errou
        print("Errou! Tentativas restantes:", tentativas)

# Se acabar as tentativas, jogador perdeu
if tentativas == 0:
    print("Você perdeu! A palavra era:", palavra)