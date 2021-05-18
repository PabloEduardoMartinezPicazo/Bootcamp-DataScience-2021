# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os
from utils.stream_config import create_sliders, draw_map
from utils.dataframes import get_data_from_df, load_csv_df, load_csv_for_map

path = os.path.dirname(__file__) #accedo a los archivos de la carpeta 
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Normal Dataframe", "Load Dataframe Columns", "Graphs", "Map"]) #generamos el menu

st.title('Wine Quality Classifier Web App')
st.write('This is a web app to classify the quality of your wine based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.') #escribir por pantalla 

if menu == 'Normal Dataframe': #si el meno es normal, coge una formula de stream config que crea un diccionario
    features = create_sliders() #barra del lateral
    features_df  = pd.DataFrame([features])
    st.table(features_df)  #creo un datagframe con el diccionario de la formula 
if menu == "Load Dataframe Columns": 
    st.write("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
    col1, col2 = st.beta_columns([2, 4]) #crea dos columnas en la que la izquierda ocupa la mitad de la de la derecha 
    slider_csv = st.sidebar.file_uploader("Select CSV", type=['csv']) #que creemos un slidebar seleccionando un csv
    new_df_path = None
    df_slider = None
    df_writed = None
    with col1: #en la columna de la izquierda 
        image = Image.open(path + os.sep  + 'img' + os.sep + 'happy.jpg') #dentro de la capreta img hay una imagen de img. os.sep es la separacion
        st.image (image,use_column_width=True) #mostrar esa imagen que utilicec todo el tamaño de la columna
        #user_input = st.text_area("label goes here", "Escribe algo") #esto es para escribir algo en un bloque de texto de la pagina
        new_df_path = st.text_input('CSV file path or url') #text imput nos pide un csv
        if new_df_path:
            graph_slider_1 = None
            st.text(str(new_df_path))
            df_writed = pd.read_csv(str(new_df_path)) # nos da una url de una pagina, si lo pegamos en el sitio pequeño nos permite ejecutarlo y que nos eneseñe un dataframe
        if type(df_writed) != type(None): #si el tipo del df existe 
            for i in range(5): st.write("") #escribe 5 saltos de lineas 
            st.table(df_writed) #que nos printee el dataframe
        if st.button('Show values'): #creo un boton, para que muestre los valores, se muestra por debajo porque esta debajo del dataframe
            values = None
            if type(df_writed) == type(pd.DataFrame()): #si el tipo del dataframe es de tipo dataframe, llamo a una funcion de get_date que le paso el parametro dataframe, es una funcion que esta en dataframes, la funcion convierte a array los v alores de las 10 primeras columnas y me los devuelve en array el boton es lo que muestra
                values = get_data_from_df(df_writed) #los muestra en pantalla
            st.write(' Selected  '+ str(values))
        if type(slider_csv) != type(None): #si alguien ha subido un archivo csv
            df_slider = load_csv_df(slider_csv) #cargamos la formula de ultils.dataframe -> la formula dice si el archivo lo cargo y que solo me cargue 200 filas 
            df_writed = None
        if type(df_slider) != type(None): # que me escribas con 6 saltos de linea el dataframe 
            for i in range(6): st.write("")
            st.table(df_slider)  # me lo muestre en una tabla 
    with col2: 
        if type(df_slider) != type(None): # si el dataframe que hemos cargado ahora existe 
            df_slider["inds"] = df_slider["inds"].astype(float) #cambiamos la columna inds a float 
            df_slider["acidez"] = df_slider["acidez"].astype(float) # cambiamos a float
            graph_slider_1 = alt.Chart(df_slider).mark_circle().encode(
            x='inds', y='acidez', size="acidez", color="id") #accedemos a la libreria, y mostrar un chart para hacer circulos y le estamos pasando el dataframe y le decimos que es el eje x y el y y ue tamaño cada uno de los puntos va a estar marcado por el tamaño de la aciden y el color que sea  
            st.write(graph_slider_1) #mostrar por pantalla el grafico
        
        

if menu == "Graphs": # si seleccionamos el tipo grafico
    slider_csv_graph = st.sidebar.file_uploader("Select CSV", type=['csv']) #dar la oportunidad para subir un archivo a la pagina web
    new_df_path_graph = None
    df_slider_graph = None
    df_slider_graph_copy = None
    hidden = None
    c_df_3 = None
    # show grahps

    if st.button('Show Graph'): # que se genere un grafico con columnas aleatorias 
        df_3 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

        c_df_3 = alt.Chart(df_3).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        st.write(c_df_3)
    if type(slider_csv_graph) != type(None):# si hay un tipo de archivo 
        columns = [None,] # que cree una lista 
        df_slider_graph = load_csv_df(slider_csv_graph) # que muestra un grafico de barras del dataframe entero
        st.subheader('DF:')
        st.bar_chart(df_slider_graph)
        tamano = st.sidebar.select_slider("Number of values",
                                      options=range(0, df_slider_graph.shape[0]), # que en la s columnas, te de un rango hasta el maximo de filas 
                                      value=100.0) # va a crear en la parte de la izquierda un sidebar que va a tener el numero de valores con defecto un valor de 100
        columns.extend(list(df_slider_graph.columns)) #que se extienda el grafico con el nombre de columnas 
    
        column_choose = st.sidebar.selectbox(
            'Select a column:',
            options=columns) #creamos un desplegable  con todas las columnas 
        if column_choose != None: # que si el usuaro ha elegido algo
            st.bar_chart(df_slider_graph.head(tamano)[column_choose]) # head muestra los x primero que hayamos elegido en tamaño y de esos accedemos a la columna que el usuario ha elegido

if menu == "Map": #si seleccionamos la opcion map accedemos a un archivo red_recarga balblabla 
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path) #llamo a la funcion que es para cargar un archivo de streamlit
    draw_map(df_map) #dibuja un df cargado y esta definida en stream config y permite acercar o alejar el zoom