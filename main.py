import imageGeneral as imageClass


def testMethod():
    a = 1
    a += 1
    print(a)


if __name__ == '__main__':
    IMAGE_FILE_NAME = "image-resistor.jpg"
    loadImageClass = imageClass.LoadImage()

    # HSV色空間の画像ロード
    # img = loadImageClass.load_hsv_image(IMAGE_FILE_NAME)

    img = loadImageClass.extract_color_image(IMAGE_FILE_NAME, 110, 170, 190)
    loadImageClass.show_image(img)
