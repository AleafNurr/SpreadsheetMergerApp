from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def file_upload():
    # if request.method == "POST":
    #     if 'file' not in request.files:
    #         return "No files uploaded", 400
    #     files = request.files.getlist("files[]")
    #     for file in files:
    #         if file.filename == "":
    #             return "No files selected", 400
            
    #         file.save("uploads/" + file.filename)       

    
    return render_template('index.html')

@app.route("/success", methods=["GET", "POST"])
def sucess():
    return render_template('success.html')