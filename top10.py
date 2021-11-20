
def separar_top10(input_df, ref_col):
    '''
    Parametros:
        input_df (dataframe): dataframe de entrada
        ref_col (str): nome da coluna de referência para classificação
    
    Retorno:
        df_top10 (dataframe): dataframe com top 10%
    '''
    df = input_df.copy()
    df.sort_values(by=ref_col, ascending=False, inplace=True)
    # quantidade de amostras referente a 10% do dataframe
    quant_amostras = int(df.shape[0]*0.1)
    df_top10 = df.head(quant_amostras)
    return df_top10

def salvar_top10(input_df, ref_col, filename):
    '''
    Parametros:
        input_df (dataframe): dataframe de entrada
        ref_col (str): nome da coluna de referência para classificação
        filename (str): nome do arquivo de saída
    
    Retorno:
        df_top10 (dataframe): dataframe com top 10% com index resetado 
    '''
    df_top10 = separar_top10(input_df, ref_col)
    df_top10.reset_index(drop=True, inplace=True)
    df_top10.to_csv(filename)
    return df_top10
