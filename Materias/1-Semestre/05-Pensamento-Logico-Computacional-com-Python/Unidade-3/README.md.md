# Introdução às listas em Python

As listas são uma das estruturas de dados mais importantes do Python. Elas permitem armazenar vários valores em uma única variável, organizados em sequência. Diferentemente de uma variável simples, que guarda apenas um valor, uma lista pode reunir diversos elementos relacionados, facilitando o processamento de dados.

Uma característica fundamental das listas é a mutabilidade. Isso significa que seus elementos podem ser alterados após a criação da lista, permitindo adicionar, remover ou modificar informações sem recriar toda a estrutura. Essa flexibilidade faz com que listas sejam amplamente utilizadas em algoritmos, aplicações de inteligência artificial, análise de dados e sistemas em geral.

Os elementos de uma lista são acessados por índices numéricos, iniciando em zero. Assim, o primeiro elemento ocupa a posição 0, o segundo ocupa a posição 1 e assim por diante.

Exemplo:

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # maçã
print(frutas[1])  # banana
```

---

# Manipulação de listas: adição e remoção de elementos

Python oferece diversos métodos para modificar listas de forma eficiente.

## Adicionando elementos

O método `append()` adiciona um elemento ao final da lista:

```python
nomes = ["Ana", "Carlos"]
nomes.append("Marina")

print(nomes)
```

Resultado:

```python
['Ana', 'Carlos', 'Marina']
```

Já o método `insert()` permite inserir um elemento em uma posição específica:

```python
nomes.insert(1, "Pedro")

print(nomes)
```

Resultado:

```python
['Ana', 'Pedro', 'Carlos', 'Marina']
```

---

## Removendo elementos

O método `remove()` elimina um elemento pelo valor:

```python
nomes.remove("Carlos")
```

O método `pop()` remove um elemento pela posição:

```python
nomes.pop(0)
```

Também é possível usar `del`:

```python
del nomes[1]
```

Para limpar completamente a lista:

```python
nomes.clear()
```

Essas operações tornam listas ideais para dados dinâmicos, em que informações precisam ser constantemente atualizadas.

---

# Ordenação e reorganização de listas

Frequentemente precisamos organizar dados armazenados em listas.

## Método `sort()`

Organiza a própria lista:

```python
numeros = [8, 3, 1, 5]

numeros.sort()

print(numeros)
```

Resultado:

```python
[1, 3, 5, 8]
```

Para ordem decrescente:

```python
numeros.sort(reverse=True)
```

---

## Função `sorted()`

Cria uma versão ordenada sem alterar a lista original:

```python
valores = [7, 2, 9]

ordenada = sorted(valores)

print(ordenada)
print(valores)
```

---

## Método `reverse()`

Inverte a ordem dos elementos:

```python
valores.reverse()

print(valores)
```

Essas técnicas são muito utilizadas em sistemas que organizam eventos cronológicos, rankings ou grandes volumes de dados.

---

# Acessando e modificando elementos

Os elementos podem ser acessados diretamente pelos índices.

```python
cores = ["azul", "verde", "vermelho"]

print(cores[0])
print(cores[-1])
```

Resultado:

```python
azul
vermelho
```

O índice negativo permite acessar elementos a partir do final da lista.

---

## Modificando elementos

```python
cores[1] = "amarelo"

print(cores)
```

Resultado:

```python
['azul', 'amarelo', 'vermelho']
```

---

# Fatiamento (slicing)

O slicing permite extrair partes da lista usando:

```python
lista[início:fim:passo]
```

Exemplo:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])
```

Resultado:

```python
[20, 30, 40]
```

---

## Passo no slicing

```python
print(numeros[::2])
```

Resultado:

```python
[10, 30, 50]
```

---

## Invertendo com slicing

```python
print(numeros[::-1])
```

Resultado:

```python
[50, 40, 30, 20, 10]
```

