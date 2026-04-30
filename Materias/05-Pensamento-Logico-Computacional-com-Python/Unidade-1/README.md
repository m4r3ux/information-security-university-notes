# 1. O que é lógica de programação

A **lógica de programação** é a forma de organizar o pensamento para resolver problemas usando passos bem definidos.

---

## Ideia central

> Antes de programar, você precisa saber **como pensar a solução**

---

## Por que isso é importante?

Porque programação não é só escrever código — é:

- entender o problema
- dividir em etapas
- criar uma solução lógica

---

# 2. Pensamento computacional

É a habilidade de resolver problemas como um computador faria.

---

## Envolve principalmente:

### Decomposição

- quebrar um problema grande em partes menores

### Organização lógica

- definir ordem correta das ações

### Abstração

- focar no que é importante

### Automação

- transformar solução em passos executáveis

---

## Ideia importante para prova

> Pensamento computacional = resolver problemas de forma estruturada

---

# 3. Ferramentas da lógica de programação

Antes de codificar, usamos três ferramentas principais:

---

## 3.1 Algoritmos

### Definição

> Sequência de passos para resolver um problema

---

## Exemplo simples

Fazer café:

1. ferver água
2. colocar café no filtro
3. despejar água
4. esperar
5. servir

Isso já é um algoritmo.

---

## Características de um bom algoritmo

- claro
- finito (termina)
- eficiente
- correto

---

# 4. Exemplo clássico: média de números

Vamos analisar o exemplo do slide.

---

## Problema

Calcular a média de 5 números

---

## Passos (algoritmo)

1. pegar os números
2. somar todos
3. contar quantos são
4. dividir soma pela quantidade
5. mostrar resultado

---

## Exemplo real

Números: 4, 8, 6, 10, 2

- soma = 30
- quantidade = 5
- média = 30 ÷ 5 = 6

---

## Ideia importante

> Algoritmo = sequência lógica de passos

---

# 5. Pseudocódigo

## O que é

É uma forma de escrever algoritmos **em linguagem quase natural**.

---

## Objetivo

- facilitar entendimento
- não depender de linguagem específica

---

## Exemplo de pseudocódigo

```
início  leia n1, n2, n3, n4, n5  soma ← n1 + n2 + n3 + n4 + n5  média ← soma / 5  escreva médiafim
```

---

## Conceitos importantes

### Variáveis

- armazenam valores

### Operações

- soma, divisão, etc.

### Estruturas

- condições (if)
- repetição (loops)

---

## Ideia-chave

> Pseudocódigo serve para planejar antes de programar

---

# 6. Fluxogramas

## O que são

Representações gráficas de algoritmos

---

## Para que servem

- visualizar o fluxo da lógica
- identificar erros
- facilitar entendimento

---

## Principais símbolos

- oval → início/fim
- retângulo → processo
- losango → decisão
- paralelogramo → entrada/saída

---

## Exemplo mental

Um fluxograma pode mostrar:

- início
- ler dados
- decisão (ex: número > 0?)
- ação baseada na decisão
- fim

---

## Norma importante

- ISO 5807 → padroniza fluxogramas

---

# 7. Relação entre tudo isso

Esses três elementos trabalham juntos:

- algoritmo → ideia
- pseudocódigo → descrição textual
- fluxograma → representação visual

---

# 8. Papel do Python

O slide menciona Python porque:

- sintaxe simples
- fácil de aprender
- ideal para iniciantes

---

## Ideia importante

> Primeiro você aprende a lógica, depois aplica em uma linguagem (como Python)

---

# 9. Por que isso é o mais importante do curso

Se você dominar lógica:

- aprende qualquer linguagem
- resolve problemas com facilidade
- escreve código melhor

Se não dominar:

- vai decorar código sem entender

---

# 10. Resumo para prova

### Lógica de programação:

- organização do raciocínio

### Algoritmo:

- sequência de passos

### Pseudocódigo:

- descrição textual simplificada

### Fluxograma:

- representação gráfica

### Pensamento computacional:

- resolver problemas de forma estruturada

---

# 1. Linguagem de programação: a “ponte”

O slide começa com uma frase muito importante:

> “Uma linguagem é uma ponte”

---

## O que isso significa?

Uma linguagem de programação serve para:

- você → pensar a solução
- computador → executar a solução

---

## Ideia central

> A linguagem traduz o pensamento humano em instruções que o computador entende

---

# 2. O que é Python

Python é uma **linguagem de programação de alto nível**.

---

## Por que Python é tão usada?

Porque ela é:

- simples
- clara
- versátil
- poderosa

---

## Onde Python é usado?

