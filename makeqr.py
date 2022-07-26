import qrcode
import time    


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://volkansalma.blogspot.com')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

epoch_time = int(time.time())
img.save("qrcodes/qr_code" + str(epoch_time) + ".png")
