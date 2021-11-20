import pandas as pd

def compara_media_df(df, df_maior_renda):
    ''' 
    Calcula e retorna a média das colunas de 2 data frames
    Entrada: 2 dataframes (caso haja variáveis qualitativas é necessário já ter criado os dummies)
    Retorna: data frame contendo as médias
    '''
    
    df_media_total = df.mean().to_frame(name='Total')
    df_media_decimo = df_maior_renda.mean().to_frame(name='10%_Maior_Renda')

    df_media = df_media_total.join(df_media_decimo, how='left')

    return df_media
