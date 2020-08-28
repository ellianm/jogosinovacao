import random

def jogar():
    print("Bem vindo a Forca!")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_objetivo = palavras[numero]
    print(palavra_objetivo)

    letras_encontradas = ["_" for letra in palavra_objetivo]
    print(letras_encontradas)
    print("Agora nossa IDE está acoplada diretamente ao projeto")

    print("END GAME")

if(__name__ == "__main__"):
    jogar()