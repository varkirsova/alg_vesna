from PIL import Image

img = Image.open("bw.png")

img = img.convert("1")

width, height = img.size
#
# img = img.convert("L")

pixels = img.tobytes()

with open("image_bw.raw","wb") as f:

    f.write(width.to_bytes(4,"little"))
    f.write(height.to_bytes(4,"little"))
    f.write((0).to_bytes(1,"little"))
    f.write(pixels)