import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import sys,os


pato = os.path.dirname
direccion=pato(pato(pato(__file__)))
sys.path.append(direccion)
from notebooks.Canada import df_canada
from notebooks.Canada_2 import df_canada1
from notebooks.Japon import df_japon
from notebooks.Japon_2 import df_japon1
from notebooks.Vietnam import df_vietnam
from notebooks.Singapur import df_singapur
from notebooks.Corea import df_corea
from notebooks.Corea_aranceles import df_corea1
from notebooks.paisesfinal import df_paises
from notebooks.Aranceles import aranceles
from SRC.utils_.mining_data_tb import *
from SRC.utils_.visualization_tb import *

df = None
st.set_page_config(layout="wide") 
menu = st.sidebar.selectbox('Menu:',
            options=["Portada", "Informacion básica", "Casos de estudio", "DataFrames","El datamama","Conclusiones","Información"])

st.title(' La importancia de los acuerdos comerciales internacionales')


if menu == 'Portada':
    st.markdown('### En este estudio se pretende refutar la importancia de los acuerdos comerciales internacionales para el comercio de la Unión Europea.')
    st.write('¿Los acuerdos comerciales ayudan al comercio de la Unión Europea?: **SI**')
    st.markdown ("###### Fuentes: Comisión Europea, Datacomex, Eurostacom, ICEX y Access2Markets.")
    st.markdown('### Exportaciones UE - País / Importaciones País - UE')
    grafico1 = Image.open(direccion + os.sep + 'resources' + os.sep + 'imp_exp_total.png')
    st.image (grafico1,use_column_width=True) 
    st.markdown('### Importaciones UE - País')
    grafico2 = Image.open(direccion + os.sep + 'resources' + os.sep + 'imp_totales.png')
    st.image (grafico2,use_column_width=True) 
    st.markdown('### Exportaciones País - UE')
    grafico3 = Image.open(direccion + os.sep + 'resources' + os.sep + 'exp_totales.png')
    st.image (grafico3,use_column_width=True) 
if menu == "Informacion básica":
    st.markdown('## Definiciones')
    st.write ("1. **Acuerdo libre comercio:** acuerdo firmado por uno o varios países que lo que pretenden es mejorar el comercio entre ambos bloques a través de la eliminación de trabas arancelarias y no arancelarias.")
    st.write ("2. **Barreras no arancelarias:** aquellas que impiden el correcto comercio entre dos bloques económicos y que no son de índole arancelario. Entre ellas se encuentras los procedimiento de entrada, los procesos de registro del producto, de inspeccion sanitaria, etc.")
    st.write ("3. **Aranceles:** impuestos que se cobran por la entrada de bienes o servicios extranjeros en el mercado nacional de un determinado país.")
    st.write ("4. **Existen dos tipos de aranceles:** aplicados como un porcentaje del valor del bien o los que se les aplica un valor fijo por una unidad de medida establecida (por ejemplo una cantidad de toneladas, hectolitros, etc.)")
    st.write ("5. **Contingentes:** cantidad exenta de aranceles o a la que se le aplica un arancel menor. A partir de ese volumen los aranceles aumentan.")
    st.write ("6. **Clasificación arancelaria:** proceso por el que se asigna a cada mercancía un código numérico basado en ciertos criterios como son la naturaleza del producto o los países de origen y destino.")
    st.write ("7. **Taric:** clasificación arancelario usado por la Unión Europea.")
