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


---

# Sistema de Arquivos

O sistema de arquivos é um dos componentes mais importantes de um sistema operacional, porque ele é responsável por organizar, armazenar, localizar, proteger e recuperar informações em dispositivos de armazenamento, como HDs, SSDs, pendrives e até servidores remotos.

Sem um sistema de arquivos, os dados existiriam apenas como uma sequência desorganizada de bits no disco, sem nomes, pastas ou estrutura lógica.

## O que é um sistema de arquivos?

Um sistema de arquivos é o mecanismo utilizado pelo sistema operacional para:
- armazenar arquivos;
- localizar dados no disco;
- organizar diretórios;
- controlar permissões;
- permitir leitura e gravação;
- compartilhar informações entre programas.

Na prática, ele funciona como uma “biblioteca digital”. Imagine um computador sem sistema de arquivos:
- não existiriam pastas;
- os arquivos não teriam nomes;
- o sistema não saberia onde cada informação está armazenada;
- recuperar dados seria praticamente impossível.

## Importância do armazenamento e recuperação de informações

O slide destaca que:
> “armazenar e recuperar informações são atividades essenciais”.

Isso acontece porque praticamente tudo em um computador depende disso: documentos, fotos, vídeos, programas, bancos de dados e arquivos do sistema operacional.

Os processos precisam:
- gravar dados permanentemente;
- ler dados já armazenados;
- compartilhar arquivos com outros processos.

Exemplo: um navegador salva downloads, um editor de texto grava documentos, um banco de dados salva registros e o sistema operacional armazena configurações. Tudo isso depende do sistema de arquivos.

## O que é um arquivo?

Um arquivo é um conjunto de informações logicamente relacionadas. Essas informações podem representar: dados, instruções, configurações, imagens, vídeos ou programas executáveis.

### Exemplos de arquivos

#### Arquivo executável
Contém instruções que o processador consegue executar.
- **Exemplos:** `.exe`, `.bin`, `.app`.
- **Exemplos práticos:** Google Chrome, Word, Photoshop.

#### Arquivos de dados
Armazenam informações utilizadas por aplicações.
- **Exemplos:** `.txt`, `.csv`, `.json`, `.xml`.
- **Podem conter:** textos, tabelas, configurações ou dados estruturados.

#### Arquivos de sistema
São essenciais para o funcionamento do sistema operacional.
- **Exemplos:** `.dll`, `.sys`, `.so`.
- **Armazenam:** drivers, bibliotecas ou componentes internos do sistema. Sem eles, o sistema operacional pode nem iniciar.

### Arquivos como abstração
O slide fala que o conceito de arquivo é “abstrato e generalista”. Isso significa que o usuário não precisa saber em qual setor do disco o dado está ou como o hardware acessa os bits. O sistema de arquivos esconde essa complexidade, e o usuário apenas vê nome, pasta, extensão e tamanho.

## Operações de entrada e saída (E/S)

As operações de entrada e saída permitem ler, gravar, criar e apagar arquivos. O sistema operacional oferece rotinas padronizadas para isso, criando uma interface simples entre aplicações e hardware.

O programa não conversa diretamente com o disco.
**Fluxo:** Aplicação → Rotinas de E/S → Dispositivo

**Exemplo prático:** Quando um programa salva um arquivo, a aplicação solicita a gravação, o sistema operacional recebe a solicitação e o driver do disco executa a operação física. O programa não precisa saber como o disco funciona.

## Atributos de arquivos

Cada arquivo possui metadados chamados atributos que descrevem suas características.

- **Nome:** Identificador usado pelo usuário (ex: `relatorio.txt`).
- **Extensão:** Indica o tipo do arquivo (ex: `.pdf`, `.jpg`, `.mp4`). Ajuda o sistema a identificar qual programa abrir.
- **Tamanho:** Quantidade de bytes ocupados (ex: 15 MB).
- **Proprietário:** Usuário responsável pelo arquivo (importante em Linux e servidores).
- **Timestamps:** Registram data de criação, última modificação e último acesso.
- **Permissões:** Definem quem pode ler, escrever e executar (ex: `rwxr-xr--`).

## Diretórios

Diretórios (pastas) organizam arquivos logicamente e funcionam como índices, armazenando nomes, localizações, atributos e ponteiros para arquivos. Sem diretórios, todos os arquivos ficariam “misturados”.

**Exemplo de organização:**
- `Documentos/`
  - `trabalho.docx`
  - `provas.pdf`
- `Imagens/`
  - `foto.png`

## Sistemas de arquivos remotos

Com redes de computadores, tornou-se possível acessar arquivos remotamente, permitindo compartilhamento, colaboração e armazenamento distribuído.

