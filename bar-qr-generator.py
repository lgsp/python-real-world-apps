import os
import io
import pyqrcode
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter

class QR_Gen(object):
    def __init__(self, text):

        @staticmethod
        def qr_generator(text):
            qr_code = pyqrcode.create(text)
            file_name = "QR Code Result"
            save_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            name = f"{save_path}{file_name}.png"
            qr_code.png(name, scale=10)
            image = Image.open(name)
            image = image.resize((400, 400), Image.ATNTIALIAS)
            image.show()

class Bar_Gen(object):
    def __init__(self, digits):
        self.bar_image = self.bar_generator(digits)

    @staticmethod
    def bar_generator(digits):
        rv = io.BytesIO()
        EAN13(str(digits), writer=ImageWriter()).writer(rv)
        image = Image.open(rv)
        image = image.resize((400, 400), Image.ANTIALIAS)
        image.show()


if __name__ == "__main__":
    QR_Gen(input("[QR] Enter text or link: "))
    Bar_Gen(int(input("[BAR] Enter 12 digits: ")))


            
