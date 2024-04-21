from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os

# C:\Фигня всякая\Python Project 1\LABS_2\lab_6_pillow\_huge.jpg
img_path = input("Введите путь до изображения: ")
if not os.path.exists(img_path):
    print("Нет такого файла")
    exit()


def reflect_vertically(img_path):
    img = Image.open(img_path)
    reflected_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    reflected_img.show()
    reflected_img.save("new_img.jpg")
    exit()


def reflect_horizontally(img_path):
    img = Image.open(img_path)
    reflected_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    reflected_img.show()
    reflected_img.save("new_img.jpg")
    exit()


def reflect_diagonally(img_path):
    img = Image.open(img_path)
    reflected_img = img.transpose(Image.ROTATE_180)
    reflected_img.show()
    reflected_img.save("new_img.jpg")
    exit()


def reflect_second_diagonally(img_path):
    img = Image.open(img_path)
    reflected_img = img.transpose(Image.TRANSVERSE)
    reflected_img.show()
    reflected_img.save("new_img.jpg")
    exit()


def apply_sepia_filter(image_path):
    filtered_img = Image.open(image_path)
    width, height = filtered_img.size

    pixels = filtered_img.load()

    for py in range(height):
        for px in range(width):
            r, g, b = filtered_img.getpixel((px, py))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    filtered_img.show()
    filtered_img.save("new_img.jpg")
    exit()


def increase_brightness(image_path):
    k = float(input("Введите коэффициент: "))
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(k)
    enhanced_img.show()
    enhanced_img.save("new_img.jpg")
    exit()


def decrease_brightness(image_path):
    k = float(input("Введите коэффициент: "))
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(1 / k)
    enhanced_img.show()
    enhanced_img.save("new_img.jpg")
    exit()


def average_color(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    total_r = total_g = total_b = 0
    for pixel in pixels:
        total_r += pixel[0]
        total_g += pixel[1]
        total_b += pixel[2]
    num_pixels = len(pixels)
    avg_r = total_r // num_pixels
    avg_g = total_g // num_pixels
    avg_b = total_b // num_pixels
    avg_color = (avg_r, avg_g, avg_b)
    avg_img = Image.new('RGB', (100, 100), avg_color)
    avg_img.show()
    avg_img.save("new_img.jpg")
    exit()


def add_text(image_path, text, font_path):
    img_with_text = Image.open(image_path)
    draw = ImageDraw.Draw(img_with_text)

    # Запросить у пользователя координаты
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
    coordinates = (x, y)

    # Выбрать шрифт и размер текста
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # Нанести текст на изображение
    draw.text(coordinates, text, fill="white", font=font)
    img_with_text.show()
    img_with_text.save("new_img.jpg")
    exit()


def add_primitive(image_path, primitive_type, fill_color):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Запросить у пользователя координаты
    if primitive_type == "ellipse":
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            x1 = int(input("Введите координату X1: "))
            y1 = int(input("Введите координату Y1: "))
        except ValueError:
            print("Координаты должны быть целыми числами")
            exit()
        coordinates = tuple(map(int, (x, y, x1, y1)))
        draw.ellipse(coordinates, fill=fill_color)
    elif primitive_type == "rectangle":
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            x1 = int(input("Введите координату X1: "))
            y1 = int(input("Введите координату Y1: "))
        except ValueError:
            print("Координаты должны быть целыми числами")
            exit()
        coordinates = tuple(map(int, (x, y, x1, y1)))
        draw.rectangle(coordinates, fill=fill_color)
    elif primitive_type == "line":
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            x1 = int(input("Введите координату X1: "))
            y1 = int(input("Введите координату Y1: "))
        except ValueError:
            print("Координаты должны быть целыми числами")
            exit()
        coordinates = tuple(map(int, (x, y, x1, y1)))
        draw.line(coordinates, fill=fill_color, width=3)
    elif primitive_type == "arc":
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            x1 = int(input("Введите координату X1: "))
            y1 = int(input("Введите координату Y1: "))
        except ValueError:
            print("Координаты должны быть целыми числами")
            exit()
        coordinates = tuple(map(int, (x, y, x1, y1)))
        draw.arc(coordinates, start=0, end=180, fill=fill_color)

    img.show()
    img.save("new_img.jpg")
    exit()


print("/" * 94)
print("//                                                                                          //")
print("//             Что сделать с изображением:                                                  //")
print("//                                                                                          //")
print("//   a. Отразить изображение по вертикали                                                   //")
print("//   b. Отразить изображение по горизонтали                                                 //")
print("//   c. Отразить изображение по главной диагонали                                           //")
print("//   d. Отразить изображение по побочной диагонали                                          //")
print("//   e. Применить на изображение фильтр «Сепия» (коэффициент выберите самостоятельно)       //")
print("//   f. Увеличить яркость изображения на k.                                                 //")
print("//   g. Уменьшить яркость изображения на k.                                                 //")
print("//   h. Рассчитать и продемонстрировать средний цвет изображения                            //")
print("//      (отдельно подсчитать сумму каждой компоненты и полученные суммы поделить на         //")
print("//       количество пикселей в изображении). Для демонстрации среднего цвета можно создать  //")
print("//       новое изображение и залить его полученным цветом.                                  //")
print("//   i. Добавить текст поверх изображения по координатам, которые введёт пользователь.      //")
print("//   j. Добавить на изображение графический примитив                                        //")
print("//      (эллипс, прямую, дугу, прямоугольник…) по координатам, которые введёт пользователь. //")
print("//                                                                                          //")
print("/" * 94)

while True:
    x = input("Выберите нужный вариант: ")
    if x == "a":
        reflect_vertically(img_path)
    elif x == "b":
        reflect_horizontally(img_path)
    elif x == "c":
        reflect_diagonally(img_path)
    elif x == "d":
        reflect_second_diagonally(img_path)
    elif x == "e":
        apply_sepia_filter(img_path)
    elif x == "f":
        increase_brightness(img_path)
    elif x == "g":
        decrease_brightness(img_path)
    elif x == "h":
        average_color(img_path)
    elif x == "i":
        add_text(img_path, "Попа", "arial.ttf")
    elif x == "j":
        add_primitive(img_path, "ellipse", "red")
    else:
        print("Нет такого варианта")
