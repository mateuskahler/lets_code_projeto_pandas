
def separar_top10(input_df, ref_col):
    df = input_df.copy()
    df.sort_values(by=ref_col, ascending=False, inplace=True)
    quant_amostras = int(df.shape[0]*0.1)
    return df.head(quant_amostras)

def salvar_top10(input_df, ref_col, filename):
    df_top10 = separar_top10(input_df, ref_col)
    df_top10.to_csv(filename)
    return df_top10
