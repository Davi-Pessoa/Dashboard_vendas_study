from dataset import df  

# Agrupamento por estado e soma da receita

df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

print(df_rec_estado)


#formatação de números

def format_number(value, prefix = ''):
    for unit in ['', ' Mil']:
        if value < 1000:
            return f"{prefix}{value:.2f}{unit}"
        value /= 1000
    return f"{prefix}{value:.2f}Milhões"        