from flask import Flask
from datetime import datetime
import re
app = Flask(__name__)

@app.route('/')
def home():
    return "Yuupiii, Flask!"
'''
Vamos adicionar uma nova rota para ser tratada. <name> define
um novo destino que permite utilizar um valor adicional
'''
@app.route("/nome/<nome>")
def hello_there(nome):
    now = datetime.now()

    content = "Olá, " + nome + "! It's " + str(now)
    return content

app.run(port=8080, debug=True)  