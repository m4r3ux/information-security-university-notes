# Introdução à infraestrutura computacional

## 1. Ideia geral

O computador mudou muito com o tempo:

- Antes: servia basicamente para calcular
- Hoje: ajuda a criar, automatizar e pensar

Ou seja:  
ele não só executa tarefas, ele também ajuda o ser humano a ser mais produtivo e criativo.

---

## 2. Automatização e foco criativo

### O que é automatização?

É quando o computador faz tarefas sozinho.

Exemplos:

- organizar dados
- gerar relatórios
- repetir cálculos

### O que isso muda?

- você deixa de gastar energia com tarefas repetitivas
- sobra mais tempo para pensar

👉 Resultado: você foca no que exige inteligência humana (decisão, criação, análise)

---

## 3. Design gráfico

### Antes:

- papel e lápis
- apagar e refazer era difícil
- limitações físicas

### Agora:

- programas e realidade virtual
- criação rápida e editável
- sem limite físico real

👉 Resultado:  
o designer pode criar praticamente qualquer coisa que imaginar.

---

## 4. Música e Inteligência Artificial

A IA ajuda na criação de música.

Ela pode:

- sugerir melodias
- criar harmonias
- gerar sons novos

👉 Isso permite:

- mais criatividade
- novos estilos musicais
- mais pessoas conseguindo produzir música

---

## 5. Organização de computadores

Aqui o foco é:  
como o computador funciona por dentro.

Ele é formado por partes que trabalham juntas para:

- armazenar dados
- processar informações
- se comunicar com o usuário

---

## 6. Interação entre componentes

Pense assim:

- CPU = “cérebro” (processa tudo)
- Memória = “memória de trabalho” (guarda o que está sendo usado)
- E/S = “entrada e saída” (teclado, mouse, monitor)

👉 Como funciona:

- CPU pega dados na memória
- processa
- devolve resultado para o usuário via E/S

---

## 7. Armazenamento, transmissão e processamento

### Armazenamento

Guarda dados por tempo longo  
Ex: HD, SSD

### Transmissão

Leva dados de um lugar para outro  
Ex: barramentos, internet

### Processamento

CPU faz os cálculos e executa instruções

---

## 8. Estrutura interna do sistema

O computador funciona com peças principais:

- CPU
- RAM
- dispositivos de entrada e saída
- barramentos

👉 Tudo isso trabalha junto o tempo todo

---

## 9. Comunicação entre partes

- Barramento: comunicação dentro do computador
- Rede: comunicação entre computadores
- Interface: forma de conectar dispositivos

---

## 10. Manipulação de dados

Os dados passam por etapas:

1. Codificação: vira linguagem do computador (0 e 1)
2. Processamento: CPU trabalha nesses dados
3. Decodificação: volta para forma que o usuário entende

---

## 11. Barramentos (projeto)

São como “estradas de dados” dentro do computador.

Eles têm:

- largura (quantos dados passam de uma vez)
- velocidade (quão rápido passam)
- protocolo (regras de comunicação)

---

## 12. Hierarquia de memória

Memória não é toda igual:

- Registradores (mais rápido)
- Cache (rápido)
- RAM (intermediário)
- Disco (mais lento, mas grande)

👉 Quanto mais rápido, menor e mais caro

---

## 13. Interfaces de E/S

São formas de conectar dispositivos:

- USB: periféricos (mouse, teclado)
- HDMI: vídeo e áudio
- Ethernet: internet

---

## 14. Controle de dispositivos

Para tudo funcionar, existe:

- Drivers: fazem o sistema reconhecer o hardware
- Controladores: gerenciam dispositivos
- Firmware: “software interno” do hardware

---

## Resumo final

Infraestrutura computacional explica:

- como o computador funciona por dentro
- como os dados entram, saem e são processados
- como hardware e software trabalham juntos

---

# Arquitetura de computadores modernos: visão geral

A arquitetura de computadores modernos mostra que o computador funciona em **6 níveis diferentes**, do mais básico (hardware elétrico) até o mais alto (software especializado).

A ideia central é:  
cada nível depende do anterior e esconde sua complexidade.

