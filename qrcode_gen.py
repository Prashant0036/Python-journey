import qrcode as qr
# from PIL import image
data=input("Enter something to make it's QR Code:")
img=qr.make(data)
img.save("msg.png")
