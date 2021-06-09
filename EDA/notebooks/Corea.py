#totales corea
import pandas as pd 
import numpy as np
import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *

url = "\\data\\exportacioncorea.csv"
url2 = "\\data\\importacionescorea.csv"

df_corea = limpieza_top(url,url2,path,"Corea del Sur")
limpio_csv(df_corea,"Corea_del_Sur")
print(df_corea)

