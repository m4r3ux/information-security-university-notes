# 1. Ideia central: “tudo em Python é objeto”

Esse é o ponto mais importante do slide.

Em Python:

> **tudo é um objeto** — números, textos, listas, etc.

Mas o que isso significa na prática?

Um objeto tem duas coisas:

- **dados** (o valor que ele guarda)
- **comportamentos** (o que ele pode fazer — métodos)

---

## Exemplo simples

```
x = 10
```

Aqui:

- `10` é um objeto do tipo `int`
- ele pode:
    - somar → `x + 5`
    - verificar bits → `x.bit_length()`

---

## Conceito importante

- **Classe** → modelo (ex: `int`)
- **Instância** → objeto criado (ex: `10`)

---

# 2. Números inteiros (int) e precisão arbitrária

Em muitas linguagens, números têm limite (ex: 32 bits, 64 bits).

Em Python:

> **inteiros não têm limite fixo**

Exemplo:

```
x = 999999999999999999999999999999
```

Funciona normalmente.

Isso acontece porque o Python:

- aloca memória dinamicamente
- representa números internamente em **binário**

---

# 3. Exemplo prático: distância temporal

Aqui o slide conecta teoria com prática.

## Lógica do problema

Você tem:

- ano inicial
- ano final

E quer saber:

- direção (passado ou futuro)
- distância

---

## Código conceitual

```
inicio = int(input("Ano inicial: "))

fim = int(input("Ano final: "))

diferenca = fim - inicio

if diferenca > 0:
    print("Futuro")
elif diferenca < 0:
    print("Passado")
else:
    print("Mesmo ano")
    print("Distância:", abs(diferenca))
```

---

## Conceitos usados aqui

- `int()` → conversão de string para número
- `abs()` → valor absoluto
- condicionais (`if`)
- operações matemáticas

---

# 4. Operadores aritméticos

Esses são os “blocos básicos” de cálculo.

|Operador|Função|
|---|---|
|`+`|soma|
|`-`|subtração|
|`*`|multiplicação|
|`//`|divisão inteira|
|`%`|resto (módulo)|
|`**`|potência|

---

## Destaques importantes

### Divisão inteira (`//`)

```
7 // 2 = 3
```

Usado quando você quer:

- contagem
- distribuição

---

### Módulo (`%`)

```
7 % 2 = 1
```

Usado para:

- verificar pares/ímpares
- ciclos

---

# 5. Operações com bits (nível mais baixo)

Aqui você chega mais perto do funcionamento do hardware.

## Operadores

| Operador | Função           |
| -------- | ---------------- |
| `&`      | AND              |
| `        | `                |
| `^`      | XOR              |
| `~`      | NOT              |
| `<<`     | desloca esquerda |
| `>>`     | desloca direita  |

---

## Exemplo

```
5 << 1  # 10
```

Isso equivale a:

> multiplicar por 2

---

## Método importante

```
x.bit_length()
```

Retorna quantos bits são necessários para representar o número.

---

# 6. Números de ponto flutuante (float)

São números com decimal:

```
3.14
```

---

## Problema importante: precisão

Nem todo número decimal pode ser representado exatamente em binário.

Exemplo clássico:

```
0.1 + 0.2
```

Resultado:

```
0.30000000000000004
```

---

## Por quê?

- o computador usa base 2 (binário)
- algumas frações não são exatas nessa base

---

## Solução

Python oferece:

```
from decimal import Decimal
```

Para maior precisão (ex: sistemas financeiros)

---

# 7. Números complexos

Formato:

```
a + bj
```

Exemplo:

```
z = 2 + 3j
```

---

## Operações

```
z.real   # parte realz.imag   # parte imagináriaabs(z)   # módulo
```

---

## Onde isso é usado?

- engenharia elétrica
- física
- processamento de sinais

---

# 8. Strings (texto)

Strings são:

> sequências de caracteres

Exemplo:

```
texto = "Python"
```

---

## Característica importante

> Strings são **imutáveis**

Você não altera diretamente — cria uma nova.

---

## Manipulações comuns

### Fatiamento

```
texto[0:3]  # "Pyt"texto[::-1] # invertido
```

---

### Métodos úteis

```
.lower().upper().capitalize().replace().strip()
```

---

# 9. Unicode (muito importante)

Unicode permite:

> representar qualquer idioma

Exemplo:

