# 1. O que são portas lógicas

As **portas lógicas** são dispositivos eletrônicos que:

- recebem **entradas binárias (0 e 1)**
- aplicam uma **regra lógica**
- produzem **uma saída (0 ou 1)**

---

## Conceito-chave (importante para prova)

- **0 → baixa tensão (ex: 0V)**
- **1 → alta tensão (ex: 3.3V ou 5V)**

👉 Ou seja:

> Computadores funcionam com eletricidade interpretada como lógica.

---

## Por que isso é importante?

Tudo em computação é construído com portas lógicas:

- somadores (cálculos)
- memória (registradores)
- CPU
- sistemas operacionais (indiretamente)

---

# 2. Álgebra Booleana (base teórica)

A álgebra booleana foi criada por George Boole.

Ela define como trabalhar com valores:

- verdadeiro (1)
- falso (0)

---

## 2.1 Operações básicas

As três operações fundamentais são:

---

### AND (E)

Y=A⋅BY = A \cdot BY=A⋅B

- Só dá 1 se **todas as entradas forem 1**

---

### OR (OU)

Y=A+BY = A + BY=A+B

- Dá 1 se **pelo menos uma entrada for 1**

---

### NOT (NÃO)

Y=A‾Y = \overline{A}Y=A

- Inverte o valor

---

## 2.2 Leis importantes (cai em prova)

- Comutativa → A + B = B + A
- Associativa → (A + B) + C = A + (B + C)
- Distributiva → A(B + C) = AB + AC

### Teoremas de De Morgan:

- ¬(A · B) = ¬A + ¬B
- ¬(A + B) = ¬A · ¬B

👉 Muito usado para simplificação de circuitos.

---

# 3. Porta lógica NOT (Inversora)

## Funcionamento

- 1 entrada
- 1 saída
- sempre inverte

|A|Y|
|---|---|
|0|1|
|1|0|

---

## Aplicações

- inversão de sinal
- alarmes (detectar ausência)
- base para circuitos mais complexos

---

# 4. Porta lógica AND

## Funcionamento

- saída = 1 somente se todas entradas forem 1

|A|B|Y|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

---

## Interpretação prática

> “Tudo precisa estar verdadeiro”

Exemplo:

- login só funciona se usuário E senha estiverem corretos

---

# 5. Porta lógica OR

## Funcionamento

- saída = 1 se pelo menos uma entrada for 1

|A|B|Y|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

---

## Interpretação prática

> “Basta uma condição”

Exemplo:

- alarme dispara se QUALQUER sensor detectar movimento

---

# 6. Porta lógica XOR (OU exclusivo)

## Funcionamento

- saída = 1 quando as entradas são diferentes

Y=A⊕BY = A \oplus BY=A⊕B

|A|B|Y|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

---

## Interpretação

> “Ou um ou outro, mas não os dois”

---

## Aplicações

- somadores binários
- criptografia
- verificação de erros (paridade)

---

# 7. Implementação física

As portas lógicas já foram feitas com:

- relés (eletromecânicos)
- válvulas a vácuo
- hoje: **transistores (circuitos integrados)**

👉 Importante:

> Um processador moderno tem bilhões de transistores formando portas lógicas.

---

# 8. Circuitos digitais

## 8.1 Circuitos combinacionais

Características:

- não possuem memória
- saída depende apenas da entrada atual

Exemplos:

- somadores
- multiplexadores
- decodificadores

---

## 8.2 Circuitos sequenciais

Características:

- possuem memória
- dependem do estado anterior

Elementos usados:

- flip-flops
- latches

---

## Diferença essencial (cai muito em prova)

- Combinacional → sem memória
- Sequencial → com memória

---

# 9. Conexão com a CPU

Tudo que você viu antes sobre CPU depende disso:

- ULA → construída com portas lógicas
- registradores → usam flip-flops
- controle → lógica digital

👉 Ou seja:

> A CPU é basicamente um conjunto gigantesco de portas lógicas organizadas.

---

# 10. Resumo para prova

### Portas básicas:

- AND → tudo 1
- OR → pelo menos 1
- NOT → inverte
- XOR → diferentes

### Conceitos:

- binário → 0 e 1
- álgebra booleana → base matemática
- transistores → implementação física

### Circuitos:

- combinacionais → sem memória
- sequenciais → com memória

---

# Entendendo o CLOCK

