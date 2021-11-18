from collections import namedtuple
from pandas import DataFrame, Series


def _frequencia(serie: Series, relativa: bool, acumulada: bool) -> Series:
    contagem = serie.value_counts(normalize=relativa).sort_index()

    if acumulada:
        # todo
        pass

    return contagem


AnaliseQualitativa = namedtuple('AnaliseQualitativa', ['nome', 'dados'])


class AnalisesDeVariavelQualitativa:
    def __init__(self, dados: DataFrame, nome_da_variavel: str):
        self.nome_da_variavel = nome_da_variavel
        coluna = dados[nome_da_variavel]

        self.analises = [
            _frequencia_absoluta(coluna),
            _frequencia_absoluta_acumulada(coluna),
            _frequencia_relativa(coluna),
            _frequencia_relativa_acumulada(coluna),
        ]


def _frequencia_absoluta(serie: Series) -> AnaliseQualitativa:
    dados = _frequencia(serie, relativa=False, acumulada=False)

    return AnaliseQualitativa('Frequência Absoluta', dados)


def _frequencia_absoluta_acumulada(serie: Series) -> AnaliseQualitativa:
    dados = _frequencia(serie, relativa=False, acumulada=True)

    return AnaliseQualitativa('Frequência Absoluta Acumulada', dados)


def _frequencia_relativa(serie: Series) -> AnaliseQualitativa:
    dados = _frequencia(serie, relativa=True, acumulada=False)

    return AnaliseQualitativa('Frequência Relativa', dados)


def _frequencia_relativa_acumulada(serie: Series) -> AnaliseQualitativa:
    dados = _frequencia(serie, relativa=True, acumulada=True)

    return AnaliseQualitativa('Frequência Relativa Acumulada', dados)


def _nomes_colunas_qualitativas(df: DataFrame) -> list[str]:
    """
    Retorna lista com nome das colunas que possuem variáveis qualitativas
    """
    # nos dados fornecidos, colunas do tipo "object" contém as variáveis qualitativas
    return list(df.select_dtypes(['object']).columns)


def analisar_variaveis_qualitativas(dados: DataFrame):
    colunas_qualitativas = _nomes_colunas_qualitativas(dados)
    analises = [AnalisesDeVariavelQualitativa(
        dados, coluna) for coluna in colunas_qualitativas]

    return analises