- acentos
- símbolos
- caracteres internacionais

---

# 10. Codificação de mensagens

Exemplo simples:

```
msg = "python"print(msg[::-1])  # "nohtyp"
```

Isso é:

- uma forma básica de “criptografia”
- útil para aprendizado de manipulação de strings

---

# 11. Entrada de dados

```
input()
```

Importante:

> Sempre retorna **string**

Por isso usamos:

```
int(input())
```

---

# 12. Formatação de strings

## Métodos úteis

```
.strip()   # remove espaços.title()   # primeira letra maiúscula
```

---

## f-strings (muito importante)

```
nome = "Ana"print(f"Olá {nome}")
```

---

# 13. Conectando tudo (visão geral)

Esse slide mostra que Python permite:

- trabalhar com **números**
- manipular **texto**
- fazer **cálculos complexos**
- representar dados de forma estruturada

Tudo isso porque:

> tudo é objeto → com dados + comportamentos

---

# 14. Resumo final (para fixar)

- Python trata tudo como objeto
- Inteiros são ilimitados
- Floats têm imprecisão
- Complexos são suportados nativamente
- Strings são imutáveis e poderosas
- Bits mostram o nível mais baixo da computação
- Métodos facilitam manipulação

---

Se quiser, posso te passar exercícios práticos (bem estilo prova) usando exatamente esses conceitos para você treinar de verdade.

---

## 1. O que é uma variável em Python (base de tudo)

O slide começa com uma ideia MUITO importante:

Variável é um nome simbólico que referencia um objeto na memória

Isso muda completamente a forma de pensar.

❌ Pensamento comum (errado):

“a variável guarda o valor”

✅ Pensamento correto:

“a variável aponta para um objeto na memória”

Exemplo:
```python
a = 10
```
O que acontece:

Python cria um objeto com valor 10
A variável a aponta para esse objeto

## 2. Tipagem dinâmica

Python permite mudar o tipo da variável:

```python
x = 10
x = "Olá"
```
Isso significa:

Não precisa declarar tipo
O tipo depende do valor
Vantagem:
Mais fácil de programar
Desvantagem:
Pode causar erros se você não prestar atenção

## 3. Variáveis armazenam REFERÊNCIAS (isso cai em prova)
```python
a = 10
b = a
```
Agora:

a e b apontam para o mesmo objeto

Podemos verificar com:

```python
print(id(a))
print(id(b))
```
Se for igual → mesmo objeto

## 4. Função id()

O slide cita isso diretamente.

O que faz:

Retorna o identificador único do objeto (como se fosse o endereço)

Serve para:

Ver se duas variáveis apontam para o mesmo lugar
Entender comportamento de memória

## 5. Atribuição e mudança de valor

Agora vem um ponto essencial:

```python
a = 10
b = a

a = 20
```
Resultado:

a passa a apontar para 20
b continua apontando para 10
Por quê?

Porque números são imutáveis

## 6. Objetos mutáveis vs imutáveis (um dos pontos MAIS importantes)
Imutáveis:
- int
- float
- string
- tupla

👉 Quando muda, cria outro objeto

Mutáveis:
- lista
- dicionário
- conjunto

👉 Podem ser alterados sem criar novo objeto

Exemplo MUITO importante:
```python
lista1 = [1, 2, 3]
lista2 = lista1

lista1.append(4)
```
Resultado:

[1, 2, 3, 4]

para as duas variáveis

👉 Porque ambas apontam para o MESMO objeto

## 7. Alocação dinâmica de memória

Python controla automaticamente:

onde guardar objetos
quando liberar memória
Importante:
O endereço pode mudar cada vez que você executa o programa
Você não controla isso
Regra fundamental:

Mudar uma variável pode ou não afetar outra — depende do tipo (mutável ou não)

## 8. Criação de novos objetos
Em imutáveis:

Sempre cria novo objeto

```python
x = 10
x = 20
```
Em mutáveis:

Pode modificar o mesmo objeto

```python
lista = [1,2]
lista.append(3)
```
## 9. Cópias (para evitar problemas)
Cópia simples:
```python
lista2 = lista1.copy()
```
Cópia profunda:
```python
import copy
lista2 = copy.deepcopy(lista1)
```
Diferença:
copy → copia superficial
deepcopy → copia tudo

## 10. Tipos de dados

O slide lista vários — vamos entender cada um:

