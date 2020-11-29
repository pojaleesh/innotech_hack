from flask import request, redirect, render_template
from werkzeug.utils import secure_filename
from flask import Flask

app = Flask(__name__)

import os

app.config["IMAGE_UPLOADS"] = "images_uploaded"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 1024 * 1024 * 1024


def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
    return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        f = open('links', 'w')
        
        if request.files:
            f.write(request.form['name'])
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
        
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                
                print("Image saved")
                
                return redirect(request.url)
            
            else:
                print("That file extension is not allowed")
                return redirect(request.url)

return render_template("upload_image.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

