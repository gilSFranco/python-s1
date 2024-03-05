import os

os.system('cls')

pontuacao = [0, 0, 0, 0]

count = 1
while count < 5:
    print(f"\n{'*' * 5} {'Quiz - Sobre The Last Of Us(TLOU)'} {'*' * 5}")
    print("Quem matou joel?\n")
    print("A) - Abby.\nB) - Jesse.\nC) - Nora.\nD) - Marlene.")
    print(f"{'*' * 5} {'Quiz - Sobre nosso luizinho'} {'*' * 5}\n")

    escolha = input(f"Usuario {count}, escolha uma das opções: ")

    if escolha == "A":
        pontuacao[1] += 1

    print(f"\n{'*' * 5} {'Quiz - Sobre The Last Of Us(TLOU)'} {'*' * 5}")
    print("Por que a Ellie fez uma tatuagem em seu braço na parte II?\n")
    print("A) - Para irritar o joel, que não gosta de tatuagens.\nB) - Por puro estilo.\nC) - Para esconder a marca da mordida.\nD) - Por que ela se queimou.")
    print(f"{'*' * 5} {'Quiz - Sobre nosso luizinho'} {'*' * 5}\n")

    if escolha == "C":
        pontuacao[1] += 1

    count += 1