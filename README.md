# Introduction to flask

# Desenvolvimento de sites em flask

https://www.reddit.com/r/flask/comments/8zg0rn/flask_apppy_and_dash/

https://github.com/mbkupfer/dash-with-flask

Exemplo em c:\dropbox\dev\dashFlask

# Flask

Para instalar:
```
	conda install -c anaconda flask 
```
# Olá mundo em Flask
Create a file in python (app.py) ver exemplo em [aqui](1.olaMundo/app.py)
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Yuupiii, Flask!"

app.run(port=8080,debug=True)
```


Colocar um site para ver os dados analizados pela aplicação e gerir a plataform. Temos uma estrutura para um site em Flask [aqui](https://github.com/JackStouffer/Flask-Foundation) e um [tutorial](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.WjUfYPbLi00). Um site com vários tutoriais sobre [Flask](https://www.fullstackpython.com/flask.html).
