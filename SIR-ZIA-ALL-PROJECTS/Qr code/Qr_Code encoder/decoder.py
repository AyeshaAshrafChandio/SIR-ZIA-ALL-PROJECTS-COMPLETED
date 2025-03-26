# First install required libraries:
# pip install qrcode[pil]
# pip install pillow
# pip install pyzbar

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os

def make_qr():
    print("\n🛠️ QR Code Generator")
    data = input("Enter text/URL to encode: ")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate and save image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("my_qr.png")
    print("✅ QR code saved as 'my_qr.png'")
    img.show()  # Opens the image

def read_qr():
    print("\n🔍 QR Code Reader")
    file = input("Enter image filename (or press Enter for default): ")
    if not file:
        file = "my_qr.png"
    
    if not os.path.exists(file):
        print("❌ File not found!")
        return
    
    # Decode QR code
    result = decode(Image.open(file))
    if result:
        print("\n📋 Decoded content:")
        print(result[0].data.decode())
    else:
        print("❌ No QR code found in image")

while True:
    print("\n🌟 QR Code Tool 🌟")
    print("1. Generate QR Code")
    print("2. Read QR Code")
    print("3. Exit")
    
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        make_qr()
    elif choice == "2":
        read_qr()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice, try again!")