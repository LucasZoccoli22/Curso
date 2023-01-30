
def computador_escolhe_jogada(n, m):
        print("Vez do computador")
        if n <= m:
            return n
        else:
            quantia = n % (m + 1)


        if quantia > 0:

            return quantia


        return m

            



def usuario_escolhe_jogada(n, m):

    

    print("Sua vez!")


    jogada = 0


    while jogada == 0:

        jogada = int(input("Quantas peças irá tirar?: "))


        if jogada > n or jogada < 1 or jogada > m:

            jogada = 0


    return jogada



def campeonato():

    numeroRodada = 1

    usuario = 0

    computador = 0


    while numeroRodada <= 3:

        print('**** Rodada', numeroRodada, '* ***')

        

        vencedor = partida()

        

        if vencedor == 1:

            usuario += 1

        else:

            computador += 1

            print('Placar: Voce', usuario,"X", computador, 'Computador')


        numeroRodada += 1




def partida():

    

    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogadas? '))

    

    vezDoPC = False

    

    if n % (m + 1) == 0:

        vezDoPC = False

        print('Voce começa!')

        

    elif n % (m + 1) != 0:

        vezDoPC = True

        print('Computador começa!')

        

        

    while n > 0:

        

        if vezDoPC:

            computadorRemove = computador_escolhe_jogada(n, m)

            vezDoPC = False

            print('O computador tirou', computadorRemove, 'peças')


        else:

            jogadorRemove = usuario_escolhe_jogada(n, m)

            vezDoPC = True

            print('Você tirou', jogadorRemove, 'peças')

            

        n = n - computadorRemove


        print("Restam apenas", n,"peça(s) no tabuleiro")



    if vezDoPC:

        print("Você ganhou!")

        return 1

    else:

        print("Computador ganhou!")

        return 0




tipo_jogo = 0


print("Bem Vindo ao Jogo NIN! Faça sua escolha: ")

print(" ")

print("1 = Para jogar uma partida")

print("2 = Para jogar um campeonato")


while tipo_jogo == 0:


    tipo_jogo = int(input("Sua escolha: "))


    if tipo_jogo == 1:

        print("modo partida!")

        partida()

        break

    elif tipo_jogo == 2:

        print("modo campeonato!")

        campeonato()

        break

    else:

        print("Opção inválida")

        tipo_jogo = 0