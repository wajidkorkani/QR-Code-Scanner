from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
image = Image.open("qrCode.png")

# Decode QR code
decoded_objects = decode(image)

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))
