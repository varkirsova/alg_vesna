from PIL import Image

def image_to_raw(input_path, output_path, mode):
    """
    mode: 'bw', 'gray', 'color'
    """
    img = Image.open(input_path)

    if mode == 'bw':
        img = img.convert('L')
        # Чисто 0 или 255
        img = img.point(lambda x: 0 if x < 128 else 255, 'L')
    elif mode == 'grey':
        img = img.convert('L')
    elif mode == 'color':
        img = img.convert('RGB')

    data = img.tobytes()

    with open(output_path, 'wb') as f:
        # Добавляем метаданные (тип изображения)
        f.write(mode.encode())  # 'bw', 'gray', 'color'
        f.write(data)

# Примеры использования
image_to_raw("bw.png", "bw.raw", "bw")
image_to_raw("grey.png", "gray.raw", "grey")
image_to_raw("color.jpg", "color.raw", "color")