- **FTP (File Transfer Protocol):** Um dos primeiros métodos para enviar e baixar arquivos entre computadores.
- **DFS — Distributed File System:** Sistema de arquivos distribuído onde os arquivos ficam em vários servidores, mas aparecem como se fossem locais. Exemplos modernos incluem Google Drive, OneDrive e Dropbox.
- **Computação em nuvem:** Arquivos ficam em data centers acessados pela internet, oferecendo sincronização, backup e acesso remoto.

## Implementação do sistema de arquivos

O sistema operacional mantém estruturas em disco e em memória RAM para controlar a localização dos arquivos, espaço livre, arquivos abertos e cache.

### Estruturas em disco
- **Bloco de controle de inicialização (boot block):** Contém informações para iniciar o sistema operacional.
- **Bloco de controle de volume:** Armazena tamanho da partição, quantidade de blocos, blocos livres e ponteiros.
- **Estrutura de diretórios:** Organiza nomes, inodes e localização.
- **FCB (File Control Block):** Armazena informações detalhadas (tamanho, permissões, localização, timestamps).

### Estruturas em memória
- **Tabela de montagens:** Controla os volumes montados (HD, SSD, pendrive).
- **Cache de diretórios:** Mantém diretórios acessados recentemente para acelerar buscas.
- **Tabela de arquivos abertos:** Controla quais arquivos estão abertos e quem os usa.
- **Buffers:** Armazenam temporariamente blocos lidos ou gravados para melhorar o desempenho do disco.

## Sistemas de arquivos distribuídos

Em sistemas distribuídos, os dados ficam espalhados por vários servidores.

**Objetivos principais:**
- **Alta disponibilidade:** Dados acessíveis mesmo se um servidor falhar.
- **Tolerância a falhas:** Sistema continua funcionando com problemas na infraestrutura.
- **Replicação:** Dados copiados para vários locais para segurança e disponibilidade.

**Problema da consistência:** Todas as cópias precisam permanecer iguais, exigindo protocolos de sincronização.
**Segurança:** Risco de interceptação na rede, exigindo autenticação, criptografia e controle de acesso.

## Relação entre sistema de arquivos e sistema operacional

O sistema de arquivos é um dos pilares do sistema operacional, trabalhando com gerenciamento de memória, processos e drivers. Sem ele, não haveria armazenamento persistente ou organizado.

## Resumo Geral

- **Sistema de arquivos:** Organiza e controla armazenamento.
- **Arquivos:** Conjuntos de dados ou instruções.
- **Diretórios:** Organizam arquivos logicamente.
- **Atributos:** Metadados dos arquivos.
- **Operações de E/S:** Permitem leitura e gravação.
- **Sistemas remotos:** Permitem compartilhamento em rede.
- **Implementação:** Estruturas em disco e memória.
- **Sistemas distribuídos:** Armazenamento em múltiplos servidores.
- **Segurança:** Protege arquivos e acessos.

## Conceitos mais importantes para prova
- **Arquivo:** Conjunto lógico de dados.
- **Diretório:** Estrutura de organização.
- **Metadados:** Atributos do arquivo.
- **Abstração:** Ocultação da complexidade física.
- **Consistência:** Manutenção de cópias idênticas.


---

# Sistema de Arquivos – Segurança

A segurança em sistemas de arquivos é uma das áreas mais importantes da computação moderna, porque praticamente todas as informações importantes de um sistema estão armazenadas em arquivos:
- documentos;
- senhas;
- bancos de dados;
- programas;
- registros financeiros;
- informações pessoais;
- arquivos do sistema operacional.

O objetivo da segurança é garantir que essas informações:
- não sejam acessadas indevidamente;
- não sejam modificadas sem autorização;
- não sejam destruídas;
- permaneçam disponíveis para usuários legítimos.

## O que significa um sistema seguro?

O slide define:
> “um sistema é seguro quando seus recursos são usados e acessados como esperado sob todas as circunstâncias”.

Isso significa que:
- usuários autorizados conseguem usar os recursos normalmente;
- usuários não autorizados são bloqueados;
- os dados permanecem íntegros;
- o sistema continua funcionando corretamente.

### Segurança total existe?
O próprio slide destaca: **“a segurança total não pode ser atingida”**. Isso ocorre porque sempre surgem novas vulnerabilidades, softwares possuem falhas, usuários cometem erros e atacantes criam novas técnicas. Portanto, o objetivo real da segurança é reduzir riscos, dificultar ataques e minimizar danos.

## Violações de segurança

As violações podem ser:

- **Acidentais:** Ocorrem sem intenção maliciosa (ex: apagar um arquivo sem querer, enviar informações ao destinatário errado, erro de configuração).
- **Maliciosas:** São ataques intencionais (ex: invasões, roubo de dados, instalação de malware, destruição de arquivos).

