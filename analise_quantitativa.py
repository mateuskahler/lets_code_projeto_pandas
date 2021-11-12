from numpy.lib.function_base import iterable
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def pegar_dados_quantitativos(df: pd.DataFrame):
    return df.select_dtypes(include=np.number) 

def gerar_estatisticas(df, estimadores : list = None, map_nomes_estimadores:dict=None):

    df_estatisticas = df.describe()


    if estimadores:
        df_estatisticas = df_estatisticas.loc[estimadores]

    if map_nomes_estimadores:
        df_estatisticas = df_estatisticas.rename(index = map_nomes_estimadores)

    return df_estatisticas.T


def gerar_estatisticas_quantitativas(df:pd.DataFrame, estimadores = None, map_nomes_estimadores:dict=None):
    df = pegar_dados_quantitativos(df)
    df_estatisticas = gerar_estatisticas(df,
                                         estimadores=estimadores, 
                                         map_nomes_estimadores=map_nomes_estimadores)
    return df_estatisticas

def eh_outliner(df:pd.DataFrame):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3-q1
    filtro_bool = (df < q1-1.5*iqr) | (df > q3 + 1.5 * iqr)
    return filtro_bool

def remover_outliners(df:pd.DataFrame, apenas_numericos=False):
    if apenas_numericos:
        df = pegar_dados_quantitativos(df)
    filtro_bool = eh_outliner(df)
    return df.mask(filtro_bool)

def preencher_com_mediana(df:pd.DataFrame):
    return df.fillna(df.median())