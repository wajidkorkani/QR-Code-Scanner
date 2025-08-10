# QR Code Scanner

This project is a simple QR Code Scanner built in Python. It uses your laptop camera to capture an image, then scans and decodes any QR code present in the captured image.

## Features
- Captures an image from your laptop camera after 10 seconds
- Saves the captured image as `qrCode.png`
- Scans and decodes QR codes from the image
- Prints the QR code type and data to the console

## Requirements
Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
Run the main script:

```bash
python Src/index.py
```

The camera window will open. After 10 seconds, a picture will be taken and saved as `qrCode.png`. If a QR code is detected, its data will be printed in the console.

Press `q` to quit the camera window early.

## Dependencies
- opencv-python
- pyzbar
- Pillow

## License
This project is open source and licensed under the MIT License. You are free to use, modify, and distribute this software in your own projects, both personal and commercial, as long as you include the original copyright and license notice.

See the LICENSE file for full details.