Inteiros
```python
x = 10
```
Float
```python
y = 3.14
```
String
```python
nome = "Ana"
```
Lista (mutável)
```python
lista = [1,2,3]
```
Tupla (imutável)
```python
coord = (10,20)
```
Dicionário
```python
pessoa = {"nome": "Ana"}
```
Conjunto (set)
```python
nums = {1,2,3}
```
## 11. Exemplo: máquina do tempo
```python
ano_destino = 2050
coordenadas = (-23.5, -46.6)
modo = "instantaneo"
```
Aqui vemos:

inteiro → ano
tupla → posição
string → modo

👉 Organização de dados

## 12. Operadores de atribuição
```python
x = 10
x += 5
x -= 2
x *= 3
x /= 2
```
São atalhos para operações

## 13. Operadores de identidade (isso cai MUITO)
- is → mesmo objeto
- == → mesmo valor
```python
a = [1,2]
b = a

print(a is b)  # True
a = [1,2]
b = [1,2]

print(a == b)  # True
print(a is b)  # False
```
## 14. Operador in
```python
lista = [1,2,3]
print(2 in lista)
```
Serve para:

verificar se algo está dentro de uma estrutura

## 15. Exemplo completo (comparação de anos)

Esse exemplo junta vários conceitos:

```python
ano_presente = 2030

ano1 = int(input("Ano 1: "))
ano2 = int(input("Ano 2: "))

d1 = abs(ano1 - ano_presente)
d2 = abs(ano2 - ano_presente)

if d1 > d2:
    print(f"{ano1} está mais distante")
elif d2 > d1:
    print(f"{ano2} está mais distante")
else:
    print("Mesma distância")
```
O que você aprende aqui:
- variáveis
- entrada de dados
- cálculo com inteiros
- abs()
- condicionais

## 16. Diferença temporal (conceito importante)

Se usar:

```python
from datetime import datetime
ano_atual = datetime.now().year
```
Interpretação:
- positivo → futuro
- negativo → passado

## 17. Boas práticas (PEP 8)
Use nomes claros:
```python
idade_usuario = 20
```
Use snake_case:
```python
ano_destino
```
Não use palavras reservadas:
```python
# errado
if = 10
```
Cuidado com maiúsculas:
```python
var != Var
```
Underscore:
```python
_variavel
```
## 18. O que você PRECISA dominar

Se isso cair na prova, vão cobrar:

- variável = referência
- mutável vs imutável
- comportamento de listas
- id()
- is vs ==
- cópia de objetos

## 19. Pegadinha clássica
```python
a = [1,2]
b = a

b.append(3)

print(a)
```
Resposta:

```
[1,2,3]
```
👉 Porque é o mesmo objeto

---

## 1. O que são funções em Python (a ideia central)

Uma função é um bloco de código que você escreve uma vez e pode reutilizar várias vezes.

Pense assim:

- Sem função → você repete código várias vezes
- Com função → você escreve uma vez e reaproveita

Isso resolve dois problemas importantes:

1. organização
2. repetição de código (evita erro e bagunça)

Estrutura básica:
```python
def nome_da_funcao(parametros):
    # código
    return resultado
```

Partes importantes:

- **def** → define a função
- **nome_da_funcao** → nome que você escolhe
- **parametros** → entradas da função
- **return** → saída da função

## 2. Como a função funciona na prática

Quando você define, ela NÃO executa.

Ela só executa quando você chama:

```python
def saudacao(nome):
    return f"Olá, {nome}"

print(saudacao("João"))
```

Fluxo:

1. Programa encontra a chamada
2. "entra" na função
3. executa o código
4. retorna o resultado

## 3. Exemplo explicado: número romano

Esse é um exemplo clássico de algoritmo dentro de função.

```python
def inteiro_para_romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""
    for valor, numeral in valores:
        while numero >= valor:
            romano += numeral
            numero -= valor
    return romano
```

O que está acontecendo aqui?
- Existe uma lista de pares: número → símbolo romano
- O `for` percorre essa lista
- O `while` repete enquanto o número ainda pode usar aquele valor

Exemplo:

- número = 23
- pega 10 → X → sobra 13
- pega 10 → X → sobra 3
- pega 1 → I → sobra 2
- pega 1 → I → sobra 1
- pega 1 → I → sobra 0

Resultado: **XXIII**

