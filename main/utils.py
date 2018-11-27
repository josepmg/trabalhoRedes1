import os
import sys
from abc import ABC, abstractmethod

class Utils(ABC):

    @abstractmethod
    def clearScreen(cls):
        # if os.name == 'nt':
        #     os.system('cls')
        # else:
        #     os.system('clear')
        print ("\n" * 20)

    @abstractmethod
    def apresentaTabuleiro(tabuleiro, dimen):
        Utils.clearScreen("cls")
        # Imprime coordenadas horizontais
        sys.stdout.write("\n    ")
        for i in range(0, dimen):
            sys.stdout.write("{0:2d} ".format(i))

        sys.stdout.write("\n")

        # Imprime separador horizontal
        sys.stdout.write("-----")
        for i in range(0, dimen):
            sys.stdout.write("---")

        sys.stdout.write("\n")

        for i in range(0, dimen):

            # Imprime coordenadas verticais
            sys.stdout.write("{0:2d} | ".format(i))
            # Imprime conteudo da linha 'i'
            for j in range(0, dimen):
                sys.stdout.write("{0:2} ".format(tabuleiro[i][j]))

            sys.stdout.write("\n")