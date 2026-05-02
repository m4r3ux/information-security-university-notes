# Escalonamento de Processos — explicação completa

## 1. O que é escalonamento de processos?

Dentro de um sistema operacional (SO), existem vários processos competindo por recursos, principalmente a CPU.

Um processo é um programa em execução.

O problema central é o seguinte:  
A CPU (por núcleo) só consegue executar uma instrução por vez. Portanto, o sistema precisa decidir constantemente quem vai usar a CPU.

O escalonamento de processos é justamente o mecanismo responsável por decidir:

- qual processo será executado
- quando será executado
- por quanto tempo será executado

Sem esse controle, o sistema ficaria desorganizado e ineficiente.

---

## 2. Tipos de escalonamento (níveis)

O escalonamento ocorre em três níveis diferentes, cada um com uma função específica.

### 2.1 Longo prazo (Long-term scheduler)

Esse nível decide quais processos entram no sistema para competir pela CPU.

Função principal:

- controlar quantos processos estarão ativos
- evitar sobrecarga do sistema

Exemplo:  
Se muitos programas forem abertos ao mesmo tempo, o sistema pode não colocar todos imediatamente para execução.

Esse nível trabalha com o conceito de admissão de processos.

---

### 2.2 Médio prazo (Medium-term scheduler)

Esse nível gerencia a suspensão e reativação de processos.

Função principal:

- retirar processos da memória temporariamente (swap out)
- trazer processos de volta quando necessário (swap in)

Exemplo:  
Quando você minimiza um programa pesado, ele pode ser suspenso para liberar memória.

Isso ajuda a melhorar o desempenho geral do sistema.

---

### 2.3 Curto prazo (Short-term scheduler)

Esse é o nível mais importante.

Ele decide qual processo pronto será executado imediatamente pela CPU.

Características:

- atua constantemente
- realiza decisões em alta frequência

Exemplo:  
Você pode estar com vários programas abertos ao mesmo tempo, e o sistema alterna rapidamente entre eles.

Isso cria a sensação de multitarefa.

---

## 3. Algoritmos de escalonamento

Agora entramos em como o sistema toma decisões.

---

### 3.1 FCFS (First Come, First Served)

Funcionamento:

- os processos são executados na ordem de chegada
- não há interrupção

Exemplo:  
Uma fila de atendimento.

Vantagem:

- simples de implementar

Desvantagem:

- processos longos podem atrasar todos os outros
- pode gerar alto tempo de espera

---

### 3.2 SJF (Shortest Job First)

Funcionamento:

- executa primeiro o processo com menor tempo estimado

Vantagem:

- reduz o tempo médio de espera

Desvantagens:

- é difícil prever o tempo de execução
- pode causar inanição

Inanição significa que processos maiores podem nunca ser executados porque sempre chegam processos menores.

---

### 3.3 Round Robin

Funcionamento:

- cada processo recebe um pequeno intervalo de tempo chamado quantum
- se não terminar, volta para o final da fila

Exemplo:  
Cada processo executa por alguns milissegundos.

Vantagens:

- distribuição justa de tempo de CPU
- muito utilizado em sistemas modernos

---

### 3.4 Escalonamento por prioridade

Funcionamento:

- cada processo recebe um nível de prioridade
- processos mais importantes executam primeiro

Problema:

- processos de baixa prioridade podem nunca executar

Solução:

- técnica de envelhecimento (aging), onde a prioridade aumenta com o tempo

---

## 4. Criação de processos

Um processo pode ser criado de várias formas.

1. Inicialização do sistema:  
    O sistema operacional cria processos essenciais ao iniciar.
2. Requisição do usuário:  
    Quando o usuário abre um programa.
3. Chamada de sistema:  
    Um processo cria outro processo.
4. Operação em lote:  
    Processos são executados automaticamente pelo sistema.

---

## 5. Comunicação entre processos (IPC)

Processos frequentemente precisam trocar informações.

Principais métodos:

Memória compartilhada:

- processos acessam a mesma área de memória
- rápido, mas exige controle rigoroso

Troca de mensagens:

- comunicação via envio e recebimento de mensagens
- mais segura

Pipes e FIFOs:

- comunicação sequencial de dados
- comum em sistemas Unix

Sockets:

- permitem comunicação entre processos em máquinas diferentes

---

## 6. Sincronização de processos

Problema:  
Vários processos acessando o mesmo recurso ao mesmo tempo podem gerar inconsistência.

Ferramentas para controle:

Semáforos:

- controlam quantos processos podem acessar um recurso

Mutex:

- garante que apenas um processo acesse o recurso