---

# Nível 1: nível lógico digital

Aqui está a base de tudo.

- Computadores funcionam com **portas lógicas AND, OR e NOT**
- Essas portas são feitas de **transistores**
- Elas implementam **funções booleanas**

Depois disso, essas portas formam:

- **Circuitos digitais complexos**
    - somadores (fazem contas)
    - multiplexadores (escolhem dados)

E também:

- **Flip-flops**
    - criam memória e registradores
    - guardam informações temporárias

Resumo:  
é o nível elétrico/lógico que permite o computador “pensar” em 0 e 1.

---

# Nível 2: ISA (Arquitetura do Conjunto de Instruções)

Aqui está a “linguagem da CPU”.

- Define as instruções que a CPU executa diretamente (linguagem de máquina)
- Cada instrução faz uma ação (somar, mover dados etc.)

Também define:

- **Modos de endereçamento**
    - direto
    - indireto
    - indexado

Resumo:  
é a interface entre hardware e software, ou seja, o que o processador entende.

---

# Nível 3: Sistema operacional

Aqui o computador começa a “se organizar”.

Funções principais:

- **Gerenciamento de processos**
    - cria, gerencia e finaliza programas
    - controla CPU e memória
- **Gerenciamento de memória**
    - usa paginação e segmentação
- **Sistema de arquivos**
    - organiza arquivos e pastas no armazenamento

Resumo:  
é o “gerente” que controla todos os recursos do computador.

---

# Nível 4: Linguagem assembly

É uma forma intermediária entre máquina e humano.

- Usa **mnemônicos** (ex: MOV, ADD)
- Representa instruções de máquina de forma simplificada
- O **assembler** traduz assembly para código de máquina executável

	Resumo:  
é programação de baixo nível, com controle direto do hardware.

---

# Nível 5: Linguagens de alto nível

Aqui entram linguagens mais usadas na prática:

- C, Java, Python

Características:

- **Abstração**: esconde detalhes do hardware
- **Portabilidade**: funciona em diferentes sistemas
- **Produtividade**: facilita criar programas complexos
- **Compiladores**: traduzem para código de máquina ou bytecode

Também envolve:

- **type cast (conversão de tipo)**
    - quando converte um valor de um tipo para outro

Resumo:  
permite programar sem lidar diretamente com o hardware.

---

# Nível 6: linguagem orientada a problemas

É o nível mais especializado.

- Focado em problemas específicos:
    - simulação numérica
    - processamento de imagens

Exemplos:

- MATLAB
- R
- Python com bibliotecas

Características:

- alto nível de abstração
- foco no problema, não na máquina

Resumo:  
você resolve problemas complexos sem pensar na implementação interna.

---

# Interação entre os níveis

Os níveis funcionam juntos assim:

- **Abstração**: cada nível esconde o de baixo
- **Interface**: cada nível conversa com o de cima
- **Desempenho**: otimização em cada nível melhora o sistema

Resumo:  
os níveis trabalham como uma cadeia organizada.

---

# Virtualização

Permite rodar vários sistemas no mesmo computador.

- **Máquinas virtuais (VMs)**
    - vários sistemas operacionais em um hardware
- **Containers**
    - isolam processos
    - compartilham o mesmo kernel
    - são mais leves que VMs

---

# Computação em nuvem

Modelos de serviço:

- **IaaS**
    - infraestrutura (servidores, rede, armazenamento)
- **PaaS**
    - plataforma de desenvolvimento pronta
- **SaaS**
    - software pronto para uso

---

# Computação quântica

Tecnologia avançada baseada em:

- **Qubits**
    - podem ser 0, 1 ou ambos
- **Superposição**
- **Entrelaçamento quântico**

Objetivo:  
resolver problemas muito difíceis para computadores clássicos.

---

# Inteligência Artificial e Machine Learning

Baseado em:

- **Algoritmos**
    - identificam padrões e tomam decisões
- **Dados**
    - grandes volumes para treinamento

Aplicações:

- reconhecimento de imagem
- linguagem natural

---

# Desafios da arquitetura de computadores

