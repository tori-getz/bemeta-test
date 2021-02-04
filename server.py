from flask import Flask
from db import database_connect

database_connect()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run()
