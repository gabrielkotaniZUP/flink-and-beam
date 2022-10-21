# About flink-and-beam stack

Comece facilmente a utilizar o `Apache Beam` e rodar Jobs no `Apache Flink` para processar dados através de **batch** ou **streaming** jobs.
Use `Python` e outras ferramentas com `GUI` para facilitar seus testes, e deixar seu ambiente organizado.


## Estrutura da Stack
A **Stack flink-and-beam** foi desenvolvida seguindo todas boas práticas de arquitetura de software:
+ Clean Architecture
+ Componenentes desacoplados

A Stack possui uma estrutura básica, onde o template cria estrutura de arquivos, e baixa as bibliotecas necessárias, subindo um serviço do Apache Flink localmente. 