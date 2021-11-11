import pandas as pd
from pathlib import Path

import os


def criar_caminho_arquivo(nome_arquivo):
    PASTA_DOS_DADOS = 'dados'

    return os.path.join('.', PASTA_DOS_DADOS, nome_arquivo)


def ler_arquivos():
    caminho_arquivo = criar_caminho_arquivo('1_demografico.csv')
    return pd.read_csv(caminho_arquivo, sep=';')
