
from flask import Flask
from flask_cors import CORS

from doctors import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

# Flask очень схож с Express, но во многом выглядит гораздо лаконичнее и читабельнее.
@app.route('/')
def index():
    return 'Use /doctors'

@app.route("/doctors/")
def doctors():
    return json.dumps(doctors_load())

if __name__ == "__main__":
    app.run()
