import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def plot_histogram(image):
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.title("Гистограмма изображения")
    plt.xlabel("Интенсивность")
    plt.ylabel("Частота")
    plt.xlim(0, 256)
    plt.plot(histogram, color='black')

    colors = ('red', 'green', 'blue')
    for i, color in enumerate(colors):
        channel_histogram, _ = np.histogram(image[:, :, i], bins=256, range=[0, 256])
        plt.subplot(2, 2, i + 2)
        plt.title(f"Гистограмма {color.upper()} канала")
        plt.xlabel("Интенсивность")
        plt.ylabel("Частота")
        plt.xlim(0, 256)
        plt.plot(channel_histogram, color=color)

    plt.tight_layout()
    plt.show()

def main(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')

        image_np = np.array(image)

        plt.imshow(image_np)
        plt.axis('off')
        plt.title('Исходное изображение')
        plt.show()

        plot_histogram(image_np)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    image_path = 'img.jpg'
    main(image_path)