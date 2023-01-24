print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas > 0:  # hile para testar se ainda há rodadas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # funcao .format
    print("tentativa numero ")
    chute_str = input("Digite o seu numero: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
    else:
        if maior:
            print("Você errou o seu chute foi maior que o numero secreto.")
        elif menor:
            print("Você errou o seu chute foi menor que o numero secreto.")

    rodada = rodada + 1  # Depois do elif, mas antes do último print, incrementar a variável rodada:

print("Fim do Jogo")
