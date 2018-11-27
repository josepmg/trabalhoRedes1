![logos](http://www.professores.uff.br/kowada/wp-content/uploads/sites/63/2017/08/UFF-IC-logos.png)
# Jogo da memória on-line
Trabalho semestral apresentado para a disciplina Redes de Computadores 1 para Sistemas de Informação.

**Alunos:** Giovane Lopes da Silva e José Paulo de Mello Gomes

**Instituição:** Universidade Federal Fluminense

**Curso:** Bacharelado em Sistemas de Informação

**Disciplina/período:** Redes de computadores para Sistemas de Informação/2018.2

**Professor:** Diego Gimenez Passos

## Utilização
### Preparação do ambiente
Este projeto foi desenvolvido em Python 3.7.0. Portanto, faz-se necessário instalação desta ou superiores versões.

Utilizou-se o módulo [pickle](https://docs.python.org/3/library/pickle.html) do Python para serialização e de-serialização binária de objetos, como arrays e números inteiros ao serem transmitidos pelo socket TCP desta aplicação.

### Baixando repositório
```bash
git init
git clone https://github.com/josepmg/trabalhoRedes1.git
```

### Executando os arquivos
Primeiro, deve-se executar o arquivo servidor pelo comando:
```bash
$ py servidor.py [NUMERO_JOGADORES] [DIMENSÃO_TABULEIRO]
```
O programa servidor utiliza a porta 12000. Caso queira trocá-la, a linha 13 deve ser alterada.
Além disso, o programa servidor mostra um "gabarito" com os valores de cada peça.

Após, os clientes são executados pelo comando: 
```bash
$ py cliente.py [IP_SERVIDOR] [PORTA_SOCKET_SERVIDOR]
```

Agora é só aproveitar o jogo!

## Estrutura do projeto
### Estrutura
- main
  - cliente.py: arquivo do programa cliente
  - servidor.py: arquivo do programa servidor
  - utils.py: arquivo com funções variadas
- model
  - jogador.py: arquivo da classe Jogador e seus respectivos métodos e atributos, como identificador, pontuação, socket e endereço;
  - partida.py: arquivo da classe Partida e seus respectivos métodos e atributos, como lista de jogadores, um tabuleiro e número de jogadores;
  - tabuleiro.py: arquivo da classe Tabuleiro e seus respectivos métodos e atributos, como dimensão, número de peças, pares totais e pares descobertos, além um array contendo os valores das peças e outro com os as informações a serem mostradas;

Alguns métodos serão citados e explicados mais adiante.
### Especificação dos métodos e funcionamento 

#### Servidor
##### Método _startTCPServer(serverPort)_
Essa função faz a criação do Socket TCP no servidor, utilizando a variável “serverPort” que contém o número de porta especificada e comunica que está aguardando conexão dos jogadores para o programa servidor.
##### Método  _sendStatus(numPlayers, match)_
Através do socket de cada jogador, essa função é responsável por enviar a todos os jogadores o status da partida, como tabuleiro(de display, sem os valores do tabuleiro original) atualizado, placar de pontuação atualizado e o jogador da vez.
##### Método _sendRoundPlayer(numPlayers, match, roundPlayers)_
Esta função tem como objetivo enviar a todos os jogadores o atual jogador da vez(roundPlayer). Para isso, recebe a partida (contendo o vetor de jogadores), o número de jogadores e o jogador da vez como parâmetros.
##### Método _sendTile(numPlayers, match, tileCoord, tileValue)_
Após receber as coordenadas do jogador da vez, essa função fica responsável por enviar apenas o valor e as coordenadas, revelando assim o valor da peça no tabuleiro display para todos os jogadores da partida.

#### Cliente
##### Método _startTCPClient(serverIp, serverPort)_
Essa função é utilizada para criar um socket cliente TCP informando o IP do servidor (serverIp) e sua porta (serverPort). Após, comunica ao cliente que a conexão foi estabelecida e está aguardando demais jogadores.
##### Método _getCoordinates(dimen)_
Utilizada para ler as coordenadas (de 1 peça por vez) do cliente quando for sua vez de jogar. Faz verificações de valores inválidos, ou seja, que não equivalham a nenhuma peça do tabuleiro, neste caso, pede novamente as coordenadas. Caso as coordenadas sejam válidas, ela as retorna.

#### Utils
Possui dois métodos: um para limpar a tela e outro para apresentar o tabuleiro formatado. Optou-se por criar esta classe para evitar repetição de código, uma vez que esses métodos são utulizados tanto no cliente, quanto no servidor.

#### Partida
Como dito previamente, é a classe referente a uma partida. Possui, como atributos, o úmero de jogaores, uma instância de Tabuleiro e um vetor de jogadores.
##### Método  _getters_
Funções para recuperarem o valor dos atributos do objeto
##### Método _addPlayer(self, ident, socket, address)_
Adiociona um novo jogador ao vetor de jogadores
##### Método _showScore(self)_
Cria uma string formatada com as pontuações de cada jogador 

#### Jogador
Como dito previamente, é a classe referente a um jogador. Possui como atributos, um identificado, a pontuação (inicialmente 0), um socket e uma tupla de endereço (contendo IP do hosto do cliente e pota em que o processo está sendo executado).

Além disso, possui métodos para incrementar a pontuação, encerrar a conexão, dentre outras.

#### Tabuleiro
Como dito previamente, é a classe referente a um tabuleiro. Possui como atributos, a dimensão, o número total de peças e de pares. Além do número de pares descobertos , um vetor com os valores das peças e outro vetor de display. 

Além dos métodos a seguir, possui outros para recuperar os atributos supracitados.
##### Método _revealPiece(self, i, j)_
Caso seja um valor válido, retorna o valor indicado pelas coordenadas dadas. Caso contrário, retorna 0.
##### Método _hidePiece(self, i, j)_
Caso seja um valor válido, "esconde" a peça (display nas coordenadas = '?'), posição no array de valores passa a ser negativa, indicando que está fechada, e retorna _true_, indicando que a operação foi realizada. Caso contrário, retorna _false_.
##### Método _removePiece(self, i, j)_
Remove uma peça do tabuleiro de display. Caso ela já tenhaa sido removida, retorna _false_. Se não, retira a peça e retornan _true_, indicando o sucesso da operação.