O slicing é extremamente importante para manipulação eficiente de dados.

---

# Exemplo prático: planejamento de viagens no tempo

Imagine um sistema que armazena anos históricos que um viajante deseja visitar.

```python
quantidade = int(input("Quantos destinos deseja cadastrar? "))

destinos = []

for i in range(quantidade):
    ano = int(input("Digite um ano: "))
    destinos.append(ano)

print("Lista completa:", destinos)
```

---

## Exibindo os primeiros destinos

```python
primeiros = destinos[0:3]

print("Primeiros destinos:", primeiros)
```

---

## Exibindo os últimos destinos

```python
ultimos = destinos[-2:]

print("Últimos destinos:", ultimos)
```

---

## Destinos alternados

```python
alternados = destinos[::2]

print("Destinos alternados:", alternados)
```

---

## Invertendo a ordem da viagem

```python
invertidos = destinos[::-1]

print("Ordem invertida:", invertidos)
```

Esse exemplo demonstra como listas podem organizar sequências temporais de maneira prática e flexível.

---

# Análise de dados em listas com funções nativas

Python possui funções prontas para análise de listas numéricas.

## Quantidade de elementos

```python
valores = [5, 8, 10, 3]

print(len(valores))
```

Resultado:

```python
4
```

---

## Maior e menor valor

```python
print(max(valores))
print(min(valores))
```

Resultado:

```python
10
3
```

---

## Soma dos elementos

```python
print(sum(valores))
```

Resultado:

```python
26
```

Essas funções são muito utilizadas em estatística, ciência de dados e relatórios computacionais.

---

# Comparação entre listas e tuplas

Embora parecidas, listas e tuplas possuem diferenças importantes.

|Característica|Lista|Tupla|
|---|---|---|
|Mutabilidade|Mutável|Imutável|
|Sintaxe|`[]`|`()`|
|Alteração de elementos|Permitida|Não permitida|
|Uso comum|Dados dinâmicos|Dados fixos|

Exemplo de lista:

```python
lista = [1, 2, 3]
```

Exemplo de tupla:

```python
tupla = (1, 2, 3)
```

As tuplas são mais seguras para armazenar dados que não devem ser alterados, como coordenadas geográficas ou registros fixos.

---

# Considerações finais

As listas são estruturas fundamentais no Python devido à sua flexibilidade, capacidade de armazenamento e facilidade de manipulação. Elas permitem organizar dados sequenciais de forma eficiente, sendo amplamente utilizadas em aplicações modernas.

Dominar operações como inserção, remoção, ordenação, slicing e análise de listas é essencial para o desenvolvimento de algoritmos robustos e para a manipulação eficiente de dados em sistemas computacionais.

---

# Dicionários em Python – Estrutura e funcionalidade

Os dicionários são estruturas de dados extremamente importantes em Python. Diferentemente das listas, que armazenam elementos em sequência utilizando índices numéricos, os dicionários organizam informações em pares de chave e valor.

Essa estrutura permite acessar dados de forma rápida e eficiente, utilizando uma chave única como identificador. Assim, em vez de procurar um elemento percorrendo toda a estrutura, basta informar sua chave correspondente.

Os dicionários são amplamente utilizados em sistemas modernos porque permitem representar informações complexas de maneira organizada, clara e flexível.

Exemplo básico:

```python
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "Computação"
}

print(aluno)
```

Resultado:

```python
{'nome': 'Carlos', 'idade': 21, 'curso': 'Computação'}
```

---

# Comparação entre listas e dicionários

Embora listas e dicionários sejam estruturas de armazenamento, cada uma possui características próprias.

|Estrutura|Forma de acesso|Melhor uso|
|---|---|---|
|Lista|Índices numéricos|Dados ordenados|
|Dicionário|Chaves|Relacionamento de informações|

---

