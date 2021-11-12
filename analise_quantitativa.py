from numpy.lib.function_base import iterable
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def pegar_dados_quantitativos(df: pd.DataFrame):
    return df.select_dtypes(include=np.numeric)

def gerar_estatisticas(df, colunas : list = None, map_colunas:dict=None):
    if colunas is None:
        colunas = df.columns
    
    df_estatisticas = (
        df.describe()
          .loc[colunas]
    )

    if map_colunas:
        df_estatisticas.rename(index = map_colunas)

    return df_estatisticas.T


def gerar_estatisticas_quantitativas(df:pd.DataFrame, colunas : iterable = None, map_colunas:dict=None):
    df_estatisticas = gerar_estatisticas(pegar_dados_quantitativos(df),
                                         colunas=colunas, 
                                         map_colunas=map_colunas)
    return df_estatisticas

def eh_outliner(df:pd.DataFrame):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3-q1
    filtro_bool = (df < q1-1.5*iqr) | (df > q3 + 1.5 * iqr)
    return filtro_bool

def remove_outliners(df:pd.DataFrame, apenas_numericos=False):
    if apenas_numericos:
        df = pegar_dados_quantitativos(df)
    filtro_bool = eh_outliner(df)
    return df.mask(filtro_bool)

def preencher_com_mediana(df:pd.DataFrame):
    return df.fillna('median')