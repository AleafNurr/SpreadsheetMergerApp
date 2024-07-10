from flask import Flask, render_template, request, send_file, make_response
import pandas as pd

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'csv'}

@app.route("/", methods=["GET", "POST"])
def file_upload():
    
    if request.method == "POST":
        if 'file1' not in request.files and 'file2' not in request.files:
            return f"No files uploaded", 400
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")
        if file1 and file2:
            if file1.filename == "" or file2.filename == "":
                return f"Missing filename", 400
            if not file1.filename.endswith(".csv") or not file2.filename.endswith(".csv"):
                return f"Incorrect file type (.csv)", 400
            x1 = pd.read_csv(file1)
            x2 = pd.read_csv(file2)
            if not len(x1.columns) == len(x2.columns):
                return "File mismatch (columns)", 400
            else:
                # concate
                x3 = pd.concat([x1, x2]) 
                concate_file = x3.to_csv(index=False)
                # create HTTP response with CSV data
                response = make_response(concate_file)
                response.headers['Content-Disposition'] = "attachment; filename=export.csv"
                response.headers['Content-type'] = "text/csv"
                return response
        else:
            return f"upload failed", 400
        
        # if len(files) <= 1:
        #     return f"Failed to upload the minimum number of files (2) {files}", 400
        # if len(files) > 2:
        #     return "Exceed maximum number of files (2)", 400
        # check file type
        # for file in files:
        #     if file.filename == "":
        #         return f"No files selected {file}", 400
        #     if not file.filename.endswith(".csv"):
        #         return f"Incorrect file {file.filename}", 400
        # # get first file -> read into pd from csv
        # x1 = pd.read_csv(files[0].filename)
        # # get second file
        # x2 = pd.read_csv(files[1].filename)
        # # check col size equal
        # if not len(x1.columns) == len(x2.columns):
        #     return "File mismatch (columns)", 400
        # else:
        #     # concate
        #     x3 = pd.concat([x1, x2]) 
        #     return send_file(x3, mimetype='text/csv', as_attachment=True, download_name='concatenated.csv')
    return render_template('index.html')