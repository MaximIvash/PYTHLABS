from PIL import Image, ImageDraw, ImageFont

def watermark(srcImagePath, srcWatermarkImagePath, dirImagePath, watermatkText, posImage, posText):
    with Image.open(srcImagePath) as img, Image.open(srcWatermarkImagePath) as newimg:
        output = ImageDraw.Draw(img)

        newimg = newimg.resize((200, 200))

        img.paste(newimg, posImage)
        drawing = ImageDraw.Draw(img)
        font = ImageFont.load_default(size=30)
        drawing.text(posText, watermatkText, fill=(255, 255, 0), font=font)

        img.show()
        img.save(dirImagePath, 'jpeg')
if __name__ == '__main__':
    srcImage = 'cars.jpg'
    srcWatermark = 'cars.jpg'
    dirPath = 'newimages/task3.jpg'
    watermark(srcImage, srcWatermark, dirPath, watermatkText='Ivashchenko Maxim', posImage=(10, 10), posText=(10, 10))