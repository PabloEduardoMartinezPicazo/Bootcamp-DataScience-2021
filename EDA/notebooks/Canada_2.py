#los archivos con un 2  son las que indican los periodos antes y despues de los respectivos acuerdos. 
import pandas as pd
import numpy as np
import sys, os
path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from SRC.utils_.mining_data_tb import*

url = "//data//exportacionescanada.csv"
url2 = "//data//importacioncanada.csv"

df_canada1 = limpieza_top(url,url2,path,"Canadá")
df_canada1 = Trabajito_canada (df_canada1)
limpio_csv(df_canada1,"Canadá1")
print(df_canada1)