## 1. Ideia central: o que é o clock

O **clock** é um sinal elétrico que:

- oscila entre 0 e 1 continuamente
- em intervalos regulares
- coordenando todas as operações do sistema

---

## Como entender de forma simples

Pense no clock como:

> um “metrônomo” ou “batida” que dita o ritmo do computador

Sem ele:

- cada componente funcionaria em tempos diferentes
- haveria caos no processamento

---

# 2. O papel do clock no sistema

O clock serve para **sincronizar tudo**:

- CPU
- memória
- barramentos
- dispositivos

---

## Analogia importante (cai em prova)

> O clock é como um maestro de uma orquestra

Cada componente só executa ações no momento certo, definido pelo clock.

---

# 3. Frequência do clock (Hertz)

A frequência indica quantos ciclos acontecem por segundo.

f=ciclos por segundo

---

## Exemplos

- 1 Hz → 1 ciclo por segundo
- 1 MHz → 1 milhão de ciclos por segundo
- 1 GHz → 1 bilhão de ciclos por segundo

---

## Exemplo prático

Um processador de 3 GHz:

- executa **3 bilhões de ciclos por segundo**

---

# 4. O que é um ciclo de clock

Um **ciclo de clock** é uma oscilação completa do sinal:

- vai de 0 → 1 → 0

---

## Estrutura do ciclo

### Nível alto (1)

- sinal elétrico alto
- certas operações acontecem aqui

### Nível baixo (0)

- sinal baixo
- outras operações podem ocorrer

---

## Transições importantes

- **borda de subida** → 0 → 1
- **borda de descida** → 1 → 0

👉 Muitas operações acontecem exatamente nessas bordas

---

# 5. Frequência x Período (muito importante)

Existe uma relação matemática fundamental:

T = 1 / f1

---

## O que isso significa

- T = tempo de um ciclo (período)
- f = frequência

---

## Exemplo

- 1 GHz → período = 1 ns
- 4 GHz → período = 0,25 ns

👉 Quanto maior a frequência:

- menor o tempo de cada ciclo
- mais rápido o processamento

---

# 6. Como o clock é gerado

O clock é gerado por um componente chamado:

## Oscilador

Geralmente baseado em:

- cristal de quartzo

---

## Como funciona

1. o cristal vibra com energia elétrica
2. gera pulsos estáveis
3. esses pulsos viram o clock

---

## Depois disso

- o sinal é distribuído por todo o sistema
- todos os componentes usam esse mesmo ritmo

---

# 7. Clock e o funcionamento da CPU

O clock controla o ciclo de execução da CPU.

Lembra do ciclo?

- Fetch (buscar)
- Decode (decodificar)
- Execute (executar)
- Store (armazenar)

---

## Como o clock entra nisso

Cada etapa acontece em **ciclos de clock**

Exemplo:

- ciclo 1 → buscar instrução
- ciclo 2 → decodificar
- ciclo 3 → executar
- ciclo 4 → armazenar

---

👉 Importante:

> Algumas instruções podem levar vários ciclos

---

# 8. Clock e desempenho

A ideia intuitiva é:

> maior clock = mais rápido

Mas isso NÃO é totalmente verdade.

---

## O desempenho depende de vários fatores:

- frequência do clock
- arquitetura (CISC/RISC)
- número de núcleos
- memória cache
- eficiência do software

---

## Conclusão importante (cai em prova)

> Clock alto ajuda, mas não garante melhor desempenho

---

# 9. Overclocking

## O que é

Aumentar o clock além do padrão do fabricante.

---

## Objetivo

- aumentar desempenho

---

## Problemas

- gera mais calor
- pode causar instabilidade
- reduz vida útil
- pode invalidar garantia

---

## Requisitos

- boa refrigeração (cooler, water cooling)

---

# 10. Resumo final (para prova)

### Clock:

- sinal que sincroniza o sistema

### Frequência:

- ciclos por segundo (Hz)

### Período:

- tempo de um ciclo
- relação: T = 1/f

### Ciclo:

- alternância entre 0 e 1

### Importante:

- nem tudo depende só do clock
- arquitetura também influencia

---

# 11. Ligação com o que você já viu

- portas lógicas → executam operações
- CPU → organiza essas operações
- clock → diz **quando** cada operação acontece

---

# 1. O que é a Arquitetura de Von Neumann

