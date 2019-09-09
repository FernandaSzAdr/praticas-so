# praticas-so
Provas práticas realizadas na disciplina de Sistemas Operacionais 

- Primeira prova prática está armazenada `pratica_geren_process`. Descrição da prova:
    
    - Implemente um "mini" simulador (mostrando a execução de, pelo menos, 5 processos do início ao término de todos) de comunicação inter-processos, conforme CADA abordagem abaixo:

        a) Soluções de software com busy wait: Algoritmo de Peterson.

        b) Soluções de software com bloqueio: Semáforos.

        Para esta questão, considerar a permuta de um processo (simulado como thread) para outro a cada 5 segundos considerando pelo menos uma variável compartilhada (região crítica). A entrada de processos deve ser dinâmica (passível de simulação com outras entradas).

     - Implemente um "mini" simulador (mostrando a execução de, pelo menos, 10 processos do início ao término de todos) de escalonamento de processos, conforme UM algoritmo da abordagem de sistemas interativos. Nesse caso foi o Round-robin por prioridades.

        Para esta questão, considerar a permuta de um processo (simulado como thread) para outro a cada 5 segundos considerando pelo menos três processo "HighPriority" e três processo "LowPriority". A entrada de processos deve ser dinâmica (passível de simulação com outras entradas).
