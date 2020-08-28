import adivinhacao

def selecionar_jogo():
    print("Selecione o jogo que você quer jogar, I para Adivinhacao, e II para Forca")

    jogo_selecionado = int(input("Defina sua opção"))

    if(jogo_selecionado == 1):
        adivinhacao.jogar()
    else:
        print("Ainda não há outra opcao")

if(__name__ == '__main__'):
    selecionar_jogo()
