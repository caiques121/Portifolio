from selenium import webdriver
import time
import warnings
import pandas as pd
from datetime import date
import re
warnings.filterwarnings("ignore")

# Puxa a data de hoje para colocar no nome do arquivo
today = date.today()
d1 = today.strftime("%d/%m/%Y")
d1 = d1.replace("/", "-")

#### Cria o template da tabela que irei popular com os dados do Metacritic ######

data = {'Game': [''], 'Ranking': [''], 'Metascore': [
    ''], 'Platform': [''], 'Release Date': ['']}

df = pd.DataFrame(data)

# Define o Timer de carregamento de página
TIME_TO_WAIT = 0.8

# Carrega o webdriver do selenium e o Metacritic
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'C:\Users\p35z9yu\OneDrive-Deere&Co\OneDrive - Deere & Co\Desktop\Rotina\atualiza_relatorio\output'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(
    "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=condensed")
print("Conecta no Metacritic")

time.sleep(TIME_TO_WAIT * 4)

# Crio este while para ele ir passando página por página até dar erro (Quando não tem mais página pra rodar)
continuar_rodando = True

final = int(input("Informe o número da última página")) + 1

lista_paginas = list(range(0, int(final)))

del lista_paginas[0]

for i in lista_paginas:
    print("Fazendo scrap da página: " + str(i))
    a = driver.find_elements_by_class_name("clamp-list")

    for i in a:

        b = i.find_elements_by_class_name("expand_collapse")

        for y in b:

            a = y.text

            res = re.split(r"\n", a)

            score = res[0]
            ranking = res[1]
            ranking = ranking.replace(
                ".", "")
            title = res[2]
            platform = res[3]
            platform = platform.replace(
                "Platform: ", "")
            release = res[4]

            df['Game'] = str(title)
            df['Ranking'] = str(ranking)
            df['Metascore'] = str(score)
            df['Platform'] = platform
            df['Release Date'] = release

            df.to_csv("output/Best Video Games of All Time " +
                      str(d1) + ".csv", mode="a", sep=";")

    proximo = driver.find_elements_by_class_name("next")[0]
    proximo.click()
    time.sleep(TIME_TO_WAIT * 4)

print("Salvando os dados")
df = pd.read_csv("output/Best Video Games of All Time " +
                 str(d1) + ".csv", sep=";")

df = df[df['Game'] != 'Game']

del df['Unnamed: 0']

df.to_csv("output/Best Video Games of All Time " +
          str(d1) + ".csv", sep=";", index=False)
