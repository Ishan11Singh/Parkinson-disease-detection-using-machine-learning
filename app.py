import os
import requests
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from process_image import process_image


app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["IMAGE_UPLOADS"] = "./static/img"

@app.route("/", methods=["GET", "POST"])
def upload_image():
   if request.method == "POST":
      if request.files:
         image = request.files["image"]

         image_url = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)

         image.save(image_url)

         print("Image saved")

         result = process_image(image_url)

         print(result)

         image_path = "static/img/" + image.filename
         return render_template("result.html", result=result, image_path=image_path)
   
   return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
   return render_template("about.html")

DOWNLOAD_DIRECTORY = "./static/img"



if __name__ == '__main__':
    app.run(debug=True)