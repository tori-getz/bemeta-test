
from flask import Flask
from flask_cors import CORS

from doctors import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

@app.route('/')
def index():
    return 'Use /doctors'

@app.route("/doctors/")
def doctors():
    return json.dumps(doctors_list())

@app.route("/doctors/<id>") # Ай как мне хотелось тут написать /doctor/:id
def doctors_by_id(id):
    result = doctors_find_by_id(id)

    if result:
        return result
    else:
        return "Not found"

@app.route("/doctors/<id>/<field>")
def doctor_name(id, field):
    result = doctors_find_by_id(id)["fields"][field]
    logger.debug(result)
    return result



if __name__ == "__main__":
    app.run()
