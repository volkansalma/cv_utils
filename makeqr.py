import qrcode
import time

"""
All systems are right handed
x forward
y left
z up

optical_z forward
optical_x right
optical_y down

roll, pitch, yaw about X, Y, Z axes respectively
"""

magic_word = 'https://volkansalma.blogspot.com'

# in meters
x = 0.00000
y = 0.00000
z = 0.00000

# in radians
roll = 0.00000
pitch = 0.00000
yaw = 0.00000

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=10,
)

qr.add_data(magic_word)
qr.add_data(' x:' + str(x))
qr.add_data(' y:' + str(y))
qr.add_data(' z:' + str(z))
qr.add_data(' roll:' + str(roll))
qr.add_data(' pitch:' + str(pitch))
qr.add_data(' yaw:' + str(yaw))

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

epoch_time = int(time.time())
img.save("qrcodes/qr_code" + str(epoch_time) + ".png")
