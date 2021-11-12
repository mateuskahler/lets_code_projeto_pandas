import pandas as pd
import os

def ler_arquivo(arquivo, pasta):
    arquivo = os.path.join('.', pasta, arquivo) 
    df = pd.read_csv(arquivo, sep=';')
    return df
    
def juntar_arquivos(*arquivos, pasta, tipo_join=None, chave=None):
    arquivos = [*arquivos]
    lista_dataframes = []
    
    for i in range(len(arquivos)):
        df = ler_arquivo(arquivos[i], pasta=pasta)  
        lista_dataframes.append(df)

    if chave:
        df = lista_dataframes[0].merge(lista_dataframes[1], how=tipo_join, on=chave)
        arquivo = os.path.join('.', pasta, 'merged_df.csv') 
        df.to_csv(arquivo, sep=';', index=False)
    
    else:
        df = lista_dataframes[0].join(lista_dataframes[1])
        arquivo = os.path.join('.', pasta, 'merged_df.csv') 
        df.to_csv(arquivo, sep=';', index=False)

    return df