Principais problemas:

- **Lei de Moore**
    - limite físico dos transistores
- **Consumo de energia**
    - mais calor e energia
- **Complexidade**
    - sistemas difíceis de projetar e manter

---

# Tendências futuras

- arquiteturas especializadas (IA e ML)
- computação neuromórfica (inspirada no cérebro)
- novos materiais (grafeno e nanotubos de carbono)

---

# Impacto da arquitetura de computadores

- **Economia**
    - inovação e crescimento
- **Sociedade**
    - muda como vivemos e trabalhamos
- **Ciência**
    - avanços em medicina, física e astronomia

---

# Arquiteturas CISC e RISC
# 1. Introdução: o que são CISC e RISC

As arquiteturas **CISC (Complex Instruction Set Computing)** e **RISC (Reduced Instruction Set Computing)** são dois modelos de projeto de CPU (Unidade Central de Processamento).

A diferença central entre elas está na filosofia de como o processador deve executar instruções:

- **CISC:** poucas instruções, mas muito complexas (fazem “muita coisa por vez”)
- **RISC:** muitas instruções simples (fazem “uma coisa por vez”)

Essa diferença impacta diretamente:

- desempenho
- consumo de energia
- complexidade do hardware
- tamanho do código
- papel do compilador

---

# 2. Arquitetura CISC (Complex Instruction Set Computing)

## 2.1 Conceito principal

A arquitetura CISC possui um **conjunto de instruções extenso e complexo**, onde cada instrução pode realizar várias operações ao mesmo tempo.

Exemplo conceitual:  
Uma única instrução pode:

- acessar memória
- fazer cálculo
- armazenar resultado

---

## 2.2 Densidade de código

Um ponto muito importante:

**CISC prioriza densidade de código.**

Isso significa:

- menos linhas de código em linguagem de máquina
- programas menores em tamanho

Isso acontece porque uma instrução “faz mais coisas”.

---

## 2.3 Compatibilidade retroativa

CISC geralmente mantém compatibilidade com versões antigas.

Isso significa:

- novos processadores ainda executam instruções antigas
- evita reescrever software legado

Isso é extremamente importante no mundo real, especialmente na linha x86.

---

## 2.4 Vantagens da CISC

- Alta densidade de código
- Compatibilidade retroativa
- Instruções poderosas (mais complexas)

---

## 2.5 Desvantagens da CISC

- Hardware mais complexo (difícil de projetar)
- Ciclos de clock variáveis (instruções demoram tempos diferentes)
- Muitas instruções raramente usadas (ineficiência interna)

---

## 2.6 Exemplos de CISC

### x86 (Intel/AMD)

- Arquitetura dominante em PCs
- Presente em desktops e notebooks
- Altamente compatível com software antigo

### Motorola 68000

- Muito usado em computadores clássicos (ex: Macintosh antigo)
- Também presente em sistemas embarcados e workstations

---

# 3. Arquitetura RISC (Reduced Instruction Set Computing)

## 3.1 Conceito principal

A arquitetura RISC usa um **conjunto reduzido de instruções simples**, onde cada instrução faz apenas uma operação básica.

Exemplo:

- carregar dado da memória
- somar dois valores
- armazenar resultado

Cada instrução faz uma coisa só.

---

## 3.2 Execução rápida

Como as instruções são simples:

- execução mais rápida
- ciclos de clock menores
- pipeline mais eficiente

---

## 3.3 Paralelismo

RISC facilita muito:

- execução paralela de instruções
- pipelines mais organizados
- maior throughput (mais instruções por segundo)

---

## 3.4 Vantagens da RISC

- Execução rápida e uniforme
- Hardware mais simples
- Menor consumo de energia

---

## 3.5 Desvantagens da RISC

- Menor densidade de código (código maior)
- Maior dependência do compilador
- Menor compatibilidade direta com instruções antigas

---

## 3.6 Exemplos de RISC

### ARM

- Dominante em smartphones e tablets
- Altamente eficiente energeticamente
- Crescendo também em servidores

### MIPS

- Muito usado em sistemas embarcados
- Roteadores e consoles
- Simplicidade de design

