
from flask import Flask

from doctors import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Use /doctor/:id'

@app.route("/doctor/<id>") # Ай как мне хотелось тут написать /doctor/:id
def doctor(id):
    result = doctors_find_by_id(id)

    if result:
        return result
    else:
        return "Not found"

if __name__ == "__main__":
    app.run()
