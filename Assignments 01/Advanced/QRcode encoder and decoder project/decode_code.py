from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("D:/data D/I.T Classes Course/Quarter 3/Assignments-Projects Python/assignments-04/Assignments 01/Advanced/QRcode encoder and decoder project/newqrcode.png")

results = decode(img)
print(results)