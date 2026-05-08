# Gerenciamento de Memória — Infraestrutura Computacional

Essa parte da disciplina entra em um dos temas mais importantes de Sistemas Operacionais: como o computador organiza, distribui e controla a memória enquanto vários programas executam ao mesmo tempo.

Sem gerenciamento de memória, o sistema operacional não conseguiria:

- executar múltiplos programas simultaneamente;
- proteger processos uns dos outros;
- evitar desperdício de memória;
- executar aplicações maiores que a RAM disponível;
- garantir desempenho adequado.

O slide apresenta desde os conceitos básicos de memória até técnicas modernas como memória virtual e paginação por demanda.

## O que é memória em um computador?

A memória é o local onde:

- programas ficam armazenados enquanto executam;
- dados são carregados para processamento;
- instruções são buscadas pela CPU.

O slide define a memória como:

> “um grande array de bytes, cada um com seu próprio endereço”.

Isso significa que:

- a memória é organizada em posições numeradas;
- cada posição possui um endereço único;
- a CPU acessa os dados usando esses endereços.

Exemplo simplificado:

| Endereço | Conteúdo |
| :--- | :--- |
| 1000 | instrução |
| 1001 | número |
| 1002 | caractere |

A CPU lê continuamente instruções da memória.

## Como a CPU usa a memória

O processador trabalha junto da memória o tempo inteiro.

O slide menciona:
- contador de programa;
- carga de dados;
- armazenamento de dados.

### Contador de programa (Program Counter)

O contador de programa guarda:
**o endereço da próxima instrução que será executada.**

Fluxo simplificado:
1. CPU lê instrução da memória;
2. executa a instrução;
3. atualiza o contador;
4. busca próxima instrução.

Exemplo:
- **Memória:**
  - 100 -> SOMAR
  - 101 -> SUBTRAIR
  - 102 -> IMPRIMIR

Se o contador está em 100:
- a CPU executa SOMAR;
- depois vai para 101.

### Leitura e escrita na memória

As instruções podem:
- ler dados;
- gravar dados;
- modificar valores.

Exemplo:
```python
x = 10
x = x + 5
```

O processador:
1. lê o valor 10 da memória;
2. soma 5;
3. grava 15 novamente.

## Hardware básico

O slide explica algo extremamente importante:

A CPU só acessa diretamente:
- registradores;
- memória principal (RAM).

Ela **NÃO** acessa o disco diretamente.

### Registradores

Registradores são pequenas áreas internas da CPU.

Características:
- extremamente rápidos;
- armazenam dados temporários;
- usados durante cálculos.

São muito mais rápidos que RAM.

### RAM (Memória principal)

A RAM:
- armazena programas em execução;
- guarda dados temporários;
- é mais lenta que registradores;
- é muito mais rápida que disco.

### Disco rígido / SSD

O armazenamento secundário:
- guarda dados permanentemente;
- é mais lento;
- possui maior capacidade.

O processador não conversa diretamente com ele. O sistema operacional precisa copiar dados do disco para RAM; só depois a CPU consegue usar.

## Por que gerenciamento de memória é necessário?

Imagine: navegador, jogo, editor, antivírus e sistema operacional, todos executando simultaneamente.

O sistema operacional precisa:
- dividir memória;
- proteger processos;
- evitar conflitos;
- otimizar desempenho.

É exatamente isso que o gerenciamento de memória faz.

## Memória Virtual

Esse é um dos conceitos mais importantes do slide.

**O que é memória virtual?**
Memória virtual é uma técnica que:
- combina RAM + disco;
- cria a ilusão de memória maior.

Mesmo que o computador tenha 8 GB de RAM, um programa pode acreditar que possui muito mais espaço.

### Ideia central da memória virtual

O programa **NÃO** trabalha diretamente com endereços físicos da RAM. Ele usa **endereços virtuais**. O sistema operacional converte:
**Endereço virtual -> endereço físico**

### Vantagem disso

- **Sem memória virtual:** programas ficariam limitados ao tamanho da RAM.
- **Com memória virtual:** partes do programa podem ficar temporariamente no disco; apenas o necessário fica na RAM.

Exemplo simples:
Imagine um programa enorme de 20 GB em um computador com 8 GB RAM.
- **Sem memória virtual:** impossível executar.
- **Com memória virtual:** somente partes necessárias são carregadas; o restante fica no disco.

### Transparência para o programador

O slide compara memória virtual a vetores. Quando você usa `lista[500]`, você não sabe onde fisicamente o dado está. O sistema operacional resolve isso automaticamente.

### História da memória virtual

O slide menciona:
- Atlas (1960);
- IBM System/370 (1972).

Isso mostra que memória virtual foi revolucionária porque permitiu multiprogramação eficiente, programas maiores e melhor uso do hardware. Hoje praticamente todos os sistemas usam memória virtual.

## Swapping

Outro conceito fundamental.

**O que é swapping?**
Swapping é mover processos entre RAM e disco temporariamente.

Fluxo:
1. RAM cheia
2. Processo vai para disco
3. Outro processo entra
4. Processo antigo pode voltar depois