A **Arquitetura de Von Neumann** foi proposta por John von Neumann em 1945.

Ela define **como um computador é organizado internamente**.

---

## Ideia principal (muito importante)

> Dados e programas ficam na mesma memória

Isso é chamado de:

### **conceito de programa armazenado**

Antes disso:

- máquinas eram “fixas”
- não eram facilmente programáveis

Depois disso:

- você pode mudar o software sem mudar o hardware

---

# 2. Os 4 componentes principais

A arquitetura é formada por quatro blocos fundamentais:

---

## 2.1 Memória Principal

Função:

- armazenar **dados e instruções**

Características importantes:

- armazenamento binário (0 e 1)
- organizada em **endereços**
- acesso aleatório (RAM)

---

## Ideia importante para prova

> A mesma memória guarda dados E programas

---

## 2.2 CPU (Processador)

A CPU tem duas partes principais:

### Unidade de Controle (UC)

- controla tudo
- busca e decodifica instruções

### Unidade Lógica e Aritmética (ULA)

- faz cálculos
- executa operações lógicas

---

## 2.3 Entrada e Saída (I/O)

Permite comunicação com o mundo externo:

- teclado
- mouse
- monitor
- impressora

---

## 2.4 Barramentos (interconexão)

São os “caminhos” por onde os dados trafegam.

Tipos:

- barramento de dados
- barramento de endereços
- barramento de controle

---

# 3. Como tudo funciona junto

O funcionamento segue um ciclo:

---

## Ciclo de instrução (importantíssimo)

1. Fetch (buscar)
2. Decode (decodificar)
3. Execute (executar)
4. Store (armazenar)

---

## Explicando de forma simples

- CPU busca instrução na memória
- entende o que fazer
- executa
- guarda o resultado

E repete isso continuamente.

---

# 4. Memória na arquitetura de Von Neumann

## Estrutura unificada

- uma única memória
- armazena tudo

---

## Células de memória

- organizadas por endereços
- cada célula guarda bits

---

## Hierarquia moderna

Apesar do modelo original ser simples, hoje temos:

- registradores (mais rápidos)
- cache
- RAM
- armazenamento (HD/SSD)

---

# 5. Gargalo de Von Neumann (muito importante)

## O problema

A CPU usa o **mesmo barramento** para:

- buscar dados
- buscar instruções

---

## Consequência

> A CPU precisa esperar a memória

Isso limita o desempenho.

---

## Nome disso

**Gargalo de Von Neumann**

---

## Impacto

- CPU fica ociosa
- desempenho reduz

---

## Soluções modernas

- memória cache
- pipeline
- múltiplos núcleos
- barramentos mais rápidos

---

# 6. Comparação com Arquitetura Harvard

Aqui é um dos pontos mais cobrados.

---

## Von Neumann

- memória única
- barramento único
- mais simples
- mais flexível
- tem gargalo

---

## Harvard

- memória separada (dados e instruções)
- barramentos separados
- mais rápido
- mais complexo

---

## Ideia-chave

> Harvard permite acessar dados e instruções ao mesmo tempo

---

# 7. Onde cada arquitetura é usada

## Von Neumann

- computadores pessoais
- notebooks
- servidores

---

## Harvard

- microcontroladores
- sistemas embarcados
- DSPs (processamento de sinal)

---

## Mundo real (importante)

Hoje usamos **arquiteturas híbridas**:

- CPU estilo Von Neumann
- cache estilo Harvard

---

# 8. Importância histórica

A arquitetura de Von Neumann:

- tornou computadores programáveis
- permitiu criação de software
- transformou máquinas em sistemas universais

---

## Conceito mais importante de todos

> Programa armazenado = base da computação moderna

---

# 9. Conexão com o que você já estudou

- Portas lógicas → formam circuitos
- CPU → executa instruções
- Clock → sincroniza tudo
- Von Neumann → organiza todo o sistema

---

# 10. Resumo para prova

### Componentes:

- Memória
- CPU (UC + ULA)
- Entrada/Saída
- Barramentos

---

### Conceitos-chave:

- programa armazenado
- memória única
- ciclo de instrução
- gargalo de Von Neumann

---

### Diferença principal:

- Von Neumann → memória única
- Harvard → memória separada 

---

# 1. O que é um Sistema Operacional

Um **Sistema Operacional (SO)** é o software responsável por:

> gerenciar os recursos do computador e permitir que programas sejam executados

