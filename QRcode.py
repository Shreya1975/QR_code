import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Create QR code
myqr = qrcode.make("https://www.youtube.com/watch?v=-OEh1EQ-vuM")
myqr.save("myqr.png") # Save the QR code as an image file 


myqr1 = qrcode.make("https://www.youtube.com/watch?v=0RDI9CMilhk")
myqr1.save("myqr1.png")


# Decode QR code
#What is this...
MYQR = decode(Image.open("myqr.png"))
print(MYQR[0].data.decode("ascii"))
