import pandas as pd
from datetime import datetime
import polars as pl 
try:
    ENDERECO_DADOS = r'./dados/'
    hr_import = datetime.now()
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv', separator=';',encoding='iso-8859-1')
    print(df_janeiro)
    hora_impressao= datetime.now()
    print(f'Tempo de execução: {hora_impressao - hr_import}')
except ImportError as e:
    print('Erro ao obter dados:', e)

