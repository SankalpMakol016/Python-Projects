import qrcode

url=input("Enter your url: ")
filename = input("Enter the filename u want to save: ")
if not(filename.endswith(".png")):
    filename=filename+".png"
img = qrcode.make(url)
img.save(filename)
