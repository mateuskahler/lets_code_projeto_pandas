from collections import namedtuple
from pandas import DataFrame, Series, concat


class AnalisesDeVariavelQualitativa:
    def __init__(self, dados: DataFrame, nome_da_variavel: str):
        self.nome_da_variavel = nome_da_variavel
        coluna = dados[nome_da_variavel]

        self.analise = concat([
            _frequencia_absoluta(coluna),
            _frequencia_absoluta_acumulada(coluna),
            _frequencia_relativa(coluna),
            _frequencia_relativa_acumulada(coluna),
        ], axis=1)


def analisar_variaveis_qualitativas(dados: DataFrame) -> list[AnalisesDeVariavelQualitativa]:
    colunas_qualitativas = _nomes_colunas_qualitativas(dados)

    analises = [AnalisesDeVariavelQualitativa(
        dados, coluna) for coluna in colunas_qualitativas]

    return analises


def _frequencia_absoluta(serie: Series) -> Series:
    resultado = _frequencia(serie, relativa=False, acumulada=False)

    return resultado.rename('Frequência Absoluta')


def _frequencia_absoluta_acumulada(serie: Series) -> Series:
    resultado = _frequencia(serie, relativa=False, acumulada=True)

    return resultado.rename('Frequência Absoluta Acumulada')


def _frequencia_relativa(serie: Series) -> Series:
    resultado = _frequencia(serie, relativa=True, acumulada=False)

    return resultado.rename('Frequência Relativa')


def _frequencia_relativa_acumulada(serie: Series) -> Series:
    resultado = _frequencia(serie, relativa=True, acumulada=True)

    return resultado.rename('Frequência Relativa Acumulada')


def _frequencia(serie: Series, relativa: bool, acumulada: bool) -> Series:
    contagem = serie.value_counts(normalize=relativa).sort_index()

    if acumulada:
        return contagem.cumsum()
    else:
        return contagem


def _nomes_colunas_qualitativas(df: DataFrame) -> list[str]:
    """
    Retorna lista com nome das colunas que possuem variáveis qualitativas
    """
    # nos dados fornecidos, colunas do tipo "object" contém as variáveis qualitativas
    return list(df.select_dtypes(['object']).columns)
