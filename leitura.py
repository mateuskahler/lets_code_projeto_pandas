import pandas as pd
import os

PASTA_DADOS = os.path.join('.', 'dados')

def ler_varios_csv_na_pasta(pasta, **kwargs):
    arquivos_nomes_com_extensao = os.listdir(pasta)

    arquivos_csv = [i for i in arquivos_nomes_com_extensao if i.split('.')[-1]=='csv']

    lista_de_dados = []
    for i in arquivos_csv:
        arquivo = os.path.join(pasta, i)
        df = ler_csv(arquivo, **kwargs)
        lista_de_dados.append(df)
    return lista_de_dados

def ler_csv(arquivo, **kwargs):
     return pd.read_csv(arquivo, **kwargs)
    
    
def juntar_tabelas(frame, other, tipo_join=None, chave=None):
    if chave:
        df = frame.merge(other, how=tipo_join, on=chave)
    
    else:
        df = frame.join(other)

    return df

def juntar_varios_arquivos(*dados):
    if len(dados) == 0:
        return None
    if len(dados) == 1:
        return dados[0]

    colunas_iguais = _ache_colunas_iguais(dados[0], dados[1])
    df = juntar_tabelas(dados[0], dados[1], tipo_join='left', chave=colunas_iguais)

    for i in range(2,len(dados)):
        colunas_iguais = _ache_colunas_iguais(df, dados[i])
        df = juntar_tabelas(df, dados[i], tipo_join='left', chave=colunas_iguais)
    
    return df

def _ache_colunas_iguais(frame, other):
    cols1 = frame.columns
    cols2 = other.columns

    colunas_iguais = [i for i in cols1 if i in cols2]
    return colunas_iguais if colunas_iguais else None

def carregar_dados(pasta = PASTA_DADOS, **kwargs):
    """
    Faz a leitura de todos os dados em csv da pasta requisitada.

    Parâmetros
    ----------
    pasta: str
        A pasta onde se encontram os arquivos. Padrão: pasta dados no caminho de execução.
    kwargs:
        Parâmetros opcionais usados para leitura dos csv. Ex: sep=';' ou encoding='utf-8'.

    Retorna
    -------
    Data frame com todos os dados da pasta unidos.
    """
    
    dados = ler_varios_csv_na_pasta(pasta, **kwargs)

    frame = juntar_varios_arquivos(*dados)

    return frame
