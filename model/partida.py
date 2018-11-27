from model.jogador import Jogador
from model.tabuleiro import Tabuleiro
class Partida:

    def __init__(self, playersNumber, boardDimen):
        self.playersNumber = playersNumber
        self.players = []
        self.board = Tabuleiro(boardDimen)

    def getPlayersNumber(self):
        return self.playersNumber

    def getBoardDimen(self):
        return self.board.getDimen()

    def getPlayer(self, position):
        return self.players[position]

    def addPlayer(self, ident, socket, address):
        self.players.append(Jogador(socket, address, ident))

    def showScore(self):
        placar = "\n\nPLACAR:\n---------------------\n"
        # print("n jogadores: " + str(self.playersNumber))
        for i in range (0, self.playersNumber):
            placar += "Jogador " + str(i + 1) + ": " + str(self.players[i].getScore()) + "\n"
        placar += "\n"
        return placar
