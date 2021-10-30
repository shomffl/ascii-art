import cv2
from PIL import Image, ImageFont, ImageDraw


#ascii-art作成のための処理
class MakeGrayFrame:

    def __init__(self, filepath, output_path):
        self.filepath = filepath
        self.output_path = output_path

    def make_gray(self):

        colorset = "@QT&gWNM0$#B8%DRXmOKGAH9UpbpkSE257j]aewZhIoy31YIC}ix>=-~^`':;,. "

        #ascii-artを書き込んでいくための画像生成のための変数
        img = cv2.imread(self.filepath)
        height = img.shape[0] * 14
        width = img.shape[1] * 15
        canvasSize    = (width, height)
        backgroundRGB = (255, 255, 255)
        textRGB       = (0, 0, 0)
        font = ImageFont.truetype("./HGRGE.TTC", 10)
        pos = (0,0)


        #画像をグレイスケール化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        #ascii-artを書き込んでいくための画像を生成
        image = Image.new("RGB", canvasSize, backgroundRGB)
        draw = ImageDraw.Draw(image)


        output = ""
        for gray2 in gray:
            for dark in gray2:

                #colorsetの中からグレイスケールを4で割った数に該当する文字を選んでいく
                output += colorset[dark // 4] * 3
            output += "\n"


        draw.text(pos,output,fill=textRGB, font = font)
        image_resize = image.resize((width, height))
        image_resize.save(f"{self.output_path}image.png")
