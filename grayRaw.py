from PIL import Image

img = Image.open("grey.jpg")

img = img.convert("L")

width, height = img.size

pixels = img.tobytes()

with open("imageGray.raw", "wb") as f:
    f.write(width.to_bytes(4,"little"))
    f.write(height.to_bytes(4,"little"))
    f.write((1).to_bytes(1,"little"))
    f.write(pixels)