- ciência de dados
- inteligência artificial
- desenvolvimento web
- automação

---

## Ideia importante

> Python não é só para iniciantes — é usada profissionalmente em grandes sistemas

---

# 3. Alto nível vs baixo nível

Esse é um conceito muito importante.

---

## Linguagens de baixo nível

Exemplo:

- Assembly

Características:

- próximas do hardware
- difíceis de entender
- muito rápidas

---

## Linguagens de alto nível (como Python)

Características:

- mais próximas da linguagem humana
- fáceis de entender
- abstraem detalhes do hardware

---

## Comparação simples

Baixo nível:

```
mover valor para registradorsomar registradores
```

Alto nível (Python):

```
resultado = a + b
```

---

## Ideia para prova

> Alto nível = mais fácil para humanos  
> Baixo nível = mais próximo do hardware

---

# 4. Compiladores vs Interpretadores

Esse é um dos pontos mais importantes do slide.

---

## Compilador

- traduz o programa inteiro antes de executar
- gera um arquivo executável

Exemplo:

- C, C++

---

## Interpretador

- executa linha por linha
- traduz enquanto roda

Exemplo:

- Python

---

## Python na prática

Python faz algo intermediário:

1. transforma o código em **bytecode**
2. executa na **máquina virtual Python**

---

## Ideia importante

> Python é interpretado (com uma etapa intermediária)

---

## Diferença prática

Compilado:

- mais rápido
- menos flexível

Interpretado:

- mais flexível
- mais fácil de testar

---

# 5. Python no ensino

Python é muito usado para aprender programação porque:

- sintaxe simples
- menos “poluição visual”
- foco na lógica

---

## O que você aprende com Python

- variáveis
- decisões (if)
- repetição (loops)
- estruturas de dados

---

## Ideia importante

> Python ajuda a aprender lógica sem distrações

---

# 6. Sintaxe do Python (muito importante)

Python tem uma característica única:

## Indentação obrigatória

---

### Exemplo:

```
idade = 12

if idade >= 18:
	print("Maior de idade")
else:
	print("Menor de idade")
```

---

## O que é indentação?

- espaços no começo da linha
- indicam blocos de código

---

## Diferença de outras linguagens

Outras usam:

- chaves { }
- ponto e vírgula ;

Python usa:

- indentação

---

## Comentários

```
# Isso é um comentário
```

Servem para:

- explicar o código
- documentar

---

# 7. Bibliotecas e frameworks

## Biblioteca

> conjunto de funções prontas

---

### Analogia

- biblioteca = caixa de ferramentas

Você escolhe o que usar.

---

## Framework

> estrutura que define como o sistema deve ser feito

---

### Analogia

- framework = planta de uma casa

Você segue um padrão.

---

## Exemplos

### Flask

- simples
- flexível

### Django

- completo
- robusto

---

## Conceito importante

**DRY (Don’t Repeat Yourself)**  
→ evitar repetição de código

---

# 8. Python na prática

O slide mostra um código. Vamos entender linha por linha.

---

## Código:

```
nome_pessoa = input("Qual é o seu nome?")
```

### O que acontece:

- pede um valor ao usuário
- armazena na variável `nome_pessoa`

---

```
print(f"Meu nome é {nome_pessoa}")
```

### O que acontece:

- imprime texto
- insere valor da variável dentro da frase

---

## Conceito importante: variável

> espaço na memória que guarda um valor

---

## Outro ponto importante: f-string

```
f"Olá {nome}"
```

Permite:

- inserir variáveis dentro de texto

---

# 9. IDEs e prática

Para programar usamos ferramentas:

- PyCharm
- VS Code

---

## Por que são importantes?

- ajudam a escrever código
- mostram erros
- facilitam execução

---

# 10. Ideia mais importante da aula

> Programar = aplicar lógica usando uma linguagem

---

# 11. Resumo para prova

### Python:

- linguagem de alto nível
- interpretada
- sintaxe simples

---

### Diferenças:

- compilador → traduz tudo antes
- interpretador → executa linha por linha

---

### Conceitos importantes:

- indentação
- variáveis
- entrada (input)
- saída (print)

---

### Bibliotecas vs frameworks:

- biblioteca → você controla
- framework → ele controla a estrutura

---

# 1. O que são estruturas condicionais

## Ideia central

> Estruturas condicionais permitem que o programa **tome decisões**

---

## Em termos simples

O programa passa a fazer:

- **se acontecer X → faça A**
- **senão → faça B**

---

## Exemplo do mundo real

- Se está chovendo → leve guarda-chuva
- Senão → não leve

Isso já é uma estrutura condicional.

---

