import pandas as pd
from datetime import datetime
import polars as pl 
import os
import gc
try:
    # pandas 01:21
    # polars 00.32
    ENDERECO_DADOS = r'./dados/'
    hr_import = datetime.now()
    lista_arquivos= []
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    
    for arquivo in lista_dir_arquivos:
        
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
        # print(df.shape()) imprime corpo
        # print(df.columns()) imprime coluna
        # print(df.dtypes()) tipos
    
    for arquivo in lista_arquivos:
        print(f'Processando arquivos {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo,separator=';',encoding='iso-8859-1')

        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia])
        else:
            df_bolsa_familia = df
        
        del df
        
        print(df_bolsa_familia.head())

        df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        del df_bolsa_familia
        
        gc.collect()


    hora_impressao= datetime.now()
    print(f'Tempo de execução: {hora_impressao - hr_import}')
except ImportError as e:
    print('Erro ao obter dados:', e)