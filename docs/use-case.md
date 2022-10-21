# Use case

## Visão Geral:
Comece facilmente a utilizar o `Apache Beam` e rodar Jobs no `Apache Flink` para processar dados através de **batch** ou **streaming** jobs.

## Pré-requisitos:
+ STK CLI
+ Python 3.6+
+ pip
+ Docker Compose

## Inputs
Os inputs necessários para utilizar o template são:
| Campo | Valor | Descrição |
| Project name | Texto | Nome do projeto |

## Serviços:
+ `Flink & Beam` : Construído em cima da imagem *dataradiant/beam-flink*.

## Portas:
+ `Flink` : porta: 48080

## Quick-start:


### Accesse a pagina via browser
Abra um browser e acesse http://localhost:48080

### Inicie por exemplo

Abra o arquivo `example.py` para iniciar um job do Beam no Flink
```Python
with beam.Pipeline(options) as p:
    # Configure o codigo abaixo para criar seu pipeline
    print('Write your Beam code below, and it will run on Flink locally.')
```
