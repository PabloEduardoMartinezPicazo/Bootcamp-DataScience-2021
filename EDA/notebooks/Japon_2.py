#los archivos con un 2  son las que indican los periodos antes y despues de los respectivos acuerdos. 

import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *

url = "//data//exportacionjapon.csv"
url2 = "//data//importacionjapon.csv"
df_japon1 = limpieza_top(url,url2,path,"Japón")
df_japon1 = Trabajito_japon(df_japon1)

limpio_csv(df_japon1,"Japón1")

print(df_japon1)

