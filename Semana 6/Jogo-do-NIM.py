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


op = int

def main():
    print ('Bem-vindo ao jogo do NIM! Escolha: ')
    print ('1 - para jogar uma partida isolada')
    print ('2 - para jogar um campeonato 2')
    op = int(input(''))
    if op == 1:
        print ('Voce escolheu uma partida!')
        partida()
    elif op == 2:
        print ('Voce escolheu um campeonato!')
        campeonato()

def partida():
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    
    if n % (m + 1) != 0:
        print ('Computador começa!')
        vez = True
    elif n % (m + 1) == 0:
        print ('Você começa!')
        vez = False
        
    while n > 0:
        if vez :
            comptirou = computador_escolhe_jogada(n,m)
            vez = False
            print (f'O computador tirou {comptirou} peças.')
            n -= comptirou 
        else :
            jogadortirou = usuario_escolhe_jogada(n,m)
            vez = True
            print (f'Você tirou {jogadortirou} peças.')
            n -= jogadortirou
            
        print (f'Agora restam {n} peças no tabuleiro')
        
    if vez :
        print ('Você ganhou!')
        return 1
    else :
        print ('Computador ganhou!')
        return 0
    
def campeonato():
    nrodada = 1
    winusuario = 0
    wincomputador = 0
    while nrodada <= 3:
        print (f'**** Rodada {nrodada} ****')
        vencedor = partida()
        if vencedor == 1:
            winusuario += 1
        else:
            wincomputador += 1
        print ('**** Final do campeonato! ****')
        print (f'Placar: Você {winusuario} X {wincomputador} Computador')

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
    while tirada > n or tirada < 1 or tirada > m:    
        print ('Oops ! Jogada inválida ! Tente de novo.')
        tirada = int(input('Quantas peças você vai tirar?' ))
    print (f'Você tirou {tirada} peças.')
    print (f'Agora resta apenas {n - tirada} peças no tabuleiro')
    return tirada
    
main ()