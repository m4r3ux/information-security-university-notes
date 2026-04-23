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