class Jogador:

    def __init__(self, socket, address, ident):
        self.socket = socket
        self.address = address
        self.score = 0;
        self.id = ident

    def getScore(self):
        return self.score

    def addScore(self):
        self.score += 1

    def closeConnection(self):
        self.socket.close()

    def getIdent(self):
        return self.id

    def getSocket(self):
        return self.socket

