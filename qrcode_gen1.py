import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=40,border=10)
qr.add_data("Hello")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("qr1.png")