Monitores:

- abstração de alto nível para controle de acesso

Variáveis de condição:

- permitem que processos aguardem até uma condição ser satisfeita

---

## 7. Problema da seção crítica

Seção crítica é a parte do código onde há acesso a recursos compartilhados.

Uma solução correta deve garantir três condições:

1. Exclusão mútua:  
    Apenas um processo pode acessar a seção crítica por vez.
2. Progresso:  
    O sistema não pode ficar travado sem necessidade.
3. Espera limitada:  
    Nenhum processo pode esperar indefinidamente.

---

## 8. Problemas clássicos de sincronização

Esses problemas são usados para estudar concorrência.

Jantar dos Filósofos:

- ilustra problemas de deadlock

Produtor-Consumidor:

- um processo produz dados e outro consome
- exige sincronização do buffer

Leitores-Escritores:

- múltiplos leitores podem acessar simultaneamente
- escritores precisam de exclusividade

---

## 9. Conexão geral dos conceitos

O funcionamento do sistema pode ser entendido assim:

- vários processos competem por recursos
- o sistema operacional decide quem executa (escalonamento)
- processos precisam se comunicar (IPC)
- isso gera problemas de concorrência
- a sincronização resolve esses problemas

---

# 1. Por que programação concorrente é difícil?

Antes de entrar nas boas práticas, você precisa entender o problema central:

Quando vários processos ou threads executam ao mesmo tempo:

- eles podem acessar os **mesmos dados**
- em **ordens diferentes**
- em **tempos imprevisíveis**

Isso gera comportamentos como:

- resultados inconsistentes
- travamentos
- erros que aparecem “às vezes” (os mais perigosos)

Por isso o slide começa com:

## Testar e depurar código concorrente

Diferente de programas sequenciais, aqui não basta testar uma vez.

É necessário garantir que o sistema funcione:

- com várias threads
- em diferentes ordens de execução
- sob carga alta

Ou seja:

> você não testa um caminho — você testa **vários cenários possíveis de execução**

---

# 2. Abstrações de alto nível

Agora entra uma ideia muito importante: **não trabalhar diretamente com baixo nível quando possível**

## O que são abstrações de alto nível?

São ferramentas que escondem a complexidade de:

- mutex
- semáforos
- controle manual de threads

E oferecem algo mais simples, como:

- filas de tarefas
- pools de threads
- estruturas prontas

## Por que isso é importante?

Programação concorrente no baixo nível é:

- propensa a erro
- difícil de manter
- difícil de entender

Então, abstrações permitem que você foque na lógica do problema, e não nos detalhes técnicos.

---

# 3. Bibliotecas e frameworks de concorrência

Essas abstrações geralmente vêm em forma de bibliotecas.

Elas oferecem três grandes benefícios:

---

## 3.1 Padrões de concorrência

São soluções já prontas para problemas comuns.

Exemplos importantes:

- Thread Pool:
    - reutiliza threads em vez de criar novas toda hora
    - melhora desempenho
- Fila de trabalho (work queue):
    - tarefas são colocadas em uma fila
    - threads consomem essas tarefas
- Barreiras de sincronização:
    - processos esperam até todos chegarem em um ponto

A ideia central é:

> não reinventar soluções — usar padrões já testados

---

## 3.2 Garantias de segurança

Essas bibliotecas ajudam a evitar problemas automaticamente, como:

- condições de corrida
- deadlocks

Como fazem isso?

- verificações em tempo de execução
- restrições na forma como o código é escrito
- controle interno de acesso aos dados

Isso aumenta muito a confiabilidade do sistema.

---

# 4. Evitando condições de corrida

Esse é um dos problemas mais importantes.

## O que é condição de corrida?

Acontece quando:

> o resultado depende da ordem de execução das threads

Exemplo simples:  
Duas threads incrementam uma variável ao mesmo tempo → resultado errado.

---

## 4.1 Identificação de recursos compartilhados

Primeiro passo:

Você precisa saber **o que pode ser acessado por vários processos ao mesmo tempo**, como:

- variáveis globais
- arquivos
- estruturas de dados

Se você não identificar isso, não consegue proteger.

---

## 4.2 Implementação de proteções

Depois de identificar, você protege usando:

- mutex (exclusão mútua)
- semáforos
- locks

Objetivo:

> garantir acesso controlado ao recurso

---

## 4.3 Verificação de atomicidade

Uma operação atômica é:

> indivisível — não pode ser interrompida

Exemplo:

- leitura + modificação + escrita → deve ser feita como um bloco único

Se não for atômico:

