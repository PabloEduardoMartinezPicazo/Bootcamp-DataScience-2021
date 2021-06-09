#totales vietnam
import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *

url = "//data//exportacionvietnam.csv"
url2 = "//data//importacionvietnam.csv"

df_vietnam = limpieza_top(url,url2,path,"Vietnam")
limpio_csv(df_vietnam,"Vietnam")
print(df_vietnam)

