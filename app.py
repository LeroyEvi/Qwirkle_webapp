from azure.storage.blob import BlobClient
from flask import Flask, render_template, request

account_name = "qwirklefunction"
account_key = "KaHc+hHr/rVqLCoMu74h8ahUJtfQysPqDNpyeazVfSGWl04HhkrGBKnYmIw+/LwqjIXOMm/1krKQnFdyKNOkjQ=="
container_name = "spelbord"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route("/uploader", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save("./blob.jpg")
        blob = BlobClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=qwirklefunction;AccountKey=KaHc+hHr/rVqLCoMu74h8ahUJtfQysPqDNpyeazVfSGWl04HhkrGBKnYmIw+/LwqjIXOMm/1krKQnFdyKNOkjQ==;EndpointSuffix=core.windows.net", "spelbord", "my_blob")
        with open("./blob.jpg", "rb") as data:
            blob.upload_blob(data, overwrite=True)
        return "Afbeelding werd geüpload."


if __name__ == '__main__':
   app.run(debug = True)