O slide destaca que proteger contra erros acidentais é mais fácil, enquanto ataques maliciosos são mais complexos e difíceis de impedir.

## Tipos de violações de segurança

O conteúdo apresenta os principais tipos de ameaças, o que é extremamente importante para provas.

### 1. Brecha de sigilo (confidencialidade)
Ocorre quando alguém acessa informações sem autorização.
- **Objetivo:** roubo de dados, espionagem, obtenção de informações sigilosas.
- **Exemplos:** roubo de senhas, vazamento de cartões de crédito, acesso indevido a banco de dados.
- **Consequência:** Perda de confidencialidade. O dado continua existindo, mas pessoas indevidas tiveram acesso.

### 2. Brecha de integridade
Ocorre quando dados são modificados sem autorização. O invasor altera a informação.
- **Exemplos:** modificar notas em um sistema escolar, alterar valores bancários, editar código-fonte.
- **Consequência:** A informação deixa de ser confiável. (Ex: alterar `saldo = 100` para `saldo = 100000`).

### 3. Brecha de disponibilidade
Relacionada à destruição ou indisponibilidade dos dados. O usuário legítimo não consegue utilizá-los.
- **Exemplos:** apagar arquivos, derrubar servidores, ransomware.
- **Desfiguração de sites (defacement):** O invasor altera a página inicial para causar impacto ou demonstrar invasão.

### 4. Roubo de serviço
Ocorre quando alguém usa recursos sem autorização.
- **Exemplos:** usar processamento do servidor, consumir banda de internet, mineração ilegal de criptomoedas.
- **Exemplo clássico:** Um invasor instala um programa escondido para enviar spam ou minerar criptomoedas, e o dono do servidor paga a conta.

### 5. Recusa de serviço (DoS)
**DoS = Denial of Service.** O objetivo é impedir usuários legítimos de utilizarem o sistema sobrecarregando o servidor, rede ou aplicação.
- **Resultado:** lentidão, travamentos ou indisponibilidade.
- **Worm da Internet:** O slide menciona um caso clássico onde um worm gerou congestionamento e criou um ataque DoS involuntário.

## Métodos usados por atacantes

### Mascaramento (spoofing)
O invasor finge ser outra entidade (usuário, computador ou servidor) para enganar o sistema e obter acesso ou permissões.

### Intermediário (Man-in-the-Middle)
O invasor intercepta a comunicação entre emissor e receptor para ler dados, modificar informações ou roubar senhas.

## Níveis de proteção de segurança

O slide divide a segurança em quatro níveis fundamentais.

1. **Segurança física:** Protege o ambiente físico (salas trancadas, biometria, câmeras). Se alguém tiver acesso físico, pode roubar discos ou instalar malwares.
2. **Segurança humana:** Relacionada às pessoas. Usuários podem compartilhar senhas ou cometer erros.
   - **Engenharia social:** O atacante manipula pessoas (phishing, falsas ligações) em vez de atacar o sistema diretamente.
3. **Segurança do sistema operacional:** O SO deve impedir acesso indevido, processos maliciosos e escalonamento de privilégios.
   - **Estouro de pilha (buffer overflow):** Quando dados excedem limites de memória, permitindo execução de código malicioso.
4. **Segurança de rede:** Protege os dados que trafegam pela rede contra interceptação e ataques remotos. Soluções incluem criptografia, VPN, HTTPS e firewalls.

> **“A corrente é tão forte quanto o elo mais fraco”**
> Significa que a segurança depende de TODOS os níveis. Não adianta ter criptografia avançada se a senha está escrita em um papel.

## Ameaça de programas

Programas são um dos maiores meios de ataque porque tudo no computador executa através de processos.

### Daemon de porta dos fundos (backdoor)
Programas ocultos que permitem acesso futuro mesmo após a invasão inicial. O invasor instala o backdoor e retorna quando quiser.

### Importância do isolamento de processos
O isolamento evita que um processo acesse a memória de outro, prevenindo interferências indevidas e corrupção de dados.

## Estratégias de ataque (Ciclo típico)
1. **Acesso inicial:** Encontrar vulnerabilidade ou senha fraca.
2. **Estabelecimento de processo malicioso:** Instalar malware ou backdoor.
3. **Ocultação de rastros:** Apagar logs e registros.
4. **Manutenção do acesso:** Garantir entrada futura.

## Medidas de proteção
- **Monitoramento de processos:** Acompanhar CPU e memória para detectar atividades suspeitas.
- **Análise de código:** Examinar programas para identificar falhas antes da execução.
- **Privilégios mínimos:** Garantir que processos tenham apenas as permissões necessárias.
