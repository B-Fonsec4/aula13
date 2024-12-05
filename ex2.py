import pandas as pd
from datetime import datetime
import polars as pl 
import gc
try:
    # pandas 01:21
    # polars 00.32
    ENDERECO_DADOS = r'./dados/'
    hr_import = datetime.now()
    lista_arquivos= ['202401_NovoBolsaFamilia.csv','202402_NovoBolsaFamilia.csv']
    for arquivo in lista_arquivos:
        print(f'Processando arquivos {arquivo}')
        df =pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='ISO-8859-1')
        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia])
        else:
            df_bolsa_familia = df
        print(df.head())
        # print(df.shape()) imprime corpo
        # print(df.columns()) imprime coluna
        # print(df.dtypes()) tipos
        del df
        gc.collect()


    hora_impressao= datetime.now()
    print(f'Tempo de execução: {hora_impressao - hr_import}')
except ImportError as e:
    print('Erro ao obter dados:', e)