---

## Ideia mais importante (para prova)

> O SO é um **gerenciador de recursos**

---

## Quais recursos?

- CPU
- memória (RAM)
- armazenamento (HD/SSD)
- dispositivos de entrada/saída

---

## Outra forma de entender

O SO funciona como um “intermediário” entre:

- hardware (parte física)
- software (programas)

---

# 2. O papel do SO como alocador de recursos

O computador tem recursos limitados, mas vários programas querem usar ao mesmo tempo.

O SO precisa:

- decidir quem usa o quê
- quando usar
- por quanto tempo

---

## Exemplo simples

Você tem:

- 1 CPU
- vários programas abertos

O SO decide:

- qual programa vai usar a CPU agora
- qual vai esperar

---

# 3. Recursos gerenciados pelo SO

## 3.1 Tempo de CPU

- controla qual processo executa
- define por quanto tempo

Isso é chamado de:

> **escalonamento (scheduling)**

---

## 3.2 Memória

- aloca memória para programas
- libera quando não é mais usada

---

## 3.3 Armazenamento

- organiza arquivos no disco
- controla espaço livre

---

## 3.4 Dispositivos de I/O

- teclado
- mouse
- impressora
- disco

O SO controla o acesso a todos eles.

---

# 4. O problema da concorrência

## Situação

Vários programas querem usar o mesmo recurso ao mesmo tempo.

---

## Problema

- conflitos
- travamentos
- inconsistências

---

## Papel do SO

> resolver esses conflitos de forma transparente

---

## Exemplo

Dois programas querem imprimir ao mesmo tempo:

- o SO organiza a fila de impressão

---

# 5. Critérios de alocação (importante para prova)

O SO tenta equilibrar:

---

## Eficiência

- usar bem os recursos

## Justiça

- distribuir recursos de forma equilibrada

## Previsibilidade

- comportamento consistente

## Desempenho

- resposta rápida e bom rendimento

---

# 6. Tipos de sistemas operacionais

## Desktop

- uso pessoal
- multitarefa
- interface gráfica

---

## Servidor

- alta estabilidade
- muitos usuários simultâneos

---

## Móvel

- baixo consumo de energia
- otimizado para toque

---

# 7. Gerenciamento de processos

## O que é um processo?

> Um programa em execução

---

## Etapas principais

### 1. Criação

- processo é iniciado

### 2. Escalonamento

- SO decide quem usa a CPU

### 3. Sincronização

- coordena processos que compartilham recursos

### 4. Finalização

- processo termina
- recursos são liberados

---

# 8. Gerenciamento de memória

## 8.1 Memória virtual

- usa o disco como extensão da RAM
- permite rodar mais programas

---

## 8.2 Paginação

- divide memória em blocos fixos (páginas)

---

## 8.3 Segmentação

- divide memória de forma lógica (programa)

---

## 8.4 Memória física

- RAM real disponível

---

# 9. Sistema de arquivos

Responsável por organizar dados no disco.

---

## Funções

- nomear arquivos
- organizar diretórios
- controlar permissões
- gerenciar espaço

---

## Importante

> O usuário não acessa o disco diretamente — usa o sistema de arquivos

---

# 10. Gerenciamento de I/O

O SO controla dispositivos usando:

## Drivers

- programas que fazem comunicação com hardware

---

## Ideia-chave

> O driver traduz comandos do sistema para o dispositivo

---

# 11. Segurança e proteção

## Modos de operação

### Modo usuário

- acesso limitado
- roda aplicações

### Modo kernel

- acesso total ao sistema
- executa funções críticas

---

## Mecanismos de proteção

- isolamento de memória
- controle de acesso
- permissões

---

## Objetivo

> impedir que um programa afete outro ou o sistema

---

# 12. Desafios atuais

## Multicore

- usar vários núcleos ao mesmo tempo

## Virtualização

- rodar vários sistemas no mesmo hardware

## Eficiência energética

- reduzir consumo

## Segurança

- proteger contra ataques modernos

---

# 13. Resumo para prova

### Sistema Operacional é:

- gerenciador de recursos

---

### Gerencia:

- CPU
- memória
- arquivos
- dispositivos

---

### Conceitos importantes:

- processo
- escalonamento
- memória virtual
- drivers
- modo kernel vs usuário

---

### Função principal:

> garantir uso eficiente, justo e seguro do sistema