import cv2
from PIL import Image, ImageFont, ImageDraw


class MakeGrayFrame:

    def __init__(self, filepath, output_path):
        self.filepath = filepath
        self.output_path = output_path

    def make_gray(self):

        colorset = "@QT&gWNM0$#B8%DRXmOKGAH9UpbpkSE257j]aewZhIoy31YIC}ix>=-~^`':;,. "
        img = cv2.imread(self.filepath)
        height = img.shape[0] * 14
        width = img.shape[1] * 15
        canvasSize    = (width, height)
        backgroundRGB = (255, 255, 255)
        textRGB       = (0, 0, 0)

        font = ImageFont.truetype("HGRGE.TTC", 10)
        pos = (0,0)



        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output = ""
        image = Image.new("RGB", canvasSize, backgroundRGB)
        draw = ImageDraw.Draw(image)

        for gray2 in gray:

            for dark in gray2:
                output += colorset[dark // 4] * 3
            output += "\n"

        draw.text(pos,output,fill=textRGB, font = font)
        image_resize = image.resize((width, height))
        image_resize.save(f"{self.output_path}image.png")
