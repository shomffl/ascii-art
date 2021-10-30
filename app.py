
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from make import MakeGrayFrame
from resize import ResizeImage
from convert_filename import Kakasi


app = Flask(__name__)

INPUT_FOLDER = "./static/input_image/"
OUTPUT_FOLDER = "./static/output_image/"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


#ascii-art作成の処理
@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        ascii_filename = Kakasi.japanese_to_ascii(file.filename)
        filename = secure_filename(ascii_filename)
        filepath = os.path.join(INPUT_FOLDER, filename)
        file.save(filepath)

        #画像のサイズを縮小
        resize = ResizeImage(f"{INPUT_FOLDER}{filename}", OUTPUT_FOLDER)
        mesure = resize.resize_image()

        #縮小した画像の縦と横の長さを取得
        height = int(mesure[0] * 2.5)
        width = int(mesure[1] * 2.5)

        #ascii-artを作成
        make = MakeGrayFrame(f"{OUTPUT_FOLDER}newimage.png", OUTPUT_FOLDER)
        make.make_gray()

    return render_template("result.html",  filepath=f"{OUTPUT_FOLDER}/image.png", height=height, width=width)



if __name__ == "__main__":
    app.run()