## Exemplo com lista

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[1])
```

Resultado:

```python
banana
```

Aqui, o acesso depende da posição do elemento.

---

## Exemplo com dicionário

```python
produto = {
    "nome": "Notebook",
    "preco": 3500
}

print(produto["nome"])
```

Resultado:

```python
Notebook
```

Nesse caso, o acesso é feito diretamente pela chave.

---

# Chaves e valores – Organização dos dados

Nos dicionários, cada informação é formada por:

- chave → identificador;
    
- valor → dado armazenado.
    

Exemplo:

```python
pessoa = {
    "nome": "Ana",
    "idade": 25
}
```

- `"nome"` é a chave;
    
- `"Ana"` é o valor associado.
    

---

## Características importantes das chaves

As chaves:

- devem ser únicas;
    
- devem ser imutáveis;
    
- podem ser strings, números ou tuplas.
    

Exemplo válido:

```python
dados = {
    1: "João",
    2: "Maria"
}
```

---

## Valores podem ser variados

Os valores podem armazenar praticamente qualquer tipo de dado:

```python
usuario = {
    "nome": "Lucas",
    "idade": 30,
    "hobbies": ["música", "xadrez"],
    "ativo": True
}
```

Essa flexibilidade torna os dicionários muito poderosos.

---

# Modificando dados em dicionários

Alterar informações é simples: basta utilizar a chave correspondente.

```python
usuario = {
    "nome": "Pedro",
    "idade": 20
}

usuario["idade"] = 21

print(usuario)
```

Resultado:

```python
{'nome': 'Pedro', 'idade': 21}
```

---

## Adicionando novos dados

```python
usuario["cidade"] = "São Paulo"
```

Resultado:

```python
{'nome': 'Pedro', 'idade': 21, 'cidade': 'São Paulo'}
```

---

# Eficiência na busca de dados

Uma das maiores vantagens dos dicionários é a velocidade de acesso às informações.

Isso ocorre porque Python utiliza tabelas hash internamente. Assim, o sistema localiza rapidamente a posição do dado associado à chave.

Enquanto listas normalmente precisam percorrer os elementos sequencialmente, os dicionários realizam buscas quase instantâneas.

Por isso, eles são amplamente utilizados em:

- sistemas de autenticação;
    
- bancos de dados em memória;
    
- APIs;
    
- aplicações web;
    
- indexação de informações.
    

---

# Dicionários e o formato JSON

O JSON (JavaScript Object Notation) é um formato extremamente utilizado para troca de dados entre sistemas.

Sua estrutura é praticamente igual à dos dicionários Python:

- chaves;
    
- valores;
    
- objetos aninhados;
    
- listas.
    

---

## Exemplo de JSON

```json
{
    "nome": "Maria",
    "idade": 28,
    "cidade": "Rio de Janeiro"
}
```

Esse formato é muito utilizado em APIs e aplicações web.

---

# Conversão entre dicionários e JSON

Python possui o módulo `json` para realizar conversões.

## Dicionário para JSON

```python
import json

dados = {
    "nome": "Carlos",
    "idade": 40
}

json_texto = json.dumps(dados)

print(json_texto)
```

---

## JSON para dicionário

```python
import json

texto = '{"nome": "Ana", "idade": 22}'

dicionario = json.loads(texto)

print(dicionario)
```

---

# Exemplo prático: receita em formato JSON

```python
receita = {
    "nome": "Bolo de Chocolate",
    "porcoes": 8,
    "ingredientes": [
        "farinha",
        "ovos",
        "leite",
        "chocolate"
    ]
}

print(receita)
```

Nesse exemplo:

- o dicionário principal representa a receita;
    
- a lista armazena os ingredientes;
    
- cada chave organiza uma informação específica.
    

Essa estrutura é muito comum em sistemas modernos.

---

# Armazenando perfis de usuários

Dicionários são ideais para representar pessoas, produtos ou registros.

Exemplo:

```python
usuario = {
    "nome": "Fernanda",
    "idade": 29,
    "cidade": "Curitiba"
}

