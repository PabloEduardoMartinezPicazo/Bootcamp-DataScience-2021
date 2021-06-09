#totales japon
import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *

url = "//data//exportacionjapon.csv"
url2 = "//data//importacionjapon.csv"
df_japon = limpieza_top(url,url2,path,"Japón")
limpio_csv(df_japon,"Japón")
print(df_japon)

