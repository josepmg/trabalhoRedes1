import random
import sys
from main.utils import Utils
class Tabuleiro:

    #construtor da classe Tabuleiro que ja cria um tabuleiro novo
    def __init__(self, dim):
        #dimensoes do tabuleiro
        self.dimension = dim
        #numero de pecas
        self.nPieces = dim**2
        # numero de pares
        self.pairs = dim * 2
        # numero de pares encontrados
        self.discoveredPairs = 0
        #valores do tabuleiro
        self.values = []
        #como o tabuleiro pe apresentado para o jogador
        self.display = []

        # inicializa o array de valores
        for i in range(0, dim):
            linha = []
            for j in range(0, dim):
                linha.append(0)
            self.values.append(linha)

        # inicializa o array de display
        for i in range(0, dim):
            linha = []
            for j in range(0, dim):
                linha.append('?')
            self.display.append(linha)

        # Cria um array com todas as posicoes disponiveis
        # Facilita a atribuicao inical de valores (aleatorios)
        availabePositions = []
        for i in range(0, dim):

            for j in range(0, dim):
                availabePositions.append((i, j))

        # Varre todas as pecas que serao colocadas no
        # tabuleiro e posiciona cada par de pecas iguais
        # em posicoes aleatorias.
        for j in range(0, dim // 2):
            for i in range(1, dim + 1):
                # Sorteio da posicao da segunda peca com valor 'i'
                maximo = len(availabePositions)
                indiceAleatorio = random.randint(0, maximo - 1)
                rI, rJ = availabePositions.pop(indiceAleatorio)

                self.values[rI][rJ] = -i

                # Sorteio da posicao da segunda peca com valor 'i'
                maximo = len(availabePositions)
                indiceAleatorio = random.randint(0, maximo - 1)
                rI, rJ = availabePositions.pop(indiceAleatorio)

                self.values[rI][rJ] = -i

    def getDimen(self):
        return self.dimension

    def getNPieces(self):
        return self.nPieces

    def getNumPairs(self):
        return self.pairs

    def discoverPair(self):
        self.discoveredPairs += 1

    def getDiscoveredPairs(self):
        return self.discoveredPairs

    def revealPiece(self, i, j):
        #caso a peca da posicao i j  ainda nao tenha sido esoclhida ou retirada do jogo
        if (self.display[i][j] == '?' and self.values[i][j] < 0):
            #array do display mostra o valor da peca
            self.display[i][j] = self.values[i][j]
            #array da peca passa a conter o numero POSITIVO, indicando que esta escolhido
            self.values[i][j] = -self.values[i][j]
            return self.values[i][j]

        # Caso a peça já tenha sido escolhida ou removida, retorna 0 como código de erro
        return 0

    def hidePiece(self, i, j):
        #caso a peca da posicao i j  ainda tenha sido esoclhida e nao tenha sido retirada do jogo
        if self.display[i][j] != '?' and self.display[i][j] != '-' and self.values > 0:
            #array do display recebe interrogacao
            self.display[i][j] = '?'
            #array da peca passa a conter o numero NEGATIVO, indicando que nao esta escolhido
            self.values[i][j] = -self.values[i][j]
            return True
        else:
            return False

    def removePiece(self, i, j):
        if self.display[i][j] == '-':
            return False
        else:
            self.display[i][j] = '-'
            return True

