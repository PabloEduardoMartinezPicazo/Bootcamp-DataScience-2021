#totales canada
import pandas as pd
import numpy as np
import sys, os
path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from SRC.utils_.mining_data_tb import*

url = "//data//exportacionescanada.csv"
url2 = "//data//importacioncanada.csv"

df_canada = limpieza_top(url,url2,path,"Canadá")
limpio_csv(df_canada,"Canadá")
print(df_canada)