## 4. Por que usar funções é importante

Sem função:

```python
# código repetido várias vezes
```

Com função:

```python
def calcular():
    ...
```

Benefícios:

- reutilização
- manutenção mais fácil
- código mais limpo
- menos erros

## 5. Parâmetros vs Argumentos (isso cai muito em prova)

**Parâmetro**

É o que aparece na definição:

```python
def soma(a, b):
```

**Argumento**

É o valor que você passa:

```python
soma(2, 3)
```

Tipos de uso:

1. Por posição: `soma(2, 3)`
2. Por nome: `soma(a=2, b=3)` (Mais claro e seguro.)

Parâmetro com valor padrão:
```python
def saudacao(nome="Visitante"):
    return f"Olá, {nome}"
```

## 6. Return (retorno) — MUITO importante

A função não imprime, ela retorna.

```python
def soma(a, b):
    return a + b
```

Você pode usar assim:

```python
resultado = soma(2, 3)
```

Ou direto:

```python
print(soma(2, 3))
```

Sem return:
```python
def teste():
    pass
```

Retorna: **None**

Retorno múltiplo:
```python
def valores():
    return 1, 2, 3
```

Isso vira uma tupla.

## 7. Exemplo completo: década + século

```python
ano_destino = int(input("Insira o ano de destino: "))

decada = (ano_destino // 10) * 10
seculo = inteiro_para_romano((ano_destino - 1) // 100 + 1)

print(f"O ano {ano_destino} pertence à década de {decada} e ao século {seculo}.")
```

Explicação:

**Década:**
`(ano // 10) * 10`

Ex: 1995 → 199 → 1990

**Século:**
`(ano - 1) // 100 + 1`

Por quê?
- Século 1: anos 1–100
- Século 2: anos 101–200

Ex:
- 2000 → século 20
- 2001 → século 21

## 8. Escopo de variáveis (isso causa MUITO erro)

**Variável local:**
```python
def teste():
    x = 10
```
Só existe dentro da função.

**Variável global:**
```python
x = 10
```
Existe no programa todo.

Problema:
Usar global demais → código confuso e difícil de manter

Evite isso:
`global x`

Use apenas quando necessário.

## 9. Boas práticas (importante pra prova e vida real)

1. Nome claro: `def calcular_media():` (NÃO: `def f():`)
2. Função faz UMA coisa só:
   - Errado: `def tudo():`
   - Certo: `def calcular_media():` e `def imprimir_resultado():`
3. Use docstring:
   ```python
   def soma(a, b):
       """Retorna a soma de dois números"""
   ```
4. Evite variáveis globais
5. Trate erros (Ex: `try...except`)

## 10. Eficiência das funções

Funções ajudam porque:

- evitam repetição
- reduzem uso de memória
- organizam lógica
- facilitam manutenção

Cuidado com **recursão** (Função chamando ela mesma):

```python
def f():
    f()
```

Se não tiver controle → trava o programa

## Conclusão (visão geral)

Funções são um dos pilares da programação porque:

- organizam o código
- tornam programas reutilizáveis
- facilitam manutenção
- reduzem erros
- melhoram desempenho lógico

---

## 1. Visão geral: o que esse tema quer te ensinar

Até agora você já sabe:

- criar função (`def`)
- usar `return`

Agora a pergunta é:

Como os dados entram na função, são processados e voltam?

Isso envolve 3 coisas:

1. Parâmetros (entrada)
2. Processamento (dentro da função)
3. Retorno (saída)

## 2. Passagem de parâmetros (entrada da função)

Quando você chama uma função, você pode enviar valores para ela:

```python
def soma(a, b):
    return a + b

soma(2, 3)
```

Aqui:

- **a** e **b** → parâmetros
- **2** e **3** → argumentos

Por que isso é importante?

Sem parâmetros:
```python
def soma():
    return 2 + 3
```
Função inútil → sempre retorna o mesmo valor

Com parâmetros:
```python
def soma(a, b):
    return a + b
```
Agora ela funciona para qualquer entrada → flexível e reutilizável

## 3. Assinatura da função (o "contrato")

A assinatura é a linha:
```python
def soma(a, b):
```

Isso define:
- nome da função
- quantos parâmetros ela recebe
- quais tipos de dados são esperados (implicitamente)

Por que chamamos de "contrato"?

