import random
from art import logo

def print_maos(player, dealer):
    print(f"Dealer: {dealer[0]}, X")
    print(f"Player: {', '.join(map(str, player))}")

def hit(player):
    player.append(random.randint(2, 11))

def double_down(player, aposta):
    aposta *= 2
    hit(player)

def stand():
    return True

def split(player, aposta):
    if player[0] == player[1]:
        aposta *= 2
        return [player[0]], [player[1]]
    else:
        print("Você não pode dividir essas cartas.")
        return player, aposta

def jogar_blackjack():
    print(logo)
    print("Bem-vindo ao jogo de Blackjack!")
    nome = input("Digite seu Nome: ")
    aposta = float(input("Digite sua aposta: "))
    dealer = [random.randint(2, 11), random.randint(2, 11)]
    player = [random.randint(2, 11), random.randint(2, 11)]
    print_maos(player, dealer)

    while True:
        acao = input("O que você quer fazer? (hit, stand, double down, split): ").lower()
        if acao == "hit":
            hit(player)
            print_maos(player, dealer)
        elif acao == "stand":
            print("Você escolheu stand.")
            break
        elif acao == "double down":
            double_down(player, aposta)
            print_maos(player, dealer)
            break
        elif acao == "split":
            player, aposta = split(player, aposta)
            print_maos(player, dealer)
            break

    pontuacao_dealer = sum(dealer)
    while pontuacao_dealer < 17:
        dealer.append(random.randint(2, 11))
        pontuacao_dealer = sum(dealer)

    pontuacao_player = sum(player)

    print(f"Pontuação do dealer: {pontuacao_dealer}")
    print(f"Pontuação do jogador: {pontuacao_player}")

    if pontuacao_player > 21:
        print("Você estourou! Dealer ganhou.")
    elif pontuacao_dealer > 21:
        print("Dealer estourou! Você ganhou.")
    elif pontuacao_player > pontuacao_dealer:
        print("Você ganhou!")
    elif pontuacao_player < pontuacao_dealer:
        print("Dealer ganhou.")
    else:
        print("Empate!")

jogar_blackjack()
