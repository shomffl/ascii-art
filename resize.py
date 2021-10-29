import cv2

class ResizeImage:

    def __init__(self, filepath, output_path):
        self.filepath = filepath
        self.output_path = output_path

    def resize_image(self):
        image = cv2.imread(self.filepath)
        height = image.shape[0]
        width = image.shape[1]
        longer_one = max(height,width)

        adjust_per = round(200 / longer_one, 2)
        adjust_height = int(height * adjust_per)
        adjust_width = int(width * adjust_per)

        resized_image = cv2.resize(image,(adjust_width, adjust_height))
        cv2.imwrite(f"{self.output_path}newimage.png", resized_image)

        return (adjust_height, adjust_width)
