# ------- Import the necessary libraries -------
from flask import Flask, request, render_template
import os,sys
import argparse
import json

# Access to the folder and append the path
dir = os.path.dirname
src_path = dir(dir(__file__))
sys.path.append(src_path)

# ------ Import functions from apis_tb ------
from utils_.apis_tb import *

# ------ Create Flask ------
app = Flask(__name__)

@app.route("/") 
def home():
    """ Default path """
    return "Hola soy Pablo"

@app.route('/give_me_id', methods=['GET']) # localhost:8080/give_me_id?token_id=70423563R
def give_id():
    x = request.args['token_id']
    if x == "R70423563": 
        return return_json(dir(dir(dir(__file__))) + os.sep + "data" + os.sep + "csvlimpiototal.csv")
    else:
        return "Wrong password"

def main():
    
    settings_file = os.path.dirname(__file__) + os.sep + "jason.json"
    
    # Load json from file
    json_readed = read_json(fullpath=settings_file)

    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"] 

    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int, help="password")

if __name__ == "__main__":
    args = vars(parser.parse_args())
    print(args.values())
    if args["x"] == 8642: 
        main()
    else:
        print("wrong password")
