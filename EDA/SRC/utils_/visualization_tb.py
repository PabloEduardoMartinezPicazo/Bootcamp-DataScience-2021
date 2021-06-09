import pandas as pd
import numpy as np
import sys,os
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#graficas para ver las expor e impor de los 3 paises analizados (japon, corea y canada) ya que singapur y vietnam son descartados despues de este proceso
def exportaciones_total (df,pais):
    dirs = os.path.dirname
    Variacion_expo = px.bar(df, x="Descripción", color="Año",
                y='Exportaciones',
                title=(f'Variación de las exportaciones {pais} (€)'),
                barmode='group',
                height=600)
    Variacion_expo.write_html(dirs(dirs(dirs(__file__))) + os.sep + "resources" + os.sep + (f"exportacion_total{pais}.html"))
    
    return Variacion_expo
    
def importaciones_total (df,pais):
    dirs = os.path.dirname
    Variacion_imp = px.bar(df, x="Descripción", color="Año",
                y='Importaciones',
                title=(f'Variación de las importaciones {pais} (€)'),
                barmode='group',
                height=600)
    Variacion_imp.write_html(dirs(dirs(dirs(__file__))) + os.sep + "resources" + os.sep + (f"importacion_total{pais}.html"))
    return Variacion_imp
#valores totales de exp e imp
def totalitos(df):
    fig,ax=plt.subplots(1,figsize=(30,10),sharey=True)

    ax=sns.lineplot(x=df['Año'], y=df.Exportaciones, data=df,hue="País",marker="s", linestyle="-.",linewidth=3.0)
    ax.legend(title="Países",loc="upper left")
    ax.set_xlabel("Año",fontsize=14)
    ax.set_ylabel("Exportaciones EU - País",color="red",fontsize=14)
    ax2=ax.twinx()
    ax2=sns.lineplot(x=df['Año'], y=df.Importaciones,data=df,hue="País",marker="o", linestyle="-",linewidth=3.0,legend=False,)


    ax2.set_ylabel("Importaciones País - EU",color="blue",fontsize=14)
    
    return fig



    plt.show()
def exportaciones_totalitos (df):
    fig,ax1=plt.subplots(1,figsize=(30,10),sharey=True)
    ax1 = sns.lineplot(x=df["Año"], y=df.Exportaciones, data=df,hue="País",ax=ax1,marker="s", linestyle="-",linewidth=3.0)
    ax1.legend(title="Países",loc="upper left")
    ax1.set_xlabel("Año",fontsize=14)
    ax1.set_ylabel("Exportaciones",color="red",fontsize=14)
    plt.xlim(0)
    return fig
    

def importaciones_totalitos (df):
    fig,ax2=plt.subplots(1,figsize=(30,10),sharey=True)
    ax2 = sns.lineplot(x=df.Año, y=df.Importaciones, data=df,hue="País",ax=ax2,marker="s", linestyle="-",linewidth=3.0)
    ax2.legend(title="Países",loc="upper left")
    ax2.set_xlabel("Año",fontsize=14)
    ax2.set_ylabel("Importaciones",color="red",fontsize=14)
    plt.xlim(0)
    return fig
#graficos de violin distribucion aranceles
def violin_pre(df):
    dirs = os.path.dirname
    fig = go.Figure()
    fig.add_trace(go.Violin(x=df['Aranceles pre UE'],
                            
                            legendgroup='Aranceles pre UE', scalegroup='Yes', name='Aranceles pre UE',
                            side='negative',
                            line_color='blue'))
    fig.add_trace(go.Violin(x=df['Aranceles pre Corea'],
                            legendgroup='Aranceles pre Corea', scalegroup='No', name='Aranceles pre Corea',
                            side='negative',
                            line_color='orange'))
    fig.update_traces(meanline_visible=True)
    fig.update_layout(violingap=0, violinmode='overlay')
    fig.write_html(dirs(dirs(dirs(__file__))) + os.sep + "resources" + os.sep + (f"violin_pre.html"))
    return fig

def violin_post (df):
    dirs = os.path.dirname
    fig = go.Figure()
    fig.add_trace(go.Violin(x=df['Aranceles post UE'],
                        
                        legendgroup='Aranceles post UE', scalegroup='Yes', name='Aranceles post UE',
                        side='negative',
                        line_color='blue'))
    fig.add_trace(go.Violin(x=df['Aranceles post Corea'],
                            legendgroup='Aranceles post Corea', scalegroup='No', name='Aranceles post Corea',
                            side='negative',
                            line_color='orange'))
    fig.update_traces(meanline_visible=True)
    fig.update_layout(violingap=0, violinmode='overlay')
    fig.write_html(dirs(dirs(dirs(__file__))) + os.sep + "resources" + os.sep + (f"violin_post.html"))
    return fig

def horitas (array):
    plt.pie(array,labels=["Búsqueda info","Limpieza de datos","Creación funciones","Importar a main","Creación gráficas","Flask","Streamlit","Presentación"])
    plt.legend(title = "Horas invertidas:",bbox_to_anchor=(1,0))
    plt.show() 
def grafico_t_columnas_num(df,pais):
    dirs = os.path.dirname
    df.hist(figsize=(20, 20))
    plt.show()
    plt.savefig(dirs(dirs(dirs(__file__))) + os.sep + "resources" + os.sep + (f"histnumerics{pais}.jpg"))