---

# 4. Comparação direta CISC vs RISC (essencial para prova)

|Característica|CISC|RISC|
|---|---|---|
|Instruções|Complexas e numerosas|Simples e poucas|
|Código|Pequeno (alta densidade)|Maior|
|Execução|Variável|Rápida e uniforme|
|Hardware|Complexo|Simples|
|Energia|Maior consumo|Menor consumo|

---

# 5. Papel do compilador (muito importante em RISC)

Em RISC, o hardware é simples, então o **compilador faz mais trabalho**.

Ele precisa:

- dividir operações complexas em várias instruções simples
- otimizar sequências de instruções
- organizar execução (instruction scheduling)
- eliminar código desnecessário (dead code elimination)
- expandir funções inline

👉 Ou seja:

> Em RISC, a inteligência está mais no software (compilador), não no hardware.

---

# 6. Arquiteturas híbridas (mundo real moderno)

Hoje não existe CISC ou RISC “puro” na prática.

Exemplo:

### x86-64

- Mantém compatibilidade CISC
- Internamente usa técnicas RISC-like

👉 Isso significa:

- o processador “recebe CISC”
- mas “executa como RISC internamente”

---

# 7. Consumo de energia

Esse ponto é MUITO cobrado:

- RISC → menor consumo → ideal para mobile
- CISC → maior consumo → tradicional em PCs

Técnicas usadas:

- clock gating (desliga partes do clock)
- voltage scaling (reduz tensão elétrica)

---

# 8. Futuro das arquiteturas

A tendência atual não é escolher um lado, mas evoluir para:

- processamento paralelo (multi-core)
- IA embarcada (NPUs)
- arquiteturas neuromórficas (inspiradas no cérebro)
- computação quântica (novo paradigma)

---

# 9. Resumo mental (para prova)

Se quiser decorar rápido:

- **CISC = instruções complexas, código pequeno, hardware pesado**
- **RISC = instruções simples, código maior, hardware leve**

---

# Unidade Central de Processamento
# 1. O que é a CPU (Unidade Central de Processamento)

A **CPU (Central Processing Unit)** é o principal componente de processamento de um computador.

Ela é responsável por:

- Interpretar instruções de programas
- Executar operações lógicas e matemáticas
- Controlar o fluxo de dados do sistema

👉 Em termos simples:

> A CPU é o “cérebro” do computador.

---

# 2. Unidades funcionais da CPU

A CPU é dividida em três partes principais:

---

## 2.1 Unidade de Controle (UC)

A **UC (Unidade de Controle)** é responsável por coordenar tudo.

Funções:

- Busca instruções na memória
- Decodifica instruções
- Controla o fluxo de dados entre CPU, memória e ULA
- Garante execução na ordem correta

👉 Analogamente:

> É o “maestro da orquestra”

---

## 2.2 Unidade Lógica e Aritmética (ULA)

A **ULA (ALU – Arithmetic Logic Unit)** executa operações.

Ela realiza:

### Operações aritméticas:

- soma
- subtração
- multiplicação
- divisão

### Operações lógicas:

- AND
- OR
- NOT

👉 Resumo:

> A ULA é onde o processamento “de fato acontece”.

---

## 2.3 Registradores

Os **registradores** são pequenas memórias extremamente rápidas dentro da CPU.

Função:

- armazenar dados temporários
- guardar endereços de memória
- manter valores em uso imediato

👉 Característica principal:

> São a memória mais rápida do computador.

---

# 3. Ciclo da CPU (Fetch-Decode-Execute-Store)

Esse ciclo é fundamental e MUITO cobrado em provas.

---

## 3.1 Fetch (Busca)

PC→Mem_Instru\xE7\xE3oPC \rightarrow Mem\_Instru\xE7\xE3oPC→Mem_Instru\xE7\xE3o

- A CPU busca a próxima instrução na memória
- Usa o **PC (Program Counter)** para saber onde buscar

---

## 3.2 Decode (Decodificação)

- A UC interpreta a instrução
- Identifica:
    - operação a ser feita
    - operandos (dados envolvidos)