if menu == "Casos de estudio":
    submenu=st.sidebar.selectbox(label="País:",
            options=["Corea del Sur","Japón","Canadá"])
    if submenu=="Corea del Sur":
        st.markdown('## El caso coreano: reacción inmediata ')
        checkbox_graficas = st.sidebar.checkbox("Gráficas", value=True)
        checkbox_correlaciones = st.sidebar.checkbox("Correlaciones", value=True)

        if checkbox_graficas:
            
            st.write("Aumento en las exportaciones e importaciones de un **72,26%** y un **105,76%**, respectivamente. ")
            st.write ("Reducción de los aranceles: ")
            st.write ("- Reduccion mediana de las importaciones del 27% al 5%. ")
            st.write ("- Reduccion mediana de las exportaciones del 14% al 0%. ")
            col1, col2 = st.beta_columns(2)
            with col1: 
                st.markdown('### Importaciones de Corea del Sur a la Unión Europea ')
                st.plotly_chart(importaciones_total(df_corea1,"Corea del Sur"),use_container_width=True)    
            with col2:
                st.markdown('### Exportaciones de Corea del Sur a la Unión Europea ')
                st.plotly_chart(exportaciones_total(df_corea1,"Corea del Sur"),use_container_width=True)
        if checkbox_correlaciones:
            
            col1, col2 = st.beta_columns(2)
            with col1:
                st.markdown('### Aranceles 2011 ')
                st.plotly_chart(violin_pre(aranceles),use_container_width=True)    
            with col2:
                st.markdown('### Aranceles 2020 ')
                st.plotly_chart(violin_post(aranceles),use_container_width=True)
    if submenu=="Japón":
        
        st.markdown('## El caso japonés: la larga marcha ')
        st.write ("Disminución en las exportaciones de un **-3,35%** y un aumento el **27,72%** de las importaciones.")
        col1, col2 = st.beta_columns(2)
        with col1: 
            st.markdown('### Importaciones de Japón a la Unión Europea ')
            st.plotly_chart(importaciones_total(df_japon1,"Japón"),use_container_width=True)    
        with col2:
            st.markdown('### Exportaciones de Japón a la Unión Europea ')
            st.plotly_chart(exportaciones_total(df_japon1,"Japón"),use_container_width=True)
    if submenu=="Canadá":
        st.markdown('## El caso canadiense: con x de mixta')
        st.write ("Aumento en las exportaciones e importaciones de un **41,59%** y un **141,80%**, respectivamente.")

        col1, col2 = st.beta_columns(2)
        with col1: 
            st.markdown('### Importaciones de Canadá a la Unión Europea ')
            st.plotly_chart(importaciones_total(df_canada1,"Canadá"),use_container_width=False)    
        with col2:
            st.markdown('### Exportaciones de Canadá a la Unión Europea ')
            st.plotly_chart(exportaciones_total(df_canada1,"Canadá"),use_container_width=False)

if menu == "DataFrames":
    submenu=st.sidebar.selectbox(label="País:",
            options=["Canadá","Corea del Sur","Japón","Singapur","Vietnam"])
    if submenu=="Canadá":
        col1, col2 = st.beta_columns(2)
        with col1:
            st.markdown('### Datos antes y despues acuerdo ')
            df1 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioCanadá1.csv",nrows=20)
            st.table(df1)
        with col2:
            st.markdown('### Datos completos')
            df = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioCanadá.csv",nrows=20)
            st.table(df)
    if submenu=="Corea del Sur":
        st.markdown('### Datos antes y despues acuerdo ')
        df2 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioCorea_del_Sur_1.csv",nrows=50)
        st.table(df2)
    if submenu=="Japón":
        
        col1, col2 = st.beta_columns(2)
        with col1: 
            st.markdown('### Datos antes y despues acuerdo ')
            df3 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioJapón1.csv",nrows=50)
            st.table(df3)
        with col2:
            st.markdown('### Datos completos')
            df4 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioJapón.csv",nrows=50)
            st.table(df4)   
    if submenu=="Singapur":
        st.markdown('### Datos completos')
        df3 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioSingapur.csv",nrows=50)
        st.table(df3)
    if submenu=="Vietnam":
        st.markdown('### Datos completos')
        df3 = pd.read_csv(direccion + os.sep + 'data' + os.sep + "csvlimpioVietnam.csv",nrows=50)
        st.table(df3)


if menu == "El datamama":
    r = requests.get("http://localhost:8080/give_me_id?token_id=R70423563").json()
    df = pd.DataFrame(r)
    st.write(df)
if menu == "Conclusiones":
    st.markdown('## Conclusiones')
    st.write ("- Todos los tipos de acuerdos comerciales desde aquellos que son más ambiciosos hasta aquellos que son más conservadores ayudan a mejorar el comercio internacional.")
    st.write ("- La correlación entre las exportaciones e importaciones con respecto a los aranceles es inversa.")
    st.write ("- A mayor rapidez en la implantacion mayor aumento en el comercio internacional.")
    st.write ("- Las barreras arancelarias tienen un peso muy importante en el aumento o disminucion del comercio.")
    st.write ("- La comparación entre los países que han adpotado las medidas hace más tiempo y los que las han adoptado hace menos indica que el comercio entre los diferentes bloques se incrementa mucho más tras los acuerdos ")
    st.write ("- Las economías con mayor apertura comercial tienden a ser más dependientes del sector exterior que las economias protectoras.")
    st.write ("- Importante remarcar que hay una serie de variables no númericas (barreras no arancelarias) que tienen un gran impacto en el comercio, habría que hacer un análisis más profundo.")
if menu == "Información":
    st.markdown("### Para más información:")
    st.write(" 1. [Linkedin](https://www.linkedin.com/in/pabloeduardomartinezpicazo/)")
    st.write(" 2. Correo electónico: pabloeduardo.martinezpicazo@gmail.com")
    Imagen_despedida= Image.open(direccion + os.sep + 'resources' + os.sep + 'agradecimiento.jpg')
    st.image (Imagen_despedida,use_column_width=True) 