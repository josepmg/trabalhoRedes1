import sys
sys.path.append('../')
import socket, pickle
from main.utils import Utils

def startTCPClient (serverIP, serverPort):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIP, serverPort))
    print("Conexão estabelecida")
    return clientSocket

def getCoordinates(dimen):

    entrada = input("Especifique uma peca: ")

    try:
        i = int(entrada.split(' ')[0])
        j = int(entrada.split(' ')[1])
    except (IndexError, ValueError):
        print("Coordenadas invalidas! Use o formato \"i j\" (sem aspas),")
        print("onde i e j sao inteiros maiores ou iguais a 0 e menores que {0}".format(dimen))
        input("Pressione <enter> para continuar...")
        return False

    if i < 0 or i >= dimen:
        print("Coordenada i deve ser maior ou igual a zero e menor que {0}".format(dimen))
        input("Pressione <enter> para continuar...")
        return False

    if j < 0 or j >= dimen:
        print("Coordenada j deve ser maior ou igual a zero e menor que {0}".format(dimen))
        input("Pressione <enter> para continuar...")
        return False

    return (entrada.strip())

# Abrindo conexão com servidor
clientSocket = startTCPClient(sys.argv[1], int(sys.argv[2]))
# Recebendo ID do jogador local
idJogador = clientSocket.recv(4096).decode('utf8')
print("Aguardando outros jogadores se conectarem...\n")

coord1 = ""
coord2 = ""
# Enquanto o jogador da vez for válido(diferente de -1), a partida está acontecendo
while True:

    # Recebendo o tabuleiro do servidor
    data = clientSocket.recv(4096)
    tabuleiro = pickle.loads(data)
    # Recebendo dimensão do tabualeiro para apresentá-lo
    dimen = clientSocket.recv(4096).decode('utf8')
    # Recebendo placar inicial
    placar = clientSocket.recv(4096)
    placar = pickle.loads(placar)
    # Recebendo o jogadaor da vez
    jogadorVez = clientSocket.recv(4096).decode('utf8')
    # Verifica se ainda há partida
    if jogadorVez == "-1":
        break

    if coord1 == "":
        print("Iniciando patida!\n")



    # Apresentando o tabuleiro e placar recebidos
    Utils.apresentaTabuleiro(tabuleiro, int(dimen))
    print(placar)

    # PRIMEIRA PEÇA
    while True:
        # Verifica se cliente é o jogador da vez
        if jogadorVez == idJogador:
            # Indica que é a vez deste cliente
            print("Sua vez, jogador " + str(int(jogadorVez)+1) + "")
            # As coordenadas serão tradadas como string, pois a trasmissão e recepção(socket) é de iplementação mais fácil
            # Solicita coordenadas para usuário
            coord1 = getCoordinates(int(dimen))
            # Enquanto as coordenadas forem falsas (inválidas),
            # o programa cliente continuará pedindo por peças válidas
            while (coord1 == False):
                coord1 = getCoordinates(int(dimen))
            # Envia coordenadas ao servidor
            clientSocket.sendall(coord1.encode())
        # Caso o cliente não seja o jogador da vez
        else:
            # Imprime o jogador da vez
            print("Vez do jogador " + str(int(jogadorVez)+1))

        # Recebendo valor da PRIMEIRA PEÇA(em string)
        tileValue1 = clientSocket.recv(4096).decode('utf8')
        # Recebendo a coordenada da PRIMEIRA PEÇA
        coord1 = clientSocket.recv(4096).decode('utf8')

        # # # #  # # #  # # #  # # #  # # #  #  # # #
        # FAZER FERIFICAÇÃO SE A PEÇA É VÁLIDA AQUI #
        # # # #  # # #  # # #  # # #  # # #  #  # # #
        if (tileValue1 == "0"):
            if (jogadorVez == idJogador):
                print("Escolha uma peca ainda fechada!")
                input("Pressione <enter> para continuar...")
                continue
            else:
                print("Jogador " + str(int(jogadorVez)+1) + " escolheu uma peça já fechada")
        else:
            # Como a sting tera formato 'i j', podemos acessar esses valores através de suas posições na string
            # Como são caracteres, devem ser convertidos para int
            tabuleiro[int(coord1[0])][int(coord1[2])] = tileValue1

            # Apresentando estado atual do tabuleiro
            Utils.apresentaTabuleiro(tabuleiro, int(dimen))
        break

    # SEGUNDA PEÇA
    while True:
    # Verifica se cliente é o jogador da vez
        if jogadorVez == idJogador:
            # Indica que é a vez deste cliente
            print("Sua vez, jogador " + str(int(jogadorVez)+1) + "")
            # As coordenadas serão tradadas como string, pois a trasmissão e recepção(socket) é de iplementação mais fácil
            # Solicita coordenadas para usuário
            coord2 = getCoordinates(int(dimen))
            # Enquanto as coordenadas forem falsas (inválidas),
            # o programa cliente continuará pedindo por peças válidas
            while (coord2 == False):
                coord2 = getCoordinates(int(dimen))
            # Envia coordenadas ao servidor
            clientSocket.sendall(coord2.encode())
        # Caso o cliente não seja o jogador da vez
        else:
            # Imprime o jogador da vez
            print("Vez do jogador " + str(int(jogadorVez)+1) + "")

        # Recebendo valor da SEGUNDA PEÇA(em string)
        tileValue2 = clientSocket.recv(4096).decode('utf8')
        # Recebendo a coordenada da SEGUNDA PEÇA
        coord2 = clientSocket.recv(4096).decode('utf8')

        # # # #  # # #  # # #  # # #  # # #  #  # # #
        # FAZER FERIFICAÇÃO SE A PEÇA É VÁLIDA AQUI #
        # # # #  # # #  # # #  # # #  # # #  #  # # #
        if (tileValue2 == "0"):
            if(jogadorVez == idJogador):
                print("Escolha uma peca ainda fechada!")
                input("Pressione <enter> para continuar...")
                continue
            else:
                print("Jogador " + str(int(jogadorVez)+1) + " escolheu peças inválias.")
        else:
            break

    # Como a sting tera formato 'i j', podemos acessar esses valores através de suas posições na string
    # Como são caracteres, devem ser convertidos para int
    print("Coord2: " + coord2)
    tabuleiro[int(coord2[0])][int(coord2[2])] = tileValue2

    # Apresentando estado atual do tabuleiro
    Utils.apresentaTabuleiro(tabuleiro, int(dimen))

    # APRESENTA AS PEÇAS ESCOLHIDAS
    if jogadorVez == idJogador:
        # VERIFICA SE SÃO UM PAR
        if tileValue1 == tileValue2:
            print("Você escolheu as peças [" + coord1 + "] e [" + coord2 + "] e pontou :D")
        else:
            print("Você escolheu as peças [" + coord1 + "] e [" + coord2 + "], mas não pontou :(")
    else:
        # VERIFICA SE SÃO UM PAR
        if tileValue1 == tileValue2:
            print(
                "Jogador " + jogadorVez + " escolheu as peças [" + coord1 + "] e [" + coord2 + "] e pontou :D")
        else:
            print(
                "Jogador " + jogadorVez + " escolheu as peças [" + coord1 + "] e [" + coord2 + "], mas não pontou :(")

Utils.clearScreen("cls")
print(placar)
print("O jogo acabou :/")
winner = int(clientSocket.recv(4096).decode('utf8')) + 1
if winner == 0:
    print("Houve um empate. Portanto, não houve vencedor.")
else:
    print("O vencedor foi o jogador " + str(winner) + "!")
    print("Parabéns, jogador " + str(winner) + "!" )


clientSocket.close()