- outra thread pode interferir no meio da operação

---

## 4.4 Testes de concorrência

Aqui entra uma prática essencial:

Você precisa testar especificamente para detectar:

- condições de corrida
- falhas de sincronização

Como?

- testes com múltiplas threads
- execução repetida
- testes de estresse

---

# 5. Deadlocks (impasses)

Outro problema crítico.

## O que é deadlock?

Situação onde:

- processos ficam esperando recursos
- e nenhum consegue continuar

Exemplo clássico:  
Processo A espera recurso de B  
Processo B espera recurso de A

Resultado: travamento total

---

# 6. Como lidar com deadlocks

O slide mostra três abordagens principais:

---

## 6.1 Algoritmos de detecção

O sistema analisa o estado atual:

- constrói um grafo de recursos
- verifica se há ciclos

Se houver ciclo → há deadlock

Pode ser feito:

- periodicamente
- sob demanda

---

## 6.2 Estratégias de prevenção

Aqui a ideia é evitar que o problema aconteça.

Técnicas importantes:

- Ordenação de recursos:  
    Sempre adquirir recursos na mesma ordem
- Alocação completa:  
    Só executa se todos os recursos estiverem disponíveis
- Verificação de segurança:  
    Garante que o sistema não entre em estado perigoso

---

## 6.3 Mecanismos de recuperação

Se o deadlock já aconteceu:

O sistema pode:

- encerrar processos
- retirar recursos (preempção)
- voltar o sistema para um estado anterior (rollback)

Isso geralmente tem custo alto.

---

# 7. Teste e depuração de código concorrente

Essa é a parte final e mais prática.

## Por que é difícil?

Porque os erros:

- não são determinísticos
- não acontecem sempre
- dependem do tempo de execução

---

## Ferramentas usadas:

### Análise estática

- analisa o código sem executar
- encontra possíveis problemas

### Análise dinâmica

- monitora o sistema em execução
- detecta erros reais

---

## Técnicas importantes:

### Execução determinística

- tenta reproduzir o mesmo comportamento sempre

### Injeção de falhas

- força situações problemáticas

### Testes de estresse

- executa com muitas threads
- simula carga alta

---

# 8. Conexão geral do conteúdo

Tudo isso está conectado da seguinte forma:

- Programas concorrentes executam múltiplas threads
- Isso gera problemas como:
    - condições de corrida
    - deadlocks
- Para evitar isso:
    - usamos sincronização
    - usamos abstrações de alto nível
- Para garantir que funciona:
    - testamos intensivamente
    - usamos ferramentas especializadas

---

# 9. Ideia central para prova

Se tiver que resumir:

- Concorrência aumenta desempenho, mas traz complexidade
- Problemas principais:
    - condição de corrida
    - deadlock
- Solução:
    - sincronização
    - boas práticas
    - testes rigorosos

---

# 1. Visão geral: gerenciamento de processador no Linux

O tema central do slide é:

> Como o Linux cria, executa, controla e finaliza processos

O Linux segue a tradição dos sistemas UNIX, mas introduz melhorias importantes em:

- desempenho
- flexibilidade
- concorrência

---

# 2. O que é um processo no Linux?

## Definição de processo

Um processo é:

> uma instância de um programa em execução com recursos próprios

Esses recursos incluem:

- memória
- registradores da CPU
- arquivos abertos
- estado de execução

Ou seja:

> o processo é a unidade básica de execução no sistema

---

## Contexto de execução

Cada processo possui seu próprio **contexto**, que inclui:

- contador de programa (qual instrução será executada)
- registradores
- pilha
- espaço de memória

Isso garante:

- isolamento entre processos
- segurança (um processo não interfere no outro diretamente)

---

## Compatibilidade com UNIX

O Linux foi projetado para ser compatível com UNIX, então:

- mantém conceitos clássicos
- mas melhora desempenho e flexibilidade

---

# 3. Separação entre criação e execução (ponto muito importante)

Diferente de outros sistemas, o Linux separa claramente:

- criação de processo
- execução de programa

Essa separação é fundamental e aparece no modelo:

## Modelo fork-exec

### fork()

- cria um novo processo (cópia do processo atual)
- o novo processo é chamado de filho

### exec()

- substitui o código do processo atual por outro programa

---

## Por que isso é importante?

Essa separação permite:

- maior controle do sistema
- criação de estruturas complexas (ex: servidores)
- manipulação do ambiente antes de executar um programa

---

# 4. Funcionamento do exec() (passo a passo)

Quando um processo chama exec(), o kernel faz várias etapas:

### 1. Validação

