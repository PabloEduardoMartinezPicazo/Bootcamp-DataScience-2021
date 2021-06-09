#funciones de limpieza de los diferentes dataframes 
import sys,os 
import pandas as pd
import numpy as np

#funciones de ordenado, limpieza, transformacion de variables y definicion de nuevas columnas
def limpieza_top (url,url2,path,pais):  
    df = pd.read_csv(path + url, sep=";", header=1).astype(str)
    df1=pd.read_csv(path + url2, sep=";",header=1).astype(str)
    df,df1=df.iloc[2:,0:-1],df1.iloc[2:,0:-1]
    df,df1=df.rename({"Unnamed: 0":"Tarics"},axis="columns"), df1.rename({"Unnamed: 0":"Tarics"},axis="columns")
    df=df.melt(id_vars=["Tarics"], 
            var_name="Año", 
            value_name="Exportaciones") 
    df=df.applymap(lambda x: x.replace('.',"").replace(',',"."))
    df1=df1.melt(id_vars=["Tarics"], 
            var_name="Año", 
            value_name="Importaciones")
    df1=df1.applymap(lambda x: x.replace('.',"").replace(',',"."))
    if "Exportaciones" in df.columns:
        descrip=15*["Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos","Productos cárnicos", "Pescados y mariscos","Pescados y mariscos","Pescados y mariscos","Pescados y mariscos","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Verduras y hortalizas","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Frutas y frutos secos","Cereales y harinas","Cereales y harinas","Cereales y harinas","Cereales y harinas","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Huevos, productos lácteos y miel","Aceites","Aceites","Aceites","Bebidas","Bebidas","Bebidas","Bebidas","Bebidas","Bebidas","Bebidas","Chocolates","Chocolates","Chocolates","Panaderia y pastelería"]
        df=arreglitos(df,pais=pais,descrip=descrip)
        
    df["Importaciones"]=df1["Importaciones"] 
    return df
#ultimos arreglos necesarios para obtener los dataset tal cual se desean
def arreglitos(df,pais,descrip):
    df["País"]=pais
    df.insert(2,"Descripción",descrip)
    for pos,value in enumerate(df["Tarics"]):
        df["Tarics"][pos]=df["Tarics"][pos][0:4]
    df=df[["País","Tarics","Descripción","Año","Exportaciones"]]
    return df
#esta funcion es la que da como resutlado el dataframe madre
def transformacion (df1,df2,df3,df4,df5):
    df_paises=pd.concat([df1,df2,df3,df4,df5])
    df_paises[["Exportaciones","Importaciones"]] = df_paises[["Exportaciones","Importaciones"]].replace({'nan': np.nan})
    df_paises[["Exportaciones","Importaciones"]]=df_paises[["Exportaciones","Importaciones"]].apply(pd.to_numeric)
    df_paises=df_paises.dropna(subset=["Exportaciones", "Importaciones"], how='all')
    df_paises.reset_index(drop=True)
    df_paises=df_paises.groupby(['País',"Año"]).sum()
    return df_paises
#las funciones trabajito son diferentes porque tienen mascaras diferentes para poder obtener las filas deseadas
def Trabajito_corea (df):
    mask = (df['Año'] == "2011") | (df['Año'] == "2020")
    df=df[mask]
    df[["Exportaciones","Importaciones"]] = df[["Exportaciones","Importaciones"]].replace({'nan': np.nan})

    df[["Exportaciones","Importaciones"]]=df[["Exportaciones","Importaciones"]].apply(pd.to_numeric)
    df=df.groupby(["Descripción", "Año"]).sum()
    df=df.reset_index()

    return df
def Trabajito_japon (df):
    mask = (df['Año'] == "2018") | (df['Año'] == "2020")
    df=df[mask]
    df[["Exportaciones","Importaciones"]] = df[["Exportaciones","Importaciones"]].replace({'nan': np.nan})

    df[["Exportaciones","Importaciones"]]=df[["Exportaciones","Importaciones"]].apply(pd.to_numeric)
    df=df.groupby(["Descripción", "Año"]).sum()
    df=df.reset_index()

    return df

def Trabajito_canada (df):
    mask = (df['Año'] == "2014") | (df['Año'] == "2020")
    df=df[mask]
    df[["Exportaciones","Importaciones"]] = df[["Exportaciones","Importaciones"]].replace({'nan': np.nan})

    df[["Exportaciones","Importaciones"]]=df[["Exportaciones","Importaciones"]].apply(pd.to_numeric)
    df=df.groupby(["Descripción", "Año"]).sum()
    df=df.reset_index()

    return df
#guardar el csv 
def limpio_csv(x,pais):
    dirs = os.path.dirname
    return x.to_csv(dirs(dirs(dirs(__file__))) + os.sep + "data" + os.sep + (f"csvlimpio{pais}.csv"),index=False)