print(usuario["nome"])
```

Resultado:

```python
Fernanda
```

---

# Dicionários aninhados

Também é possível criar estruturas mais complexas.

```python
usuario = {
    "nome": "João",
    "endereco": {
        "cidade": "Campinas",
        "estado": "SP"
    }
}

print(usuario["endereco"]["cidade"])
```

Resultado:

```python
Campinas
```

Essa técnica é muito usada em sistemas corporativos e APIs.

---

# Exemplo prático – Perfil de viajante do tempo

```python
perfil_viajante = {}

nome = input("Insira o seu nome: ")
idade = int(input("Insira sua idade: "))
ano_origem = int(input("Insira o ano de origem: "))

perfil_viajante["nome"] = nome
perfil_viajante["idade"] = idade
perfil_viajante["ano_origem"] = ano_origem

print("Perfil do viajante:", perfil_viajante)
```

---

## Acessando informações específicas

```python
print("Nome:", perfil_viajante["nome"])
```

---

## Adicionando novos atributos

```python
perfil_viajante["destino"] = 3025
```

---

# Operações úteis com dicionários

## Verificando chaves

```python
print("idade" in perfil_viajante)
```

---

## Obtendo todas as chaves

```python
print(perfil_viajante.keys())
```

---

## Obtendo todos os valores

```python
print(perfil_viajante.values())
```

---

## Percorrendo o dicionário

```python
for chave, valor in perfil_viajante.items():
    print(chave, ":", valor)
```

---

# Considerações finais

Os dicionários são estruturas fundamentais na programação moderna devido à sua eficiência, flexibilidade e organização.

Sua capacidade de armazenar informações em pares chave-valor permite representar entidades complexas de forma intuitiva e eficiente.

Além disso, a compatibilidade com JSON torna os dicionários indispensáveis no desenvolvimento de aplicações web, APIs, bancos de dados e sistemas distribuídos.

Dominar o uso de dicionários é essencial para qualquer programador que deseje criar sistemas organizados, escaláveis e eficientes em Python.

---

# Unidade III — Pensamento Lógico Computacional com Python

## Input e Output (I/O) em Python

Input e Output (Entrada e Saída de dados) são fundamentais em qualquer programa.  
Sem entrada, o programa não recebe informações. Sem saída, ele não consegue mostrar resultados.

---

# 1. O que é Input e Output?

## Entrada de dados (Input)

É quando o programa recebe informações.

Essas informações podem vir de:

- teclado;
    
- arquivos;
    
- sensores;
    
- internet;
    
- banco de dados.
    

Exemplo:

```python
nome = input("Digite seu nome: ")
```

Aqui, o usuário fornece um dado ao programa.

---

## Saída de dados (Output)

É quando o programa mostra informações.

Pode ocorrer:

- no console;
    
- em arquivos;
    
- em telas gráficas;
    
- na rede.
    

Exemplo:

```python
print("Olá!")
```

---

# 2. A função input()

A função `input()` permite interação com o usuário.

## Estrutura básica

```python
variavel = input("Mensagem")
```

Exemplo:

```python
cidade = input("Digite sua cidade: ")
print(cidade)
```

---

# 3. Como o input() funciona

Tudo digitado no `input()` é recebido como texto (`string`).

Mesmo números entram como string.

Exemplo:

```python
idade = input("Digite sua idade: ")