---

## 3.3 Execute (Execução)

- A ULA executa a operação
- Pode envolver cálculos ou operações lógicas

---

## 3.4 Store (Armazenamento)

- Resultado é armazenado em:
    - registrador
    - ou memória RAM

---

👉 Resumo do ciclo:

> Buscar → Decodificar → Executar → Armazenar

---

# 4. Clock da CPU (Clock Speed)

O **clock speed** é a frequência de operação da CPU.

f=1Tf = \frac{1}{T}f=T1​

TTT

Tf = 0.5 Hz

Onde:

- f = frequência (clock)
- T = tempo de um ciclo

---

## O que isso significa?

- Medido em **Hertz (Hz)**
- Indica quantos ciclos por segundo a CPU executa

Exemplo:

- 3 GHz = 3 bilhões de ciclos por segundo

---

## Importante (cai em prova):

Clock alto NÃO significa sempre melhor desempenho.

Porque desempenho também depende de:

- arquitetura (CISC/RISC)
- número de núcleos
- cache
- eficiência do software

---

# 5. Memória Cache

A cache é uma memória intermediária entre CPU e RAM.

Ela existe porque:

> RAM é lenta comparada à CPU

---

## 5.1 Níveis de cache

### L1 Cache

- mais rápida
- menor capacidade
- dentro do núcleo da CPU

### L2 Cache

- intermediária
- mais espaço que L1

### L3 Cache

- maior cache
- mais lenta que L1 e L2
- compartilhada entre núcleos

---

## Ideia central:

> Quanto mais perto da CPU, mais rápida e menor a memória.

---

# 6. Multiprocessamento e Multicore

## Multiprocessamento

- vários processadores físicos

## Multicore

- um processador com vários núcleos

---

## Resultado:

- execução paralela
- maior desempenho
- melhor multitarefa

---

👉 Diferença importante de prova:

- Multiprocessamento = vários CPUs físicos
- Multicore = um CPU com vários núcleos

---

# 7. CPU e Memória RAM

A CPU depende da RAM para funcionar.

Fluxo:

- CPU busca instruções na RAM
- RAM fornece dados e programas

---

## Problema:

- RAM é mais lenta que CPU

## Solução:

- cache (L1, L2, L3)

---

👉 Conclusão:

> Desempenho da CPU depende muito da RAM.

---

# 8. Sistema Operacional e CPU

O **SO (Sistema Operacional)** gerencia a CPU.

---

## 8.1 Agendamento (Scheduling)

- distribui tempo de CPU entre processos
- garante uso justo

---

## 8.2 Gerenciamento de memória

- controla uso da RAM
- protege processos entre si

---

## 8.3 Entrada e Saída (I/O)

- coordena dispositivos (teclado, mouse, disco)
- gerencia comunicação com hardware

---

👉 Ideia principal:

> O SO é o “gerente da CPU”.

---

# 9. Virtualização

Virtualização permite rodar vários sistemas operacionais em uma única máquina.

---

## Elementos:

### Hypervisor

- software que cria e gerencia VMs

### Máquina Virtual (VM)

- “computador simulado”

### Extensões de hardware:

- Intel VT-x
- AMD-V

---

👉 Importante:

> A CPU precisa suportar virtualização por hardware para melhor desempenho.

---

# 10. Monitoramento de CPU

Ferramentas:

- Gerenciador de Tarefas (Windows)
- Monitor de Atividade (macOS)

---

O que elas mostram:

- uso da CPU (%)
- temperatura
- processos ativos

---

## Para que serve?

- identificar gargalos
- otimizar desempenho
- detectar sobrecarga

---

# 11. Resumo final (para prova)

### CPU é composta por:

- UC → controla
- ULA → processa
- Registradores → armazenam dados rápidos

### Ciclo:

Fetch → Decode → Execute → Store

### Performance depende de:

- clock
- cache
- núcleos
- arquitetura
- RAM

### Conceitos importantes:

- multicore ≠ multiprocessamento
- cache L1 > L2 > L3 (velocidade inversa ao tamanho)
- SO gerencia CPU