![logos](http://www.professores.uff.br/kowada/wp-content/uploads/sites/63/2017/08/UFF-IC-logos.png)
# Jogo da memória on-line
Trabalho semestral apresentado para a disciplina Redes de Computadores 1 para Sistemas de Informação pelos alunos Giovane Lopes da Silva e José Paulo de Mello Gomes

**Instituição:** Universidade Federal Fluminense

**Curso:** Bacharelado em Sistemas de Informação

**Disciplina/período:** Redes de computadores para Sistemas de Informação/2018.2

**Professor:** Diego Gimenez Passos

**Alunos:** Giovane Lopes da Silva e José Paulo de Mello Gomes

## Utilização
### Preparação do ambiente
Este projeto foi desenvolvido em Python 3.7.0. Portanto, faz-se necessário instalação desta ou superiores versões.

Utilizou-se o módulo [pickle](https://docs.python.org/3/library/pickle.html) do Python para serialização e de-serialização binária de objetos, como arrays e números inteiros ao serem transmitidos pelo socket TCP desta aplicação.
### Baixando repositório
```bash
git init
git clone https://github.com/josepmg/trabalhoRedes1.git
```
### Estrutura
- main
  - cliente.py: arquivo do programa cliente
  - servidor.py: arquivo do programa servidor
  - utils.py: arquivo com funções variadas
- model
  - jogador.py: arquivo da classe Jogador e seus respectivos métodos e atributos, como identificador, pontuação, socket e endereço;
  - partida.py: arquivo da classe Partida e seus respectivos métodos e atributos, como lista de jogadores, um tabuleiro e número de jogadores;
  - tabuleiro.py: arquivo da classe Tabuleiroe seus respectivos métodos e atributos, como dimensão, número de peças, pares totais e pares descobertos, além um array contendo os valores das peças e outro com os as informações a serem mostradas;

Alguns métodos serão citados e explicados mais adiante.

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
