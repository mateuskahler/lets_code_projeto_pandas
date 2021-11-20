
import pandas as pd

def criar_dummies(input_df, colunas, df_completo=False):
    '''
    Parametros:
        input_df (dataframe): dataframe de entrada
        colunas (list): lista com os nomes das colunas para criar dummies
        df_completo: quando False, retorna apenas as colunas dummies criadas,
            quando True, retorna o dataframe completo com as colunas dummies
    
    Retorno:
        df_dummies (dataframe): dataframe com colunas dummies
    '''
    df = input_df.copy()
    
    if df_completo == False:
        df_dummies = pd.get_dummies(df[colunas])
    elif df_completo == True:
        df.drop(colunas, axis=1)
        df_dummies = df.merge(pd.get_dummies(df[colunas]), left_index=True, right_index=True)
    
    return df_dummies
