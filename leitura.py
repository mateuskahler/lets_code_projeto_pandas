import pandas as pd
import os

PASTA_DADOS = os.path.join('.', 'dados')

def ler_varios_csv_na_pasta(arquivos_csv, pasta, **kwargs):
    if arquivos_csv is None:
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
    
    
def juntar_dataframes(frame, other, tipo_join=None, chave=None):
    if chave:
        df = frame.merge(other, how=tipo_join, on=chave)
    
    else:
        df = frame.join(other)

    return df

def juntar_varios_dataframes(*dados):
    if len(dados) == 0:
        return None
    if len(dados) == 1:
        return dados[0]

    df = dados[0]

    for i in range(1,len(dados)):
        colunas_iguais = _ache_colunas_iguais(df, dados[i])
        df = juntar_dataframes(df, dados[i], tipo_join='left', chave=colunas_iguais)
    
    return df

def _ache_colunas_iguais(frame, other):
    cols1 = frame.columns
    cols2 = other.columns

    colunas_iguais = [i for i in cols1 if i in cols2]
    return colunas_iguais if colunas_iguais else None

def carregar_dados(arquivos = None, pasta = PASTA_DADOS, **kwargs):
    """
    Faz a leitura e junta todos os dados de interesse da pasta requisitada.

    Parâmetros
    ----------
    aquivos: iterable
        Iterável com nomes dos arquivos aos quais será feita a leitura. 
        Padrão: None, lê todos os arquivos em csv na pasta.

    pasta: str
        A pasta onde se encontram os arquivos. 
        Padrão: pasta dados no caminho de execução.

    kwargs:
        Parâmetros opcionais usados para leitura dos csv. 
        Ex: sep=';' ou encoding='utf-8'.

    Retorna
    -------
    Data frame com todos os dados da pasta unidos.
    """
    
    dados = ler_varios_csv_na_pasta(arquivos, pasta, **kwargs)

    frame = juntar_varios_dataframes(*dados)

    return frame
