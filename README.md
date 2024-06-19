

# WiFi QR Code Generator

This simple Python script generates a QR code that, when scanned, allows users to easily connect to a WiFi network without manually entering the password. It uses the `qrcode` library to create the QR code.

## Usage

1. Install the `qrcode` library if you haven't already:

   ```bash
   pip install qrcode[pil]
   ```

2. Update the `ssid`, `password`, and `security` variables in the script with your WiFi network details.

3. Run the script to generate the QR code. The QR code will be saved as `qr.png` in the same directory as the script.

## Example

For a WiFi network with the following details:

- SSID: MyWiFiNetwork
- Password: MyPassword123
- Security: WPA

Update the script as follows:

```python
ssid = 'MyWiFiNetwork'
password = 'MyPassword123'
security = 'WPA'
```

Run the script to generate the QR code.

---