# 2. Estrutura básica em Python

## Sintaxe

```
if condição:   
	código
```

---

## Exemplo

```
idade = 18
if idade >= 18:   
	print("Maior de idade")
```

---

## Como funciona

1. verifica a condição
2. se for verdadeira → executa o bloco
3. se não → ignora

---

# 3. if, elif, else

Agora vem a estrutura completa.

---

## Estrutura geral

```
if condição1:   
	código1el

if condição2:
    código2
else:
    código3
```

---

## O que cada um faz

### if

- primeira verificação

### elif (else if)

- outras condições

### else

- caso nenhuma condição seja verdadeira

---

## Exemplo prático

```
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
```

---

## Fluxo lógico

- testa o `if`
- se falso → vai para `elif`
- se tudo falso → executa `else`

---

## Ideia importante

> As condições são avaliadas **de cima para baixo**

---

# 4. Entrada de dados: input()

## O que faz

```
nome = input("Digite seu nome: ")
```

- captura dados do usuário
- sempre retorna **string**

---

## Cuidado importante (prova)

> input() sempre retorna texto (string)

---

# 5. Problema comum: letras maiúsculas/minúsculas

Usuário pode digitar:

- "Sim"
- "sim"
- "SIM"

---

## Solução: .lower()

```
resposta = input("Digite sim ou não: ").lower()
```

---

## O que faz

- transforma tudo em minúsculo

---

## Outro método importante: .strip()

```
texto = input().strip()
```

Remove:

- espaços antes e depois

---

## Encadeamento de métodos

```
resposta = input().strip().lower()
```

---

## Ideia importante

> Métodos podem ser encadeados para limpar e padronizar dados

---

# 6. Operadores de comparação

## Principal

```
==
```

---

## Exemplo

```
if resposta == "sim":   
	print("Você escolheu sim")
```

---

## Outros importantes

- > (maior)
    
- < (menor)
- > = (maior ou igual)
    
- <= (menor ou igual)

---

# 7. Operadores lógicos

Agora você começa a combinar condições.

---

## AND

```
if idade >= 18 and tem_carteira:
```

Só é verdadeiro se:

- tudo for verdadeiro

---

## OR

```
if tem_dinheiro or tem_cartao:
```

Verdadeiro se:

- pelo menos um for verdadeiro

---

## NOT

```
if not logado:
```

- inverte a condição

---

## Ideia para prova

- AND → tudo verdadeiro
- OR → pelo menos um
- NOT → inverte

---

# 8. Exemplo completo (bem importante)

Vamos juntar tudo:

```
resposta = input("Você alterou o passado? ").strip().lower()

if resposta == "sim":
    print("Risco de paradoxo alto")
else:
    print("Linha do tempo estável")
```

---

# 9. Exemplo com múltiplas condições (nível prova)

```
interagiu = True

alterou_evento = True

afetou_ancestral = False

if interagiu and alterou_evento:
    print("Paradoxo crítico")
elif alterou_evento or afetou_ancestral:
    print("Paradoxo moderado")
else:
    print("Sem risco")
```

---

## Análise

- AND → mais restritivo
- OR → mais flexível

---

# 10. Condições aninhadas

Você pode colocar um `if` dentro de outro.

---

## Exemplo

```
idade = 20

if idade >= 18:
    if idade >= 65:
        print("Idoso")
    else:       
		print("Adulto")
```

---

## Ideia

> Permite decisões mais específicas

---

# 11. Dot operator (.)

Isso aparece no slide.

---

## O que é

```
texto.lower()
```

O ponto (`.`) serve para:

> acessar métodos de um objeto

---

## Exemplo

```
nome.lower()
```

- objeto: nome
- método: lower

---

# 12. Por que condicionais são tão importantes

Sem condicionais:

- programa sempre faz a mesma coisa

Com condicionais:

- programa reage
- toma decisões
- se adapta

---

## Ideia central

> Condicionais tornam o programa **inteligente**

---

# 13. Resumo para prova

### Estruturas:

- if → decisão
- elif → alternativa
- else → padrão

---

### Entrada:

- input() → sempre string

---

### Métodos:

- .lower() → minúsculo
- .strip() → remove espaços

---

### Operadores:

- == → comparação
- and → tudo verdadeiro
- or → pelo menos um
- not → negação

---

# 14. Conexão com lógica de programação

Você já aprendeu:

- algoritmo → passos
- agora:  
    → você adiciona **decisões dentro desses passos**

---

# 1. O que são loops (laços de repetição)

## Ideia central

> Loops permitem repetir um bloco de código várias vezes

---

## Exemplo do mundo real

