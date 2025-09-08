# Install the library first: pip install qrcode[pil]
import qrcode

# Function to generate QR code
def generate_qr(data, filename="qrcode.png"):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(data)  # Add data to the QR code
    qr.make(fit=True)  # Optimize the QR code size

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Example usage
data_to_encode = "https://example.com"  # Replace with your text or URL
generate_qr(data_to_encode)
