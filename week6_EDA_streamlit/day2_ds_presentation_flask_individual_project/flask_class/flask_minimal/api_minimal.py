#STATIC Y TEMPLATES TIENEN QUE ESTAR SI O SI LAS CARPETASA DIGO
from flask import Flask, flash, request, render_template, redirect, url_for
import pandas as pd
import os
import json
#este primer grupo es obligatorio para hacerlo
UPLOAD_FOLDER = os.sep + "static" + os.sep #una barra una carpeta static y una barra static es la carpeta donde se apuinta
#hay que llamar la clase flask y pasarle el atributo __name__
app = Flask(__name__)  #se pone name pero es sinonimo de __main 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #los archivos que se vayan a subir esten en la carpeta static
app.secret_key = 'hellohello' #atributo obligatorio para interactuar con la api solo lo sabemos nosotors 


#logica del fichero
options = {"Genre_list":["hola", "adios"], 
"Platform_list":[1,2,3,4,5,6],
"Publisher_list":['Clara', 'Borja', 'Gabriel']} #diccionario con varias cosas 

@app.route("/") #desde la pagina web para acceder desde la pagina web. app.route sera la primera que se va a mostrar cuando ponga la direccion de la appi

def home():
    return render_template("upload.html", 
                           Genre_list = options["Genre_list"],
                           Platform_list= options["Platform_list"], 
                           Publisher_list= options["Publisher_list"]) #poner a este archivo upload.html que esta en la carpeta templates se va a html los valores de option
    
@app.route("/upload_form", methods = ['POST', 'GET']) #aqui se sube el archivo caund ose da a envair en cualquier sitio, siempre que damos a enviar algo en una pagina estamos haciendo un post 
def upload_form():
    if request.method == 'POST': #request es importado de flask
        genre_res = request.form['Genre'] #creas un atributo que tiene el valor de request.form y la clave genre 
        platform_res= request.form['Platform'] #le pasamos los valores a upload.html
        publisher_res = request.form['Publisher']
        all_returned = str(genre_res) + str(platform_res) + str(publisher_res) #concatenacion de todo 
        return json.dumps({"genre": genre_res,
                            "platform": platform_res,
                            "publisher": publisher_res,
                            "all_returned": all_returned}) #diccionario transformado a json ponemos los valores seleccionados 

if __name__ == '__main__': #si estoy ejecutando este archivo, vamos a ejectuar la linea de codigo infeerior
    # host='127.0.0.1' --> No permite recibir llamadas desde el exterior PRIVADO
    # host='0.0.0.0' --> Permite recibir llamadas desde el exterior PUBLICO
    # si 0.0.0.0 no funciona externamente desde la IP privada de tu PC
    # es que tu ordenador o del dispositivo desde el que se accede 
    # tiene bloqueada la conexión (antivirus / firewall) -> si no funcionan es por esto
    app.run(host='0.0.0.0',port=os.getenv("PORT", 6060), debug=True) #app es la instancia de la clase que hemos creado, le decimos cual es el host es 0.0.0.0 y puerto 1991 
    #con 0.0.0.0 es hacer el ordenador publico
    #accedemos con el local host con la ip privada 