- repetir uma tarefa 10 vezes
- percorrer uma lista de nomes
- processar vários dados

---

## Sem loop

Você teria que escrever:

```
print("Olá")print("Olá")print("Olá")
```

---

## Com loop

```
for i in range(3):    print("Olá")
```

---

# 2. Loop for (o mais importante)

## Quando usar

> Quando você sabe quantas vezes vai repetir

---

## Estrutura

```
for variável in sequência:    código
```

---

## Exemplo

```
nomes = ["Ana", "Carlos", "João"]for nome in nomes:    print(nome)
```

---

## O que acontece

- pega cada elemento da lista
- executa o bloco

---

## Ideia importante

> O `for` percorre coleções (listas, strings, etc.)

---

# 3. Listas

## O que são

> Estruturas que armazenam vários valores

---

## Exemplo

```
numeros = [4, 8, 6, 10, 2]
```

---

## Características

- ordenadas
- permitem repetição
- acessadas por índice

---

## Uso com loop

```
for numero in numeros:    print(numero)
```

---

# 4. Caracteres especiais (\n)

## O que faz

```
print("Linha 1\nLinha 2")
```

Saída:

```
Linha 1Linha 2
```

---

## Ideia

> `\n` quebra linha

---

# 5. F-strings (muito importante)

## O que são

Forma moderna de inserir variáveis em texto

---

## Exemplo

```
nome = "João"print(f"Olá, {nome}")
```

---

## Vantagem

- mais legível
- mais simples

---

# 6. Loops aninhados

## O que são

> Um loop dentro de outro

---

## Para que serve

- testar todas as combinações
- simular cenários complexos

---

## Exemplo

```
anos = [2020, 2021]

eventos = ["A", "B"]

for ano in anos:    
	for evento in eventos:        
		print(f"{ano} - {evento}")
```

---

## Resultado

```
2020 - A2020 - B2021 - A2021 - B
```

---

## Ideia importante

> Loop aninhado = combina todos os elementos

---

# 7. Contadores

## O que são

Variáveis que contam algo

---

## Exemplo

```
contador = 1

for nome in ["Ana", "João"]: 
   print(f"{contador} - {nome}")    
   contador += 1
```

---

## Ideia

> contador ajuda a acompanhar iterações

---

# 8. Loop while

## Quando usar

> Quando você NÃO sabe quantas vezes vai repetir

---

## Estrutura

```
while condição:    código
```

---

## Exemplo

```
senha = ""

while senha != "123":
   senha = input("Digite a senha: ")
```

---

## Ideia importante

> while depende de uma condição

---

# 9. Diferença entre for e while

|Tipo|Quando usar|
|---|---|
|for|quantidade definida|
|while|condição dinâmica|

---

## Resumo simples

- for → previsível
- while → depende da situação

---

# 10. Dicionários

## O que são

> Estruturas que guardam pares: chave → valor

---

## Exemplo

```
eventos = {    
"2020": "Pandemia", 
"1969": "Lua"}
```

---

## Acesso

```
print(eventos["2020"])
```

---

## Loop em dicionário

```
for chave, valor in eventos.items():
    print(f"{chave}: {valor}")
```

---

## Ideia importante

> Dicionário organiza dados estruturados

---

# 11. Controle de loops

## break

Interrompe o loop

```
for i in range(10):
    if i == 5:
    break
```

---

## continue

Pula para a próxima repetição

```
for i in range(5):
    if i == 2:
    continue
    print(i)
```

---

## Ideia

- break → para tudo
- continue → pula

---

# 12. Loops infinitos (cuidado!)

## Exemplo perigoso

```
while True:
print("Nunca para")
```

---

## Problema

- trava o programa
- consome recursos

---

## Como evitar

- sempre ter condição de parada

---

# 13. Boas práticas (isso cai bastante)

### 1. Inicializar variáveis

```
contador = 0
```

---

### 2. Indentação correta

Python depende disso

---

### 3. Evitar loops infinitos

---

### 4. Usar mensagens claras

---

### 5. Validar entradas

---

# 14. Conexão com o que você já aprendeu

Agora você tem:

- lógica → pensar
- condicionais → decidir
- loops → repetir

---

## Isso forma a base de QUALQUER programa

---

# 15. Resumo para prova

### Loop for

- percorre listas
- número definido

---

### Loop while

- depende de condição

---

### Listas

- armazenam valores

---

### Dicionários

- chave → valor

---

### Controle

- break → interrompe
- continue → pula

---

### Loops aninhados

- combinam elementos

---

# 16. Visão final (muito importante)

> Condicional = decisão  
> Loop = repetição  
> Juntos = lógica completa de um programa