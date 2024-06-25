from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def file_upload():
    return render_template('index.html')