print(type(idade))
```

Saída:

```python
<class 'str'>
```

---

# 4. Conversão de tipos

Como o `input()` retorna string, muitas vezes precisamos converter os dados.

---

## int() → inteiro

```python
idade = int(input("Digite sua idade: "))
```

---

## float() → decimal

```python
altura = float(input("Digite sua altura: "))
```

---

## bool() → booleano

```python
ativo = bool(input("Digite algo: "))
```

⚠️ Atenção:  
Qualquer texto não vazio vira `True`.

---

# 5. Console e Prompt

## Console

É a interface textual onde executamos programas.

Exemplos:

- Terminal Linux;
    
- Prompt de comando Windows;
    
- VS Code terminal;
    
- PyCharm terminal.
    

---

## Prompt

É o símbolo que indica que o sistema está aguardando comandos.

Exemplos:

- Linux:
    

```bash
$
```

- Windows:
    

```bash
>
```

---

# 6. Exibindo dados com print()

A função `print()` mostra informações na tela.

---

## Exemplo simples

```python
print("Python")
```

---

## Exibindo várias informações

```python
nome = "Ana"
idade = 20

print(nome, idade)
```

---

# 7. Parâmetro sep

Define o separador entre os valores.

Exemplo:

```python
print("Python", "Java", "C++", sep=" - ")
```

Saída:

```python
Python - Java - C++
```

---

# 8. Parâmetro end

Define como a linha termina.

Normalmente:

```python
end="\n"
```

Exemplo:

```python
print("Olá", end=" ")
print("Mundo")
```

Saída:

```python
Olá Mundo
```

---

# 9. f-strings

Forma moderna e organizada de exibir variáveis.

## Sintaxe

```python
f"texto {variavel}"
```

Exemplo:

```python
nome = "Carlos"
idade = 30

print(f"{nome} possui {idade} anos.")
```

---

# 10. Tratamento de erros

Usuários podem digitar valores inválidos.

Exemplo problemático:

```python
idade = int(input("Digite sua idade: "))
```

Se o usuário digitar:

```python
abc
```

ocorrerá erro.

---

# 11. try-except

Serve para evitar que o programa pare inesperadamente.

## Exemplo

```python
try:
    idade = int(input("Digite sua idade: "))
    print(idade)

except:
    print("Valor inválido.")
```

---

# 12. Exemplo completo — Viagem no tempo

Esse exemplo reúne:

- input;
    
- print;
    
- conversão;
    
- condição;
    
- interação.
    

```python
from datetime import datetime

ano_atual = datetime.now().year

ano_destino = int(input("Digite o ano da viagem: "))

objetivo = input("Qual o objetivo da viagem? ")

print("\n--- VIAGEM TEMPORAL ---")

print(f"Ano atual: {ano_atual}")
print(f"Ano destino: {ano_destino}")
print(f"Objetivo: {objetivo}")

if ano_destino > ano_atual:
    print("Viagem ao futuro")

elif ano_destino < ano_atual:
    print("Viagem ao passado")

else:
    print("Permaneceu no presente")
```

---

# 13. Escrita em arquivos

Além do console, programas podem salvar dados em arquivos.

---

## Abrindo um arquivo

```python
arquivo = open("dados.txt", "w")
```

### Modos:

| Modo  | Função    |
| ----- | --------- |
| `"w"` | escrever  |
| `"r"` | ler       |
| `"a"` | adicionar |

---

## Escrevendo no arquivo

```python
arquivo.write("Olá mundo")
```

---

## Fechando o arquivo

```python
arquivo.close()
```

---

# 14. Exemplo completo de escrita

```python
nome = input("Digite seu nome: ")

arquivo = open("usuarios.txt", "a")

arquivo.write(nome + "\n")

arquivo.close()

