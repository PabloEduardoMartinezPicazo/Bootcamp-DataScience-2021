#este dataframe muestra no solo los periodos antes y despues del acuerdo, si no tambien nos aranceles previos  y posteriores y la variacion de las exp e imp
import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from SRC.utils_.mining_data_tb import *


url = "\\data\\exportacioncorea.csv"
url2 = "\\data\\importacionescorea.csv"

df_corea1 = limpieza_top(url,url2,path,"Corea del Sur")
df_corea1 = Trabajito_corea(df_corea1)

df_corea1["Aranceles Corea - UE"]=[10,0,20,3,335,10,10,5,50,7.5,30,8,35,8,17,7,22.5,8.5,27,7.5]
df_corea1["Aranceles UE - Corea"] = [8,0,13.5,0,150,0,8.5,5,18,5,8,4,15,5,9,3,10,4,15,6.5]
df_corea1["Cambio Exportaciones (%)"]=[0,58,0,58,0,280,0,-4,0,200,0,120,0,90,0,351,0,55,0,165]
df_corea1["Cambio Importaciones (%)"]=[0,738,0,125,0,29,0,0,0,-34,0,3335,0,432,0,93,0,-48,0,161]
limpio_csv(df_corea1,"Corea_del_Sur_1")
print(df_corea1)

