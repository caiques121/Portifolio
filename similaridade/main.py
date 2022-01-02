import pandas as pd
from difflib import SequenceMatcher
import warnings
warnings.filterwarnings("ignore")


def similaridade(a, b):
    return SequenceMatcher(None, a, b).ratio()

df = pd.read_excel(
    "input/generic_data.xlsx")

ibge = pd.read_excel("input/ibge_data.xlsx")

df['chave'] = df['Município'].str.replace(
    '[^A-Za-z0-9]+', '')

df["chave"] = df["chave"].str.lower()

ibge['chave'] = ibge['nome'].str.replace(
    '[^A-Za-z0-9]+', '')

ibge["chave"] = ibge["chave"].str.lower()

df = df[['chave','Município','Estado']]

df['Registro Correto'] = ''

df['Similaridade'] = ""

def funcao_similaridade(porc_similaridade):
    
    for i in range(len(df)):
        ibge_filt = ibge[ibge['Estado'] == df['Estado'].iloc[i]]
        
        for y in range(len(ibge_filt)):
    
            try:

                if similaridade(str(df['chave'].loc[i]), str(ibge_filt['chave'].loc[y])) >= porc_similaridade:

                    df['Registro Correto'][i] = ibge_filt['nome'][y]
                    df['Similaridade'] = "%Similaridade" + str(porc_similaridade)
                    df1 = df[df['Registro Correto'] == df['Registro Correto'][i]]
                    df1.to_csv("output/results.csv", sep = ";", encoding="utf-8", mode = "a")
                    continue

                else:
                    pass 
                                

            except KeyError:
                pass
                next

funcao_similaridade(0.50)