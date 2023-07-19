'''
Autor: Valmir Alves Nogueira Filho
Componente Curricular: Algoritmos I
Concluído em: 01/11/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
-------------------------------------------------------------------------------------------------------------------------------------------'''
from random import shuffle

NIVEL_1 = 4
NIVEL_2 = 9

def tabuleiro_jogo(nivel): #gera tabuleiro com números aleatórios
    tabuleiro = []
    for i in range(nivel):
        sessao = list( range(1, nivel+1) )
        shuffle(sessao)
        tabuleiro.append(sessao)
    return tabuleiro

def tabuleiro_com_x(nivel): #gera o tabuleiro visível aos jogadores, nas mesmas dimensões do tabuleiro anterior
                        # inicia-se preenchido totalmente com "X"
    tabuleiro_x = []
    for i in range(nivel):
        
        linha = []
        for j in range(nivel):
            linha.append('X')
        tabuleiro_x.append(linha)
    return tabuleiro_x

def print_tabuleiro(nivel): #imprime tabuleiro na formatação de linhas e colunas

    for i in range(nivel):

        for j in range(nivel):

            if j % nivel**(1/2) == 0 and j != 0: #cálculo para quebrar o tabuleiro nas
                                                 #colunas 2 e 4 pro nível 1, e 3 e 6 pro nivel 2
                print('|  ',end=' ')

            print(linhas[i][j], end='   ')

        print(f'|  {soma_linhas[i]} <- SOMA DA LINHA {i+1}')

        if (i+1) % nivel**(1/2) == 0: 
            print()

    for i in range(nivel):

        print(soma_colunas[i], end='   ')
    print('<- SOMA DAS COLUNAS')


def encontra_numero(sessao,numero): #coleta indice do número procurado e revela ele no tabuleiro_x
    indice = tabuleiro[sessao].index(numero)
    tabuleiro_x[sessao][indice] = '\033[0;30;32m{}\033[m' .format(tabuleiro[sessao][indice])

def soma(iniciali,finali,inicialj,finalj,passo): #faz a soma dos elementos de uma linha, coluna ou diagonal
    #ex: a 1° linha do tabuleiro é formada pelos elementos [0][0], [0][1], [1][0] e [1][1].
    #na matriz original, a primeira linha é formada por [0][0], [0][1], [0][2], [0][3].
    #para automatizar a formação da linha no formato do tabuleiro, usa-se um for que adiciona os elementos certos em uma lista pra essa linha
    #(inícioi: 0; finali: 1+1=2; inicioj: 0; finalj: 1+1=2; passo: 1) logo, os parâmetros seriam (0,2,0,2,1)
    
    soma = 0
    for i in range(iniciali, finali, passo):

        for j in range(inicialj,finalj, passo):
            elemento = tabuleiro[i][j] #tabuleiro feito pelo tabuleiro_jogo()
            soma += elemento
    return soma
    
def linha_col_diag(iniciali,finali,inicialj,finalj,passo):
    #constrói uma lista para ser uma linha, coluna ou diagonal do tabuleiro
    
    linha = []
    for i in range(iniciali, finali, passo):

        for j in range(inicialj,finalj, passo):
            elemento = tabuleiro_x[i][j] #tabuleiro feito pelo tabuleiro_x
            linha.append(elemento)
    return linha

def nao_tem_x(linhaoucoluna): #confere se a linha/coluna/diagonal já foi completamente
                              #preenchida ou não (tem "X" ou não)
    for elemento in linhaoucoluna:

        if elemento == 'X':
            return False
    return True

