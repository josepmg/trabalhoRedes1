import sys
import time

sys.path.append('../')
import socket
import pickle
from model.partida import Partida
from main.utils import Utils

# Constantes do jogo
NUM_PLAYERS = int(sys.argv[1])
BOARD_DIMEN = int(sys.argv[2])
SERVER_PORT = 12000

# Metodo para iniciar um novo socket
def startTCPServer(serverPort):
    # Criando um socket para o servidor
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socker criado a porta do servidor
    serverSocket.bind(('', serverPort))

    # Habilita o socket do servidor
    serverSocket.listen(4)

    print("O servidor está pronto para receber conexões")
    return serverSocket

def sendStatus(numPlayers, match):
    i = 0
    while i < numPlayers:
        # O trecho abaixo é para enviar somente o tabuleiro de display para jogadores
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).sendall(pickle.dumps((match.board.display)))
        # Enviando as dimensões do tabuleiro  para jogadores
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).send(str(BOARD_DIMEN).encode('utf8'))
        # Enviando placar inicial para jogadores
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).sendall(pickle.dumps(match.showScore()))
        i += 1

def sendRoundPlayer(numPlayers, match, roundPlayer):
    i = 0
    while i < numPlayers:
        # Informa o joador da vez para todos jogadores
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).send((str(roundPlayer)).encode('utf8'))
        i += 1

def sendTile(numPlayers, match, tileCoord, tileValue):
    i = 0
    while i < numPlayers:
        # O trecho abaixo envia o valor da peça
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).send(tileValue.encode('utf8'))
        # Enviando as coordenadas da peça
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).send(tileCoord.encode('utf8'))
        i += 1

def sendWinner(numPlayers, match):
    i = 1
    winner = 0
    # Loop para achar o jogador vencedor
    while i < numPlayers:
        # Verificando se há algum jogador com a pontuação maior que o atual vencedor
        if ((match.getPlayer(i)).getScore() > (match.getPlayer(winner)).getScore()):
            winner = i
        # Casa haja um empate, não haverá vencedor
        if ((match.getPlayer(i)).getScore() == (match.getPlayer(winner)).getScore()):
            winner = -1
        i += 1
    # Loop para enviar o vencedor para os jogadores
    i = 0
    while i < numPlayers:
        # O trecho abaixo envia o jogador vencedor
        time.sleep(.1)
        (match.getPlayer(i).getSocket()).send(str(winner).encode('utf8'))
        i += 1

# Iniciando um socket para receber conexões TCP
serverSocket = startTCPServer(SERVER_PORT)

while True:
    # Criando uma nova partida
    partida = Partida(NUM_PLAYERS, BOARD_DIMEN)

    # Mostrando os valores dispostos no tabuleiro
    Utils.apresentaTabuleiro(partida.board.values, BOARD_DIMEN)

    # Iniciando conexões com os clientes
    # broadcast funciona com índice. Utilizado em transmissões para todos jogadores
    broadcast = 0
    while broadcast < partida.getPlayersNumber():
        print("Aguarnando nova conexão")
        connectionSocket, address = serverSocket.accept()
        partida.addPlayer(broadcast, connectionSocket, address)
        print("Nova conexão estabelecida com: ", address)
        # Enviando identificação para usuário
        time.sleep(.1)
        (partida.getPlayer(broadcast).getSocket()).send(str(broadcast).encode('utf8'))
        broadcast += 1

    # playerIndex funciona como identificador/indice para comunicar-se com jogadores individualmente
    roundPlayer = 0
    # Após iniciar conexões, o servior envia o tabuleiro para todos os jogadores
    broadcast = 0

    # Laço para controlar partida
    # (enquanto o número de pares descobertos fo menor que o número de pares, ainda há jogo)
    while (partida.board).getDiscoveredPairs() < (partida.board).getNumPairs():

        # Enquanto for a vez do jogador, ele estará nesse loop
        while True:
            # Envia status da partita para todos os jogadores
            # Por status, dizemos: estado atual do tabuleiro e pontuação dos jogadores
            sendStatus(partida.getPlayersNumber(), partida)
            # Informa o jogador da vez para todos clientes
            sendRoundPlayer(partida.getPlayersNumber(), partida, roundPlayer)
            while True:
                # Recebendo coordenadas(string) da PRIEMRIA PEÇA enviadas pelo cliente da vez
                piece1 = (partida.getPlayer(roundPlayer).getSocket()).recv(4096).decode('utf8')
                # Valor da peça escolhida
                pieceValue1 = str(partida.board.revealPiece(int(piece1[0]), int(piece1[2])))
                # Envia o valor da peça e sua posição para todos os jogadores
                sendTile(partida.getPlayersNumber(), partida, piece1, pieceValue1)
                if (pieceValue1 != 0):
                    break
            while True:
                # Recebendo coordenadas(string) da SEGUNDA PEÇA enviadas pelo cliente da vez
                piece2 = (partida.getPlayer(roundPlayer).getSocket()).recv(4096).decode('utf8')
                # Valor da peça escolhida
                pieceValue2 = str(partida.board.revealPiece(int(piece2[0]), int(piece2[2])))
                # # Envia este valor para o jogador da vez
                sendTile(partida.getPlayersNumber(), partida, piece2, pieceValue2)
                if (int(pieceValue2) != 0):
                    break
                else:
                    continue
            if (pieceValue1 != 0 and pieceValue2 != 0 and pieceValue1 == pieceValue2):
                (partida.getPlayer(roundPlayer)).addScore()
                partida.board.discoverPair()
                partida.board.removePiece(int(piece1[0]), int(piece1[2]))
                partida.board.removePiece(int(piece2[0]), int(piece2[2]))
                Utils.apresentaTabuleiro(partida.board.values, BOARD_DIMEN)
                if ((partida.board).getDiscoveredPairs() == (partida.board).getNumPairs()):
                    break
            else:
                partida.board.hidePiece(int(piece1[0]), int(piece1[2]))
                partida.board.hidePiece(int(piece2[0]), int(piece2[2]))
                if((partida.board).getDiscoveredPairs() == (partida.board).getNumPairs()):
                    roundPlayer = -1
                else:
                    roundPlayer = (roundPlayer + 1) % partida.getPlayersNumber()
                break

    # Envia status da partita para todos os jogadores
    # Por status, dizemos: estado atual do tabuleiro e pontuação dos jogadores
    sendStatus(partida.getPlayersNumber(), partida)
    # Informa o jogador da vez para todos clientes
    sendRoundPlayer(partida.getPlayersNumber(), partida, "-1")
    # Informa o jogador vencedor
    sendWinner(partida.getPlayersNumber(), partida)

    # Encerrando conexão com clientes
    i = 0
    while i < NUM_PLAYERS:
        (partida.getPlayer(i)).closeConnection()
        i += 1

    option = input("1 - Sim\n2 - Não\nDeseja iniciar uma nova partida? ")
    if option == "2" or option == 2 or option == '2':
        break
    # else:
    #     break
