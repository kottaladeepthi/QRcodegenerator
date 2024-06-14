
import qrcode
# Create a QR code
qr = qrcode.QRCode(
    version=13,  #15 means the version of the qrcode --> high the number bigger the code image and complicated picture
    box_size=5,  #Size of the box where qrcode is displayed
    border=8,  #it is the white part of the image--> border in all 4 sides with white color
)
data = 'https://www.example.com'  #here you can give any link or text you want to give when the qrcode is scanned
qr.add_data(data)
qr.make(fit= True)  #the make method processes the qrcode data and generates the matrix of qr code
# fit= True ensures that the qrcode is generated with the smallest possible size that fits all the provided data
# Generate and save the image file
img = qr.make_image(fill='white', back_color='white')
img.save('qrcode.png')


