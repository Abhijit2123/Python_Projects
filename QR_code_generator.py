import qrcode

data = input("Please enter data to be saved in QR code: ")

image = qrcode.make(data)

image.save(input("Where to save QR code? "))
