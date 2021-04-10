from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input("Please enter path of QR code: "))

result = decode(img)

print(result)
