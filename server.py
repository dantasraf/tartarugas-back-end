from main import getReq, postReq
import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'images/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['GET'])
def reqGet():
    return getReq()


@app.route('/', methods=['POST'])
def reqPost():
    return postReq()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'media' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['media']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            response = app.response_class(
                response="Upload Efetuado com Sucesso",
                status=200,
                mimetype='application/json'
            )
            # response = "Upload Efetuado com Sucesso"
            return response
