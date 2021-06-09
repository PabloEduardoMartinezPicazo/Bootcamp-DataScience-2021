#dataframe madre con todos los paises, tarics y los 15 años analizados
import pandas as pd

import numpy as np
import sys,os
import seaborn as sns


path = os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *
from notebooks.Canada import df_canada
from notebooks.Japon import df_japon
from notebooks.Vietnam import df_vietnam
from notebooks.Singapur import df_singapur
from notebooks.Corea import df_corea


df_paises = transformacion(df_canada,df_japon,df_vietnam,df_singapur,df_corea)
df_paises=df_paises.reset_index()

print(df_paises)

limpio_csv(df_paises,"total")

