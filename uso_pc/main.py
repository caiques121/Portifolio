## Autor: Caique Rezende
## Objetivo: Este script tem como objetivo capturar o % de usagem de CPU e Memória RAM a cada segundo, para posteriores estudos.
## Data de Criação: 08/09/2022

## Carrega as bibliotecas
import pandas as pd
import psutil
import time
from datetime import datetime

## Define o intervalo de obtenção e registro dos dados
espera = 1

## Cria uma lista, que posteriormente vai ser utilizada como recipiente para os resultados capturados
registra = []

while True:

    # Registra a data e a hora
    hora = datetime.now()

    # Formata a data e a hora
    hora_formatada = hora.strftime("%d/%m/%Y %H:%M:%S")

    ## Define a variável com o valor percentual de usagem do CPU
    perc_cpu = psutil.cpu_percent()

    ## Define a variável com o valor percentual de usagem da memória RAM
    perc_memoria_ram = psutil.virtual_memory()

    ## Cria um dataframe vazio que vai registrar as 3 variáveis principais
    df = [{"% Usagem do CPU": "", "% Usagem da Memória RAM": "", "Data e Hora": ""}]
    df = pd.DataFrame(df)

    ## Adiciona as variáveis ao dataframe
    df["% Usagem do CPU"] = str(perc_cpu)
    df["% Usagem da Memória RAM"] = str(perc_memoria_ram[2])
    df["Data e Hora"] = str(hora_formatada)

    ## Espera
    time.sleep(espera)

    ## Quando for 17h, o loop para e segue adiante
    if hora.hour == 17 and hora.minute >= 0:
        break

## Depois das 17h o loop de registro de informação para, e concatena os resultados em um dataframe
df1 = pd.concat(registra)

## Removo dados de lixo criados pelo pelo método do loop
df1 = df1[df1["% Usagem da Memória RAM"] != "% Usagem da Memória RAM"]

## Exporto isso em um .csv, com o Mode = "'a", para ao invés de sobrescrever, acumular
df1.to_csv("output/Registro Utilização do PC.csv", mode="a", sep=";", index=False)
