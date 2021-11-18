
def criar_dummies(input_df, colunas, df_completo=False):
    df = input_df.copy()
    
    if retornar_completo == False:
        df_dummies = pd.get_dummies(df[colunas])
    elif retornar_completo == True:
        df.drop(colunas, axis=1)
        df_dummies = df.merge(pd.get_dummies(df[colunas]), left_index=True, right_index=True)
    
    return df_dummies