### Objetivo do swapping
Permitir mais processos executando e melhor aproveitamento da memória.

### Memória de retaguarda
É o armazenamento secundário (HD, SSD). Quando falta RAM, processos menos usados podem ser removidos temporariamente.

### Problema do swapping
Disco é MUITO mais lento que RAM. Consequência: excesso de swapping deixa o sistema lento. Esse problema é chamado de **thrashing**, quando o sistema passa mais tempo movendo memória do que executando programas.

## Paginação por demanda

Agora entramos em como a memória virtual funciona internamente.

**O que é paginação?**
A memória é dividida em blocos chamados **páginas**.
Exemplo: Página 1, Página 2, Página 3.

### Paginação por demanda
A ideia é carregar apenas páginas necessárias. Em vez de carregar o programa inteiro, somente partes usadas entram na RAM.

### Vantagem
Economia enorme de memória.

Exemplo:
Imagine um editor de vídeo enorme. Talvez você esteja usando apenas o menu ou uma ferramenta. Então, somente essas partes são carregadas.

### Page Fault (Falta de página)

O slide destaca isso. Ocorre quando o programa tenta acessar uma página que **NÃO** está na RAM.

Fluxo:
1. Programa acessa página
2. Página não está na RAM
3. SO interrompe execução
4. Busca página no disco
5. Carrega para RAM
6. Programa continua

### Problema do page fault
Buscar do disco é lento. Muitos page faults reduzem o desempenho.

## Organização da memória

O slide apresenta a hierarquia da memória.

### Hierarquia da memória

1. **Cache:** Mais rápida, pequena, cara e próxima da CPU. Guarda dados acessados frequentemente.
2. **RAM:** Intermediária, maior e mais lenta que cache.
3. **Disco:** Mais lento, enorme capacidade e barato.

**Ideia da hierarquia:**
- Quanto mais rápido, menor e mais caro.
- Quanto mais lento, maior e mais barato.

### Papel da paginação
A paginação usa RAM e disco para mover páginas conforme necessidade.

## Padrões de acesso à memória

O sistema operacional tenta prever quais dados serão usados. O slide apresenta dois conceitos importantíssimos: **localidade espacial** e **localidade temporal**.

### Localidade espacial
Significa que se um dado foi acessado, os dados próximos provavelmente também serão.

Exemplo: `lista = [1,2,3,4,5]`
Ao acessar `lista[0]`, é provável que `lista[1]` e `lista[2]` também sejam usados.

**Por que isso importa?**
O sistema pode carregar blocos próximos juntos, o que reduz page faults.

### Localidade temporal
Significa que dados usados recentemente provavelmente serão usados novamente em breve.

Exemplo:
```python
for i in range(1000):
    soma += contador
```
A variável `contador` é usada repetidamente, então o sistema mantém ela próxima da CPU.

### Relação com cache
Caches funcionam principalmente graças à localidade espacial e temporal. Sem esses padrões, o desempenho seria muito pior.

## Relação entre todos os conceitos do slide

O slide inteiro constrói uma sequência lógica:

1. CPU precisa acessar memória, mas a RAM é limitada.
2. Surge a memória virtual: combina RAM + disco e cria ilusão de memória maior.
3. Surge swapping e paginação para mover dados dinamicamente.
4. Sistema usa padrões de acesso para prever o que carregar e o que remover.

## Conceitos mais importantes para prova

Você **PRECISA** saber:

- **Memória virtual:** Cria ilusão de memória maior usando RAM + disco.
- **Swapping:** Movimentação de processos entre RAM e disco.
- **Paginação por demanda:** Carregar apenas o necessário.
- **Page Fault:** Erro quando o dado não está na RAM.
- **Localidade:** Espacial e Temporal.

---

# Impacto dos padrões de acesso na paginação por demanda

Agora o slide começa a conectar dois assuntos fundamentais que vimos antes:
- paginação por demanda;
- padrões de acesso à memória.

Aqui a disciplina quer mostrar uma ideia MUITO importante: **o desempenho da memória virtual depende diretamente da forma como os programas acessam a memória.**

Ou seja, não basta existir memória virtual. O modo como o programa usa os dados influencia completamente:
- velocidade;
- quantidade de faltas de página;
- desempenho do sistema;
- uso de RAM;
- eficiência do cache.

## Revisando rapidamente: o que é paginação por demanda?

Paginação por demanda significa carregar para RAM apenas as páginas realmente necessárias.

Então:
- parte do programa fica em RAM;
- parte fica no disco.

Quando o programa precisa de uma página ausente:
1. ocorre **page fault**;
2. sistema operacional busca a página no disco;
3. a página entra na memória;
4. execução continua.

### O problema central
Disco é MUITO mais lento que RAM. Então, quanto mais page faults, pior o desempenho. E é exatamente aqui que entram os padrões de acesso.

**O que o slide quer mostrar?**
- Se o programa acessa memória de forma organizada: paginação funciona muito bem.
- Se acessa memória de forma caótica: o sistema sofre; ocorrem muitas faltas de página.

## Relação entre localidade e desempenho

