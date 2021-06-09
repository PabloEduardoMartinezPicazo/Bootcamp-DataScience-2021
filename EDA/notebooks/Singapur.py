#totales singapur
import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *
url = "//data//exportacionsingapur.csv"
url2 = "//data//importacionsingapur.csv"
df_singapur = limpieza_top(url,url2,path,"Singapur")
limpio_csv(df_singapur,"Singapur")
print(df_singapur)
