# N é o número de peças iniciais
# M é o número de peças máximas retiradas por rodada
# Se n é multiplo de m+1 o usuário começa
#O computador deve sempre retirar o número de peças máximo, sendo múltiplo de m+1
# Modos de jogo
    # Opção 1- Uma partida
    # Opção 2- Campeonato melhor 3
# receba quantas peças
# receba limite de peças retirada por jogada
# Para começar
    #
# começou
    # O computador tira peças aleatórias
    # Printa quantas peças restam
    # Pergunta quantas peças vc vai tirar
    # 
import random

op = int
qmcomeça = int
def main():
    print ('Bem-vindo ao jogo do NIM! Escolha: ')
    print ('1 - para jogar uma partida isolada')
    print ('2 - para jogar um campeonato 2')
    op = int(input(''))
    if op == 1:
        partida()

def partida():
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    quemcomeça(n,m)
    if qmcomeça == 1:
        #Computador começa
        while  n >= 0:
            computador_escolhe_jogada(n,m)
            n -= computador_escolhe_jogada
            vencedor = ('Fim do jogo! O computador ganhou !')
            if n != 0:
                usuario_escolhe_jogada(n,m)
                n -= usuario_escolhe_jogada
                vencedor = ('Fim do jogo! Você ganhou !')
        print (vencedor)
        
    elif qmcomeça == 2:
        #Usuário começa
        while n >= 0:
            usuario_escolhe_jogada(n,m)
            n -= usuario_escolhe_jogada
            vencedor = ('Fim do jogo! Você ganhou !')
            if n != 0:
                computador_escolhe_jogada(n,m)
                n -= computador_escolhe_jogada
                vencedor = ('Fim do jogo! O computador ganhou !')
        print (vencedor)
            
def quemcomeça(n,m):
    #FEITO
    #Escolhe quem começa com base N/M
    if n % (m + 1) != 0:
        print ('Computador começa!')
        qmcomeça = 1
    elif n % (m + 1) == 0:
        print ('Voce começa!')
        qmcomeça = 2
    return qmcomeça

def computador_escolhe_jogada(n,m):
    if n <= m:
        return n
    else:
        quantidade = n %(m + 1)
    
    if quantidade > 0:
        return quantidade
    
    return m           
        


def usuario_escolhe_jogada(n,m):
    #FEITO 
    #RECEBE A ENTRADA DE DADOS DO USUÁRIO
    #RETORNA O QUANTO DE PEÇA FOI REMOVIDO
    tirada = int(input('Quantas peças você vai tirar?' ))
    while tirada != int and tirada > m and tirada < 1:    
        print ('Oops ! Jogada inválida ! Tente de novo.')
        tirada = int(input('Quantas peças você vai tirar?' ))
    print (f'Você tirou {tirada} peças.')
    print (f'Agora resta apenas {n - tirada} peças no tabuleiro')
    return tirada
    
main ()