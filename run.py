import argparse
import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("data", type=str, help="Data to encode into QR code")
    parser.add_argument("output_file", type=str, help="Output file path for the QR code image")
    args = parser.parse_args()

    generate_qr_code(args.data, args.output_file)
