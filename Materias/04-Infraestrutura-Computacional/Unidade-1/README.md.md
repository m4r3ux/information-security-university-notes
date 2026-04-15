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

