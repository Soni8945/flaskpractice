from flask import Flask

app = Flask(__name__)

if __name__ == "__main__": 
    app.run(debug=True) 

@app.route("/")
def welcome():
    return "welcome to the flask"

@app.route("/index")
def index():
    return "welcome to the index"
