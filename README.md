# 1. Algoritimos Avançados N1 


**Alunos:**
- Gabriel Henrique Karing.
- Diego Planinscheck.
- Gabriel Wendorff.
- José Marcos Zoz Marques.

* * *

O repositório tem como objetivo entregar o desafio proposto pela professora **Beatriz M. Reichert**, que tem como objetivo:

> Implementar um algoritimo que fará o calculo com o maior peso entre dois vértices em um grafo de direção aciclica (DAG) tendo em consideração algumas outras restrições adicionais.
>
> Um caminho é chamado caso não exista nenhum vértice repetido. O comprimento total desse caminho é definido pela soma dos pesos de cada uma das arestas.


## 2. Entregas e métodos de avaliação:

- Entrega:
  - Código funcional.
  - Relatório com o Desevolvimento.
<br><br>
- Avaliação:
  - Código = 6 pontos (60%).
  - Relatório = 2 pontos (20%).
  - Apresentação = 2 pontos (20%).


## 3. Sobre o código e Exigências

O algoritimo deve ser desenvolvido em C++ ou python. O escolhido pela equipe foi o `Python` por ser de maior familiaridade técnica da equipe.

- O algoritimo será testado na ferramenta de execução de código online [Jdoodle.](https://www.jdoodle.com)

### 3.1 Exigências

O algoritimo deve receber sua entrada através de um arquivo de texto que deve conter os seguintes requisitos:
- Numero de Vértices: N
- Matriz de adjacência: N x N.
- Vértice de Origem.
- Vértice de Destino.
- Numero máximo de vértices que podem ser visitados no caminho: K.

1. Na matriz de Adjacência o 0 é quem indica a ausência de aresta. Então os pesos que são válidos são qualquer valor inteiro que seja !!(diferente) de 0 (tanto positivos quanto negativos).

2. O formato do arquivo e entrada pode ser observado pode ser observado em: `@\input\entrada.txt`.
    - Os índices devem sempre começar em 0.

    **O formato do arquivo de entrada não pode ser alterado apenas o contéudo dentro dele.**

3. O algoritimo deve funcionar para grafos aciclicos, direcionados e com pesos em suas arestas.

4. Ele deve aceitar pesos negativos.

5. Ele deve encontrar o caminho mais simples que possui o maior peso entre sua origem e seu destino, respeitando as suas restrições:
    - Ele só pode possuir no máximo K vértices (contando origem e destino).

6. Caso ele não encontre um caminho válido, ele deve retornar a seguinte mensagem: `Não existe caminho válido.`

## 4. Grafo de Exemplo:
![alt text](image.png)


## 5. Critérios de avaliação de código:

Serão testados 6 grafos, todos eles de forma direcionada, acíclios e com pesos em suas respectivas arestas.

- O primerio grafo que será testado irá ser o do exemplo acima, caso o primeiro teste seja executado com sucesso o primeiro ponto ja será garantido, ou seja cada teste conta como 1 ponto.

## 6. Como executar

1.Inicar o ambiente virtual:
```
python -m venv venv
```

2.Ativar o ambiente virtual:
```
.\venv\Scripts\activate
```