Porque quem usa a função precisa respeitar isso:
- `soma(2, 3)` # correto
- `soma(2)` # erro

Parâmetros bem definidos:

- **Errado:** `def f(x, y):`
- **Certo:** `def calcular_media(nota1, nota2):`

Nome claro = código fácil de entender

## 4. Parâmetros opcionais (muito importante)

Você pode definir valores padrão:

```python
def saudacao(nome="Visitante"):
    return f"Olá, {nome}"
```

Uso:
- `saudacao()` # usa padrão
- `saudacao("João")` # usa argumento

Parâmetros por nome (melhora leitura):
`soma(a=2, b=3)`

Melhor que:
`soma(2, 3)`

Principalmente em funções grandes.

## 5. Como Python passa parâmetros (ponto MUITO importante)

Aqui está um dos conceitos mais cobrados e mais confundidos.

Python trabalha com referências.

### 5.1 Objetos imutáveis
Ex: `int`, `str`, `tuple`

```python
def teste(x):
    x = 10

a = 5
teste(a)
print(a)  # continua 5
```

Por quê?
- Python cria novo objeto
- não altera o original

### 5.2 Objetos mutáveis
Ex: `list`, `dict`

```python
def adicionar(lista):
    lista.append(10)

minha_lista = [1, 2]
adicionar(minha_lista)

print(minha_lista)  # [1, 2, 10]
```

Aqui:
- a função altera o MESMO objeto
- efeito colateral acontece

**Conclusão dessa parte:**
- Imutável → seguro
- Mutável → cuidado (pode alterar fora da função)

## 6. Return (saída da função)

O `return` é o que faz a função entregar um resultado

```python
def soma(a, b):
    return a + b
```

Como usar o retorno:
1. Guardar em variável: `resultado = soma(2, 3)`
2. Usar direto: `print(soma(2, 3))`

Função sem `return`:
```python
def teste():
    print("oi")
```
Retorna: **None**

Retornando múltiplos valores:
```python
def valores():
    return 1, 2, 3
```
Python transforma em: `(1, 2, 3)`

## 7. Personalização de funções

Aqui entra a ideia de deixar funções mais flexíveis.

Exemplo ruim:
```python
def mensagem():
    print("Olá João")
```

Exemplo bom:
```python
def mensagem(nome):
    print(f"Olá {nome}")
```

Parâmetros padrão ajudam muito:
`def mensagem(nome="Visitante"):`

## 8. Funções aninhadas (nested functions)

Você pode criar funções dentro de funções:

```python
def externa():
    def interna():
        print("Oi")
    interna()
```

Por que usar isso?
- esconder funções auxiliares
- organizar melhor o código
- evitar poluição global

### Escopo LEGB (muito importante)

Python procura variáveis nesta ordem:
1. **L**ocal (dentro da função)
2. **E**nclosing (função externa)
3. **G**lobal
4. **B**uilt-in

Palavra-chave `nonlocal`:
Permite alterar variável da função externa:

```python
def externa():
    x = 10

    def interna():
        nonlocal x
        x = 20
```

## 9. Modularidade (ideia mais importante do slide)

Modularizar = dividir o código em partes menores

- **Exemplo ruim:** tudo em um bloco gigante
- **Exemplo bom:**
  ```python
  def entrada():
  def processamento():
  def saida():
  ```

Benefícios:
- código organizado
- fácil manutenção
- fácil teste
- reutilização

## 10. Fluxo de dados entre funções

Funções podem se conectar:

```python
def dobrar(x):
    return x * 2

def somar(y):
    return y + 10

resultado = somar(dobrar(5))
```

Fluxo:
1. `dobrar(5)` → 10
2. `somar(10)` → 20

### Sem variáveis globais

Isso é MUITO importante:
- **Errado:** `x global`
- **Certo:** passar valores entre funções

## 11. Uso de estruturas para passar dados

Você pode passar:
- **Lista:** `def processar(lista):`
- **Dicionário:** `def processar(dados):`

Isso permite múltiplos valores.

## 12. Conclusão geral (ligando tudo)

Esse slide ensina que:
- Funções não são só blocos de código
- Elas são sistemas de entrada → processamento → saída

Você precisa dominar:
- Como dados entram (parâmetros)
- Como são manipulados (imutável vs mutável)
- Como saem (`return`)
- Como funções se conectam (fluxo)
- Como organizar tudo (modularidade)
