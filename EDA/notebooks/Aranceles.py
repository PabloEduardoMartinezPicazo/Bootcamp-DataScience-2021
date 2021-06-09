#he creado este dataframe muy basico y bastante manual porque quería demostrar a través de dos gráficos como se han modificado los aranceles antes y después del acuerdo y como se han movido la mayoría de datos

import pandas as pd 
import numpy as np

import sys,os

path=os.path.dirname(os.path.dirname(__file__))

sys.path.append(path)

from SRC.utils_.mining_data_tb import *

ara={"Aranceles pre Corea":[40,40,22.5,22.5,27,18,20,18,3,25,20,10,20,20,20,304,45,27,27,45,27,27,30,30,30,50,45,45,45,45,45,3,109,505,328,36,176,36,50,89,36,27,8,27,3,10,8,9,30,15,15,15,20,5,5,5,8],"Aranceles pre UE":[13,13,60,13,5,13,26,7,22,70,12,12,18,17,5,12,10,15,11,14,13,11,16,7,16,14,9,15,11,15,17,350,300,250,150,60,0,30,35,45,80,60,45,35,20,13,15,6,0,10,0,15,9,9,10,8,10],"Aranceles post Corea":[15,15,7.5,10,10,15,10,5,0,5,5,5,5,5,5,5,7,0,0,10,5,5,5,7,10,10,5,12,15,7,12,0,3,15,5,15,20,10,0,15,10,10,0,5,0,0,5,0,7,0,10,0,15,0,0,0,5],"Aranceles post UE":[5,5,0,0,0,0,0,0,0,0,5,5,5,5,0,5,5,0,3,0,0,0,0,5,5,7,5,0,5,5,5,0,5,0,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0]}

aranceles=pd.DataFrame(ara)

limpio_csv(aranceles,"Aranceles")

print(aranceles)
