from PIL import Image

file = 'cars.jpg'
with Image.open(file) as img:
    img.load()
    r, g, b = img.split()

    newWidth = img.width * 4
    output = Image.new('RGB', (newWidth, img.width))

    output.paste(img)
    output.paste(r.convert('RGB'), (img.width, 0))
    output.paste(g.convert('RGB'), (img.width * 2, 0))
    output.paste(b.convert('RGB'), (img.width * 3, 0))

    output.show()
    output.save('newimages/task1.jpg', 'jpeg')