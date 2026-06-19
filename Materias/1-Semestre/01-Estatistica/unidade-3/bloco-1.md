## Análise combinatória
Ela serve para responder perguntas do tipo: de quantas maneiras algo pode acontecer?

Exemplos simples:
- Quantas senhas posso criar?
- Quantas combinações de roupas existem?
- Quantas formas de escolher pessoas?

"Qual a probabilidade de pegar uma caneta preta?"

Para resolver isso, você precisar saber quantas combinações existem.

Análise combinatória = contar possibilidades
Probabilidade = usar essa contagem

É uma forma organizada de contar sem precisar listar tudo.

---

## Fatorial
O fatorial é uma multiplicação em sequência decrescente até chegar no 1.

Forma geral

n! = n. (n-1) . (n-2) . (n - 3) .... . 1

Exemplo:

5!

5! = 5 x 4 x 3 x 2 x 1 = 120

4! = 4 x 3 x 2 x 1 = 24

3! = 3 x 2 x 1 = 6

2! = 2 x 1 = 2

1! = 1

0! = 1

Exemplo de aplicação

Mais adiante, será calculada A Razão de Dois Fatoriais

Então, é interessante detalhar o processo desse cálculo.

Considere a expressão a seguir: 6! / 4!

Aqui, fazemos:

6! = 6 x 5 x 4 x 3 x 2 x 1 = 720

4! = 4 x 3 x 2 x 1 = 24

Depois, fazemos o 6! / 4!, que é 720 / 24 = 525.

Uma dica legal, é ao invés de fazermos o fatorial do 6 até chegar o 1, podemos parar no fatorial inferior, por ex:

6! / 4!

6! = 6 x 5 x 4!

Então:

6! = 6 x 5 x 24
6! = 30 x 24
6! = 720 

Assim, diminuímos bastante o trabalho braçal.

---

## Coeficiente binominal
Ele representa quantas formas existem de escolher p elementos dentro de um total de n

Forma de ler

n sobre p - 5 sobre 2

Traduzindo...

De quantas maneiras posso escolher 2 entre 5?

(n sobre p) = n! / (p! x (n-p)!)

Então:

5 sobre 2 é:

5! / 2! . (5 - 2)!

120 /  2 . 6

120 / 12

O binominal de 5 sobre 2 é 10.