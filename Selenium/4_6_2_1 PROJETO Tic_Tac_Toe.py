import time
from random import randrange

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
def displayBoard(board):
    print("""    +-------+-------+-------+
    |       |       |       |
    |  """, board[0][0], '  |  ',board[0][1],'  |  ', board[0][2],'  |\n'
    """    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |  """, board[1][0], '  |  ',board[1][1],'  |  ', board[1][2],'  |\n'
    """    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |  """, board[2][0], '  |  ',board[2][1],'  |  ', board[2][2],'  |\n'
    """    |       |       |       |
    +-------+-------+-------+""")


def enterMove(board):
    while True:
        opcao = int(input('Informe a posição desejada conforme descrito no board[1-9]'))
        if opcao < 1 or opcao > 9:
            print('Posição inválida, favor informar um número de 1 a 9')

        elif str(opcao) not in board[0] and str(opcao)  not in board[1] and str(opcao) not in board[2]:
            print('Esta posição já foi marcada, favor selecionar outra!')

        else:
            if opcao == 1:
                board[0][0] = 'O'
            elif opcao == 2:
                board[0][1] = 'O'
            elif opcao == 3:
                board[0][2] = 'O'
            elif opcao == 4:
                board[1][0] = 'O'
            elif opcao == 5:
                board[1][1] = 'O'
            elif opcao == 6:
                board[1][2] = 'O'
            elif opcao == 7:
                board[2][0] = 'O'
            elif opcao == 8:
                board[2][1] = 'O'
            elif opcao == 9:
                board[2][2] = 'O'
            break


def make_list_of_free_fields(board):
    global lista
    lista = [ ]
    for linha in range(0,3):
        for coluna in range(0,3):
            if board[linha][coluna] == 'X' or board[linha][coluna] == 'O':
                pass
            else:
                lista.append(([linha],[coluna]))

def victory_for(board, sign):

    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or(
    board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or(
    board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or(
    board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or(
    board[1][0] == sign and board[1][1] == sign and board[2][1] == sign) or(
    board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or(
    board[0][2] == sign and board[1][1] == sign and board[2][0] == sign) or(
    board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):

        return True
    else:
        return False

def draw_move(board):
    while True:
        linha = randrange(3)
        coluna = randrange(3)

        if([linha],[coluna]) not in lista:
            continue
        else:
            board[linha][coluna] = 'X'
            return

jogador = 'O'
computador = 'X'
movimentos = 1
make_list_of_free_fields(board)
print('Bem vindo ao Jogo! \n O primeiro movimento é do computador')
time.sleep(2)
displayBoard(board)

while movimentos < 9:
    enterMove(board)
    displayBoard(board)
    movimentos += 1
    if victory_for(board, jogador):
        print("Parabéns, você venceu")
        break
    print('Agora é vez do computador')
    time.sleep(2)
    make_list_of_free_fields(board)
    draw_move(board)
    movimentos += 1
    displayBoard(board)
    if victory_for(board, computador):
        print("Que pena, dessa vez a máquina venceu")
        break

if victory_for(board, 'O') == False and victory_for(board, 'X') == False:
    print('Deu velha! rsrs')