- verifica permissões
- verifica formato do executável

### 2. Liberação de recursos

- remove o programa anterior da memória
- mantém arquivos abertos

### 3. Carregamento

- carrega o novo programa na memória (.text, .data, etc.)

### 4. Preparação da pilha

- organiza argumentos (argv)
- define variáveis de ambiente (envp)

### 5. Execução

- começa a executar o novo programa

Importante:

> o processo continua sendo o mesmo, mas o programa muda

---

# 5. Threads vs Processos no Linux

Aqui entra uma característica muito importante do Linux:

## “Tudo é processo”

No Linux:

- threads são implementadas como processos leves

---

## Diferença principal

### Processos:

- possuem memória independente
- são isolados

### Threads:

- compartilham:
    - memória
    - arquivos
    - recursos

---

## Consequência disso

Vantagem:

- troca de contexto mais rápida

Desvantagem:

- maior risco de problemas de concorrência  
    (condições de corrida, por exemplo)

---

# 6. A chamada de sistema clone()

Essa é a base de tudo no Linux moderno.

## O que clone() faz?

Permite criar processos ou threads com controle total sobre o que será compartilhado.

---

## Flags importantes

Você pode escolher o que compartilhar:

- CLONE_VM → compartilha memória
- CLONE_FS → compartilha sistema de arquivos
- CLONE_FILES → compartilha arquivos abertos
- CLONE_SIGHAND → compartilha sinais

---

## Por que isso é poderoso?

Porque permite criar:

- processos independentes
- threads completas
- modelos híbridos

---

## Relação com pthreads

Bibliotecas como pthreads usam clone() internamente.

Ou seja:

> clone() é a base da concorrência no Linux

---

# 7. Estados de processos no Linux

Um processo pode estar em diferentes estados:

---

## Running

- está executando ou pronto para executar

---

## Waiting (Blocked)

- esperando algo (I/O, evento, etc.)
- não pode executar

---

## Stopped

- foi pausado (ex: SIGSTOP)
- pode ser retomado

---

## Zombie

Muito importante para prova.

- processo já terminou
- mas ainda existe na tabela de processos

Por quê?  
Porque o pai ainda não coletou o resultado

---

# 8. Processos Zombie e Órfãos

## Zombie

Ocorre quando:

- processo termina
- pai não chama wait()

Consequência:

- ocupa espaço na tabela de processos

---

## Órfão

Ocorre quando:

- processo pai morre antes do filho

Solução:

- o processo init (PID 1) adota o filho

---

## Coleta de processos

Funções usadas:

- wait()
- waitpid()
- waitid()

Objetivo:

- liberar recursos
- evitar zombies

---

# 9. Chamadas de sistema importantes

## Criação

- fork() → cria processo
- clone() → cria com controle
- exec() → executa programa
- posix_spawn() → versão otimizada

---

## Monitoramento

- wait() → espera filho terminar
- waitpid() → espera filho específico
- getpid() → pega ID do processo

---

## Controle

- kill() → envia sinais
- setpriority() → muda prioridade
- sched_setaffinity() → define CPU
- exit() → encerra processo

---

# 10. Diferenças do Linux para outros UNIX

## fork() otimizado

Linux usa Copy-on-Write:

- não copia memória imediatamente
- copia apenas quando necessário

Resultado:

- fork() mais rápido

---

## Modelo de threads

Linux:

- threads = processos leves (clone)

Outros UNIX:

- distinção mais rígida

---

# 11. Escalonamento no Linux

O Linux usa o:

## Completely Fair Scheduler (CFS)

Objetivo:

- distribuir CPU de forma justa

Características:

- evita que processos monopolizem CPU
- melhora resposta interativa

---

# 12. Namespaces (conceito moderno)

Esse é um dos pontos mais atuais.

## O que são namespaces?

São mecanismos que isolam recursos entre processos.

Exemplo:

- processos veem sistemas diferentes

---

## Para que serve?

Base de:

- containers (Docker, por exemplo)
- virtualização leve

---

# 13. Conexão geral do conteúdo

Agora juntando tudo:

- Processo é a unidade básica
- fork() cria processos
- exec() executa programas
- clone() permite concorrência avançada
- processos têm estados
- precisam ser gerenciados (wait, kill, etc.)
- escalonador distribui CPU
- namespaces permitem isolamento moderno

---

# 14. O que você precisa guardar para prova

- Modelo fork + exec é central no Linux
- clone() é base das threads
- diferença entre processo e thread
- estados de processo (especialmente zombie)
- Copy-on-Write no fork()
- CFS como escalonador
- namespaces para isolamento
