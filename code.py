import qrcode

# WiFi configuration
ssid = 'WIFI_NAME'
password = 'WIFI_PASSWORD'
security = 'WPA'  # Change this to 'nopass' if there's no password, or 'WEP' if it's WEP

# Generate the WiFi QR code
wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_data)
qr.make(fit=True)

# Create and save the QR code as an image file
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
