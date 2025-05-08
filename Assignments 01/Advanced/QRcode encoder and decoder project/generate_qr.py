import qrcode

data = "Hell0, my name is Jawaid Ali."

img = qrcode.make(data)
img.save("D:/data D/I.T Classes Course/Quarter 3/Assignments-Projects Python/assignments-04/Assignments 01/Advanced/QRcode encoder and decoder project/newqrcode.png")
