from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Yuupiii, Flask!"

app.run(port=8080,debug=True)