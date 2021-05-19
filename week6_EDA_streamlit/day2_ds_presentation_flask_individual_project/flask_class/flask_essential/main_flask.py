from flask import Flask, request, render_template
from utils.functions import read_json #importa las librerias e importa de utils la funcion read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función ("/") representa la funcion por defecto
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet") #cada una de la funciones que creemos y que sea barra alog son diferentes endpoint para que cualquier persona pueda usarlo
def greet():
    username = request.args.get('name') # va a recoger lo que se escriba como nombre de usuario 
    return render_template('index.html', name=username) # se pasa a index dentro de templates ->y se retorna el valor de index y el nombre de usuario -> hello username

@app.route("/info") #devuelve un string 
def create_json():
    return 'Tienes que acceder al endpoint "/give_me_id" pasando por parámetro "password" con la contraseña correcta' 

@app.route('/give_me_id', methods=['GET']) #llamamos a esta funcion, recoge un parametro password y devuelve un valor 12345
def give_id():
    x = request.args['password'] #te pide la contraseña por pantalla si la das correcta te lo pone en un dic si no te sale error
    if x == "12345":
        return request.args
    else:
        return "No es la contraseña correcta"

# ---------- Other functions ----------

def main(): #si se ejecuta el archivo se ejecutara
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file) #cargamos el fichero desde functions trae ese fichero y lo transofrma en una variable diccionario
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"] #va a hacer referecia al valor de la clave server_running
    print("SERVER_RUNNING", SERVER_RUNNING)
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"] #accedemos a las claves del json
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
            "Please, allow it to run it.")

if __name__ == "__main__":
    main()