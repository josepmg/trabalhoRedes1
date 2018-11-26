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
### Baixando repositório
```bash
git init
git clone https://github.com/josepmg/trabalhoRedes1.git
```
### Estrutura
-main
 -cliente.py: arquivo do programa cliente;
 -servidor.py: arquivo do programa servidor;
 -utils.py: arquivo contendo funções diversas;
-model
 -jogador.py: classe que tem atributos e métodos dos jogadores, como identificador, pontuação, socket TCP e endereço;
 -partida.py: classe que tem atributos e métodos das partidas, como número de jogadores, uma instância de tabuleiro e uma lista de jogadores;
 -tabuleiro.py: classe que tem atributos e métodos dos tabuleiros, como dimensão, número de peças, número de pares, pares descobertos, um array com os valores das posções e outro array de apresentação.