def pontuacao_jogo(linha_coluna_diagonal, somas, lcd): 
    # se a linha/coluna/diagonal está totalmente preenchida e sua pontuação ainda não foi contada,
    # ela é incrementada a variável pontuacao_jogador
    global pontuacao_jogador_1, pontuacao_jogador_2

    for i in range(len(linha_coluna_diagonal)):
        
        if nao_tem_x(linha_coluna_diagonal[i]) == True and lcd[i] == False:
            if jog == '1':
                pontuacao_jogador_1 += somas[i]
                print(f'\033[0;30;32m{nome_jogador_1} GANHOU {somas[i]} PONTOS\033[m', end=' ')

            else: 
                pontuacao_jogador_2 += somas[i]
                print(f'\033[0;30;32m{nome_jogador_2} GANHOU {somas[i]} PONTOS\033[m', end=' ')

            lcd[i] = True #por ser True, essa linha/coluna/diagonal não entra mais na condição acima

            if lcd is d: #se o parâmetro lcd é a variável da diagonal, a pontuação dela é dobrada,
                         #se ainda não foi contabilizada
                if jog == '1':
                    pontuacao_jogador_1 += somas[i]                    
                else:
                    pontuacao_jogador_2 += somas[i]
                print(f'\033[0;30;32m + {somas[i]}  PONTOS = {somas[i]*2} PONTOS! \nPois achou a diagonal do tabuleiro, que tem seu valor dobrado!\033[m')
            
            print()

            somas[i] = '\033[0;30;42m{}\033[m' .format(somas[i])


    return lcd


def valida_menu(MSG): #impede digitação errada no menu para jogar ou sair e no menu dos níveis

    resposta = input(MSG)
    while resposta != '1' and resposta != '2':
        print('\n')
        print('Opção escolhida inválida.\n')
        resposta = input(MSG)

    print('\n')

    return resposta

def valida_posicao(nivel):
    sessao = -1
    numero = -1

    # valida: 
    # - é tipo int?
    # - está entre os números factíveis de serem inseridos a depender do nível(de 1 a 4 ou de 1 a 9)?
    while sessao < 0 or sessao > nivel-1: 

        try:
            sessao = int(input(f'Digite a sessão escolhida(DE 1 A {nivel}): '))-1
        except:
            print(f'Valor inválido. Por favor, digite números inteiros de 1 a {nivel}.')

    while numero < 1 or numero > nivel:

        try:
            numero = int(input(f'Digite o número a ter a posição revelada(DE 1 A {nivel}): '))
        except:
            print(f'Valor inválido. Por favor, digite números inteiros de 1 a {nivel}.')

    posicao = (sessao,numero)
    
    # - já foi digitado anteriormente no jogo?
    while posicao in todas_posicoes:

        print('Posição já está exibida no tabuleiro.')
        sessao = int(input(f'Digite a sessão escolhida(DE 1 A {nivel}): '))-1
        numero = int(input(f'Digite o número a ter a posição revelada(DE 1 A {nivel}): '))
        posicao = (sessao,numero) #tupla a ser retornada na função

    todas_posicoes.append(posicao) #lista que guarda histórico de posições já reveladas no tabuleiro_x
    
    return posicao

def valida_nomes(jogador):
    nome = input(f'\033[0;30;32mNOME DO {jogador}° JOGADOR: \033[m').upper()
    while len(nome.strip()) == 0:
        nome = input(f'\033[0;30;32mDIGITE UM NOME PARA O {jogador}° JOGADOR: \033[m').upper()
    return nome

'''--------------------------------------------------------------------------------------------------------------------'''
#PROGRAMA PRINCIPAL

print('='*100)
print('''
   _____                                   _____           __      __        
  / ___/____  ____ ___  ____ _            / ___/__  ______/ /___  / /____  __    )      (\_  
  \__ \/ __ \/ __ `__ \/ __ `/  ______    \__ \/ / / / __  / __ \/ //_/ / / /   ((    _/{  "-;
 ___/ / /_/ / / / / / / /_/ /  /_____/   ___/ / /_/ / /_/ / /_/ / ,< / /_/ /     )).-' {{ ;'`
/____/\____/_/ /_/ /_/\__,_/            /____/\__,_/\__,_/\____/_/|_|\__,_/     ( (  ;._ \\
                                                                             ''')
print('='*100)


