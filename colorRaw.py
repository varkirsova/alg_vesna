from PIL import Image

img = Image.open("color.jpg")

width, height = img.size

img = img.convert("RGB")

pixels = img.tobytes()

with open("imageColor.raw", "wb") as f:
    f.write(width.to_bytes(4, "little"))
    f.write(height.to_bytes(4, "little"))
    f.write((2).to_bytes(1, "little"))
    f.write(pixels)