O slide fala sobre:
- localidade espacial;
- localidade temporal.

Esses conceitos são essenciais para entender cache, RAM, memória virtual e o desempenho de programas.

### Localidade espacial
Acontece quando o programa acessa posições próximas da memória.

Exemplo:
```python
lista = [10,20,30,40,50]

for numero in lista:
    print(numero)
```
O programa acessa `lista[0]`, `lista[1]`, `lista[2]`, `lista[3]`. Tudo próximo na memória.

**Por que isso ajuda?**
Quando o sistema carrega uma página, vários dados próximos entram juntos. Então, os próximos acessos provavelmente já estarão na RAM.
**Resultado:** menos page faults e execução mais rápida.

### Localidade temporal
Acontece quando o mesmo dado é reutilizado várias vezes em um curto período.

Exemplo:
```python
contador = 0

for i in range(10000):
    contador += 1
```
A variável `contador` é acessada constantemente, então o sistema mantém ela no cache, na RAM e perto da CPU.

## Quando a paginação funciona muito bem
O slide diz:
> “Se um processo exibe alta localidade espacial ou temporal, a paginação funciona muito bem.”

Porque:
- poucas páginas precisam ser carregadas;
- páginas antigas continuam úteis;
- o sistema evita acesso ao disco.

## Quando o desempenho fica ruim
Agora vem o cenário problemático: **baixa localidade**.

Isso significa:
- acessos espalhados;
- acessos aleatórios;
- pouca repetição;
- dados muito distantes entre si.

### Exemplo de baixa localidade
Imagine acessar: `dados[5]`, `dados[900000]`, `dados[13]`, `dados[700000]`.
O sistema precisa carregar páginas diferentes constantemente.
**Consequência:** muitos page faults, muita leitura do disco e lentidão.

## O que é latência?
Latência é o tempo de espera até o dado ficar disponível.
- Buscar dados da RAM → rápido;
- Buscar dados do disco → lento.

Então: **mais page faults = mais latência.**

## Exemplo do banco de dados
Imagine um sistema de banco de dados enorme com milhões de registros.

- **Cenário ruim:** Se as consultas acessam dados aleatoriamente em regiões distantes da memória, o sistema gera muitas faltas de página. O banco de dados responde lentamente e desperdiça desempenho.
- **Cenário bom:** Se os dados são acessados sequencialmente (registro 1, 2, 3, 4), a localidade espacial melhora. Poucas páginas bastam e o desempenho é maior.

## Estratégias para melhorar desempenho

### 1. Otimização do código
Programadores podem escrever programas que usem memória de forma organizada, reutilizem dados próximos e evitem acessos aleatórios.

**Exemplo: alocação contínua**
Se os dados de uma matriz ficam próximos, o acesso é mais eficiente.

**Fragmentação:** Ocorre quando a memória fica cheia de pequenos espaços separados, o que dificulta a alocação e a eficiência.

### 2. Algoritmos de alocação de memória
O sistema operacional precisa decidir quais páginas manter e quais remover.

- **FIFO (First In, First Out):** Remove a página mais antiga. Funciona como uma fila. Problema: a página removida pode ainda ser importante.
- **LRU (Least Recently Used):** Remove a página menos usada recentemente. Aproveita a localidade temporal, mantendo páginas usadas frequentemente na RAM.

## Gerenciamento de cache
Cache é uma memória extremamente rápida que guarda dados usados frequentemente.
**Objetivo:** Evitar o ciclo CPU -> RAM -> disco o tempo inteiro. Se páginas importantes ficam no cache, ocorrem menos page faults e o desempenho é muito maior.

## Permuta-padrão (Swapping tradicional)
Consiste em remover processos inteiros da RAM, enviar para o disco e trazê-los depois.

- **Fila de prontos:** O sistema mantém processos prontos para executar na RAM ou no disco.
- **Despachante:** Decide qual processo executa, qual sai e qual entra.

### Problema principal da permuta
Ela é MUITO lenta. O slide mostra um cálculo:
Processo de 100 MB em um disco de 50 MB/s:
`100 MB / 50 MB/s = 2 segundos`

Apenas mover o processo leva 2 segundos, o que é enorme. Isso torna a mudança de contexto lenta.

### Problema de I/O durante swapping
Se um processo P1 faz operação de disco e é removido da RAM antes dela terminar, o dispositivo pode tentar escrever numa memória que agora pertence a P2, causando corrupção de dados.

**Soluções:**
1. Não remover processos com I/O pendente.
2. Usar **buffers** do sistema operacional (**double buffering**), o que gera **overhead** (custo adicional de processamento e memória).

## Por que permuta-padrão não é mais usada?
Swapping completo é lento demais e desperdiça tempo. Sistemas modernos usam paginação e memória virtual inteligente.

## Permuta em sistemas móveis
Celulares (Android/iOS) evitam swapping devido ao espaço limitado, desgaste da memória flash e bateria. Em vez disso, eles encerram aplicativos e salvam seu estado para reabertura rápida.

## Proteção da memória
Assunto fundamental para garantir que processos não interfiram uns nos outros.
