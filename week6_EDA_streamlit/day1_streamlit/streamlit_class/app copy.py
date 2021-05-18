# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

from PIL import Image
import os
from utils.stream_config import  draw_map
from utils.dataframes import load_csv_for_map, load_normal_csv

path = os.path.dirname(__file__) #accedo a los archivos de la carpeta 
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenida", "Analizador", "Mapa con Globos"]) 

if menu == 'Bienvenida': 
    st.title('Bienvenido al bootcapm de The Bridge')
    st.write('es un placer tenerte por aqui!') 

if menu == 'analizador': 
    #cargar csv
    slider_csv = st.sidebar.file_uploader("seleccione un CSV", type=['csv']) 
    #cargar el dataframe  
    if type(slider_csv) != type(None): #si alguien ha subido un archivo csv carga el dataframe
            filtro_edades = st.sidebar.checkbox("Filtrar edades") #poner un filtro en el sidebar
            df_slider = load_csv_df(slider_csv) 
            if filtro_edades:
                df_slider = df_slider [df_slider["age"]<10] #para filtrar la edad  con una mascara y que me salga el grafico y la tabla
                st.bar_chart(df_slider) # grafico de barras para cada una de las columnas
                st.table(df_slider) #esta cargado y con esto se linea 
            else:
                st.bar_chart(df_slider) # grafico de barras para cada una de las columnas
                st.table(df_slider) #esta cargado y con esto se linea 
if menu == 'Mapa con Globos': 
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path) # cargamos formula de aqui, que nos ayuda a leer un archivo con la separacion que tiene que son dos puntos y nombrar dos columnas que estan mas nombradas       
    draw_map(df_map)   #pasa a una funcion con un zoom especifico
        
 