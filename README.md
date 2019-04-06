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

# Dash on flask

git clone  https://github.com/okomarov/dash_on_flask.git
cd dash_on_flask
touch .envrc #criar um ficheiro vazio em linux em windows "echo > .envrc"

## Editar o ficheiro .envrc
### Linux
```
export FLASK_APP=dashapp
export FLASK_ENV=development
export DATABASE_URL=sqlite:///$PWD/app.db
export SECRET_KEY=secret_key_change_as_you_wish_make_it_long_123
```

### No windows:
```
set FLASK_APP=dashapp
set FLASK_ENV=development
set DATABASE_URL=sqlite:////users/user/Onedrive - Instituto Politécnico de Santarém/dev/10.SiteFlask/dash_on_flask/db.sqlite
set SECRET_KEY=secret_key_change_as_you_wish_make_it_long_123
```

## Instalar

criar virtual environment
```
conda create -n flask
```
ativar o venv
```
activate flask
```
```
source .envrc
pip install -r requirements.txt #se der erro no certifi - "conda install -c anaconda certifi"

flask db init
flask db migrate -m 'init'
flask db upgrade

flask run
```

## Utilização
### Estrutura
```
.
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── ...
│   └── webapp.py
├── app.db
├── config.py
├── dashapp.py
├── migrations/
│   └── ...
├── .envrc
└── requirements.txt
```
A pasta app contem tudo relacionado com a aplicacao em flask