print("Nome salvo com sucesso.")
```

---

# 15. Leitura de arquivos

## Exemplo

```python
arquivo = open("usuarios.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()
```

---

# 16. Resumo geral

|Conceito|Função|
|---|---|
|`input()`|recebe dados|
|`print()`|mostra dados|
|`int()`|converte para inteiro|
|`float()`|converte para decimal|
|`try-except`|trata erros|
|`open()`|abre arquivos|
|`write()`|escreve em arquivos|
|`read()`|lê arquivos|

---

# 17. Relação prática com desenvolvimento

Esses conceitos aparecem em:

- sistemas bancários;
    
- jogos;
    
- inteligência artificial;
    
- formulários;
    
- APIs;
    
- automação;
    
- análise de dados;
    
- chatbots;
    
- sistemas web.
    

Input e Output são literalmente a “porta de comunicação” entre:

- usuário;
    
- programa;
    
- sistema operacional;
    
- arquivos;
    
- internet.
    

---

# 18. Ponto mais importante da unidade

A grande ideia da unidade é:

- coletar dados;
    
- processar dados;
    
- apresentar resultados.
    

Ou seja:

```text
Entrada → Processamento → Saída
```

Esse é o ciclo básico de praticamente qualquer software.

---

# Unidade III — Escrita e Leitura de Arquivos em Python

Agora entramos em uma parte extremamente importante da programação:  
o armazenamento permanente de dados.

Até aqui, os dados existiam apenas enquanto o programa estava executando.  
Quando o programa terminava, tudo era perdido.

Os arquivos resolvem exatamente esse problema.

---

# 1. O que é escrita de arquivos?

A escrita de arquivos permite:

- salvar informações;
    
- registrar dados;
    
- armazenar configurações;
    
- criar históricos;
    
- persistir dados após o encerramento do programa.
    

Sem arquivos:

```text
Programa fecha → dados desaparecem
```

Com arquivos:

```text
Programa fecha → dados continuam salvos
```

---

# 2. A função open()

Em Python, usamos a função `open()` para trabalhar com arquivos.

## Estrutura

```python
open(nome_arquivo, modo)
```

Exemplo:

```python
arquivo = open("dados.txt", "w")
```

---

# 3. Principais modos de abertura

|Modo|Função|
|---|---|
|`"r"`|leitura|
|`"w"`|escrita|
|`"a"`|adicionar conteúdo|
|`"x"`|criar arquivo novo|
|`"rb"`|leitura binária|
|`"wb"`|escrita binária|
|`"r+"`|leitura e escrita|

---

# 4. Modo `"r"` — leitura

Abre um arquivo existente para leitura.

```python
arquivo = open("dados.txt", "r")
```

⚠️ Se o arquivo não existir:

```text
FileNotFoundError
```

---

# 5. Modo `"w"` — escrita

Cria um arquivo novo.

Se o arquivo já existir:  
✅ ele será apagado e recriado.

```python
arquivo = open("dados.txt", "w")
```

---

# 6. Modo `"a"` — append

Adiciona conteúdo ao final do arquivo sem apagar os dados anteriores.

Muito usado em:

- logs;
    
- históricos;
    
- registros;
    
- relatórios.
    

```python
arquivo = open("dados.txt", "a")
```

---

# 7. Modo `"x"` — criação exclusiva

Cria um novo arquivo.

Se ele já existir:  
❌ ocorre erro.

```python
arquivo = open("dados.txt", "x")
```

---

# 8. Arquivos de texto e binários

---

## Arquivos de texto

São legíveis por humanos.

Exemplos:

- `.txt`
    
- `.csv`
    
- `.json`
    

---

## Arquivos binários

Armazenam dados compactados ou estruturados.

Exemplos:

- imagens;
    
- vídeos;
    
- PDFs;
    
- executáveis.
    

---

# 9. Trabalhando com arquivos binários

Usamos o modo `b`.

## Exemplo

```python
arquivo = open("foto.jpg", "rb")
```

---

# 10. UTF-8 e codificação

A codificação define como caracteres são armazenados.

O padrão moderno é:

```text
UTF-8
```

Ele suporta:

- acentos;
    
- símbolos;
    
- múltiplos idiomas.
    

---

# 11. Abrindo arquivos com UTF-8

```python
arquivo = open("texto.txt", "w", encoding="utf-8")
```

Isso evita problemas como:

```text
Ã§
Ã¡
Ã£
```

---

# 12. Escrevendo em arquivos

Usamos:

```python
write()
```

---

## Exemplo

```python
arquivo = open("dados.txt", "w", encoding="utf-8")

arquivo.write("Olá mundo")

arquivo.close()
```

---

# 13. Quebra de linha

O `write()` NÃO quebra linha automaticamente.

Precisamos usar:

```python
\n
```

Exemplo:

```python
arquivo.write("Linha 1\n")
arquivo.write("Linha 2\n")
```

---

# 14. writelines()

Escreve várias linhas de uma vez.

## Exemplo

```python
linhas = ["Python\n", "Java\n", "C++\n"]

arquivo.writelines(linhas)
```

---

# 15. Fechando arquivos

Sempre devemos fechar arquivos.

```python
arquivo.close()
```

Isso:

- libera memória;
    
- salva corretamente;
    
- evita corrupção.
    

---

# 16. O comando with

Forma moderna e segura.

O arquivo fecha automaticamente.

## Exemplo

```python
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Python")
```

---

# 17. Leitura de arquivos

---

## read()

Lê todo o conteúdo.

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

---

# 18. readlines()

Lê linha por linha e devolve uma lista.

## Exemplo

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(linhas)
```

Resultado:

```python
['Linha 1\n', 'Linha 2\n']
```

---

# 19. Leitura eficiente com for

Ideal para arquivos grandes.

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

---

# 20. Verificando existência de arquivos

Usamos:

```python
os.path.exists()
```

---

## Exemplo

```python
import os

if os.path.exists("dados.txt"):
    print("Arquivo existe")
else:
    print("Arquivo não encontrado")
```

---

# 21. Exemplo completo — Registro de viagens temporais

```python
from datetime import datetime

ano = input("Ano visitado: ")
descricao = input("Descreva sua viagem: ")

data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("registro.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{data} - Ano: {ano} - {descricao}\n")

print("Registro salvo.")
```

---

# 22. Consultando registros

```python
with open("registro.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())
```

---

# 23. JSON e armazenamento de dados

JSON é um formato baseado em:

```text
chave : valor
```

Muito usado em:

- APIs;
    
- sistemas web;
    
- configurações;
    
- bancos NoSQL.
    

---

# 24. JSON e dicionários

Dicionários Python combinam perfeitamente com JSON.

---

## Exemplo de dicionário

```python
config = {
    "tema": "escuro",
    "volume": 80
}
```

---

# 25. Salvando JSON

Usamos:

```python
json.dump()
```

---

## Exemplo

```python
import json

config = {
    "modo": "gradual",
    "energia": 5000
}

with open("config.json", "w", encoding="utf-8") as arquivo:
    json.dump(config, arquivo, indent=4)
```

---

# 26. Lendo JSON

Usamos:

```python
json.load()
```

---

## Exemplo

```python
import json

with open("config.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
```

---

# 27. Vantagens do JSON

✅ Legível  
✅ Leve  
✅ Compatível com internet  
✅ Fácil integração  
✅ Muito usado em APIs

---

# 28. Relação prática com sistemas reais

Esses conceitos aparecem em:

- bancos;
    
- redes sociais;
    
- jogos;
    
- aplicativos;
    
- inteligência artificial;
    
- sistemas web;
    
- APIs REST;
    
- armazenamento de usuários;
    
- logs de segurança.
    

---

# 29. Fluxo completo de persistência

```text
Usuário → input()
          ↓
Processamento
          ↓
Arquivo/JSON
          ↓
Armazenamento permanente
          ↓
Recuperação futura
```

---

# 30. Conceito central da unidade

A ideia principal é:

```text
Memória RAM é temporária.
Arquivos tornam os dados permanentes.
```

Ou seja:

- listas e dicionários organizam dados na memória;
    
- arquivos permitem salvar esses dados;
    
- JSON estrutura as informações de maneira portátil e moderna.