while valida_menu('[1] NOVO JOGO\n[2] SAIR\n\nDigite a opção escolhida: ') != '2':

    nome_jogador_1 = valida_nomes(1)
    nome_jogador_2 = valida_nomes(2)

    nivel = valida_menu('\n[1] PARA NÍVEL 1 (TABULEIRO 4X4)\n[2] PARA NÍVEL 2 (TABULEIRO 9X9)\n\nDigite o nível que deseja jogar: ')
    
    todas_posicoes = []

    soma_numeros_chamados = 0 #receberá incremento de todos números já validados e revelados no tabuleiro_x
    
    pontuacao_jogador_1 = pontuacao_jogador_2 = 0

    #listas booleanas: elemento i vai receber True quando a pontuação da [l]inha/[c]oluna/[d]iagonal for contabilizada
    l = [False for i in range(NIVEL_1)] if nivel == '1' else [False for i in range(NIVEL_2)]
    c = [False for i in range(NIVEL_1)] if nivel == '1' else [False for i in range(NIVEL_2)]
    d = [False]

    if nivel == '1':

        tabuleiro = tabuleiro_jogo(NIVEL_1)
        tabuleiro_x = tabuleiro_com_x(NIVEL_1)
        soma_total = 40

        #o for aninhado a seguir segue essa lógica:
        # soma_linha_1 = soma(0,2,0,2,1)
        # soma_linha_2 = soma(0,2,2,4,1)
        # soma_linha_3 = soma(2,4,0,2,1)
        # soma_linha_4 = soma(2,4,2,4,1)
        # soma_linhas = [soma_linha_1, soma_linha_2, soma_linha_3, soma_linha_4]
        soma_linhas = []
        for i in range(0,4,2):

            for j in range(0,4,2):
                soma_linhas.append(soma(i,i+2,j,j+2,1))

        #idem
        soma_colunas = []
        for i in range(0,2,1):

            for j in range(0,2,1):
                soma_colunas.append(soma(i,i+3,j,j+3,2))

        soma_diagonal = [soma(0,4,0,4,3)]

        linhas = [linha_col_diag(0,2,0,2,1),linha_col_diag(0,2,2,4,1),linha_col_diag(2,4,0,2,1),linha_col_diag(2,4,2,4,1)]

        for i in range(8):

            print()
            print('=' * 100)
            print('{:^100}'.format(f'RODADA {i+1}'))
            print('=' * 100, '\n')

            jog = '1'

            print_tabuleiro(NIVEL_1)

            print(f'VAMOS LÁ, \033[0;30;34m{nome_jogador_1}\033[m! \nPONTUAÇÃO: {pontuacao_jogador_1}')

            (sessao,numero) = valida_posicao(NIVEL_1)
            soma_numeros_chamados += numero
            encontra_numero(sessao, numero)

            #idem do for usado pra soma das linhas/colunas será usado pra fazer matriz de linhas/colunas
            linhas = []
            for i in range(0,4,2):
                for j in range(0,4,2):
                    linhas.append(linha_col_diag(i,i+2,j,j+2,1))
            l = pontuacao_jogo(linhas, soma_linhas, l)
            
            colunas = []
            for i in range(0,2,1):
                for j in range(0,2,1):
                    colunas.append(linha_col_diag(i,i+3,j,j+3,2))
            c = pontuacao_jogo(colunas, soma_colunas, c)
            
            diag = [linha_col_diag(0,4,0,4,3)]
            d = pontuacao_jogo(diag, soma_diagonal, d)

            print(f'PONTUAÇÃO DE \033[0;30;34m{nome_jogador_1}\033[m: {pontuacao_jogador_1}\n')
            
            print('=' * 100, '\n')

            if soma_numeros_chamados >= soma_total: break

            jog = '2'

            print_tabuleiro(NIVEL_1)

            print(f'VAMOS LÁ, \033[0;30;31m{nome_jogador_2}\033[m! \nPONTUAÇÃO: {pontuacao_jogador_2}')


            (sessao,numero) = valida_posicao(NIVEL_1)
            soma_numeros_chamados += numero
            encontra_numero(sessao, numero)

            linhas = []
            for i in range(0,4,2):
                for j in range(0,4,2):
                    linhas.append(linha_col_diag(i,i+2,j,j+2,1))
            l = pontuacao_jogo(linhas, soma_linhas, l)
            
            colunas = []
            for i in range(0,2,1):
                for j in range(0,2,1):
                    colunas.append(linha_col_diag(i,i+3,j,j+3,2))
            c = pontuacao_jogo(colunas, soma_colunas, c)
            
            diag = [linha_col_diag(0,4,0,4,3)]
            d = pontuacao_jogo(diag, soma_diagonal, d)

            print(f'PONTUAÇÃO DE \033[0;30;31m{nome_jogador_2}\033[m: {pontuacao_jogador_2}\n')
            
    else:

        soma_total = 405
        tabuleiro = tabuleiro_jogo(NIVEL_2)
        tabuleiro_x = tabuleiro_com_x(NIVEL_2)

        #idem da soma de linhas e colunas do nível 1
        soma_linhas = []
        for i in range(0,7,3):

            for j in range(0,7,3):
                soma_linhas.append(soma(i,i+3,j,j+3,1))

        soma_colunas = []
        for i in range(0,3,1):

            for j in range(0,3,1):
                soma_colunas.append(soma(i,i+7,j,j+7,3))

        soma_diagonal = [soma(0,9,0,9,4)]

        linhas = []
        for i in range(0,7,3):

            for j in range(0,7,3):
                linhas.append(linha_col_diag(i,i+3,j,j+3,1))

        for i in range(41):
            
            print('=' * 100)
            print('{:^100}'.format(f'RODADA {i+1}'))
            print('=' * 100, '\n')

            jog = '1'

            print_tabuleiro(NIVEL_2)

            print(f'VAMOS LÁ, \033[0;30;34m{nome_jogador_1}\033[m! \nPONTUAÇÃO: {pontuacao_jogador_1}')

            (sessao,numero) = valida_posicao(NIVEL_2)
            soma_numeros_chamados += numero
            encontra_numero(sessao, numero)

            linhas = []
            for i in range(0,7,3):

                for j in range(0,7,3):
                    linhas.append(linha_col_diag(i,i+3,j,j+3,1))
            l = pontuacao_jogo(linhas, soma_linhas, l)
           
            colunas = []
            for i in range(0,3,1):

                for j in range(0,3,1):
                    colunas.append(linha_col_diag(i,i+7,j,j+7,3))
            c = pontuacao_jogo(colunas, soma_colunas, c)
            
            diag = [linha_col_diag(0,9,0,9,4)]
            d = pontuacao_jogo(diag, soma_diagonal, d)
            
            print(f'PONTUAÇÃO DE \033[0;30;34m{nome_jogador_1}\033[m: {pontuacao_jogador_1}\n')

            print('=' * 100, '\n')

            if soma_numeros_chamados >= soma_total: break

            jog = '2'
            
            print_tabuleiro(NIVEL_2)

            print(f'VAMOS LÁ, \033[0;30;31m{nome_jogador_2}\033[m! \nPONTUAÇÃO: {pontuacao_jogador_2}')

            (sessao,numero) = valida_posicao(NIVEL_2)
            soma_numeros_chamados += numero
            encontra_numero(sessao, numero)

            linhas = []
            for i in range(0,7,3):
                for j in range(0,7,3):
                    linhas.append(linha_col_diag(i,i+3,j,j+3,1))
            l = pontuacao_jogo(linhas, soma_linhas, l)
           
            colunas = []
            for i in range(0,3,1):
                for j in range(0,3,1):
                    colunas.append(linha_col_diag(i,i+7,j,j+7,3))
            c = pontuacao_jogo(colunas, soma_colunas, c)
            
            diag = [linha_col_diag(0,9,0,9,4)]
            d = pontuacao_jogo(diag, soma_diagonal, d)

            print(f'PONTUAÇÃO DE \033[0;30;31m{nome_jogador_2}\033[m: {pontuacao_jogador_2}\n')

    if nivel == '1':
       print_tabuleiro(NIVEL_1)
    else:
        print_tabuleiro(NIVEL_2)
    
    if pontuacao_jogador_1 > pontuacao_jogador_2:
        print(f'\033[0;30;42m JOGO VENCIDO POR {nome_jogador_1}! PONTUAÇÃO: {pontuacao_jogador_1} PONTOS\033[m')
    elif pontuacao_jogador_2 > pontuacao_jogador_1:
        print(f'\033[0;30;42m JOGO VENCIDO POR {nome_jogador_2}! PONTUAÇÃO: {pontuacao_jogador_2} PONTOS\033[m')
    elif pontuacao_jogador_1 == pontuacao_jogador_2:
        print(f'\033[1;35;43m EMPATE! OS DOIS JOGADORES OBTIVERAM A PONTUAÇÃO DE {pontuacao_jogador_1} PONTOS\033[m')

print('Game over.')