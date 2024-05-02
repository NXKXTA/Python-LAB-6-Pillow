from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os

# C:\Фигня всякая\Python Project 1\LABS_2\lab_6_pillow\_huge.jpg
img_path = input("Введите путь до изображения: ")
if not os.path.exists(img_path):
    print("Нет такого файла")
    exit()

img = Image.open(img_path)


def reflect_vertically():
    reflected_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    return reflected_img

def reflect_horizontally():
    reflected_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return reflected_img


def reflect_diagonally():
    reflected_img = img.transpose(Image.ROTATE_180)
    return reflected_img


def reflect_second_diagonally():
    reflected_img = img.transpose(Image.TRANSVERSE)
    return reflected_img


def apply_sepia_filter():
    width, height = img.size

    pixels = img.load()

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))
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

    return img


def increase_brightness():
    k = float(input("Введите коэффициент: "))
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(k)
    return enhanced_img


def decrease_brightness():
    k = float(input("Введите коэффициент: "))
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(1 / k)
    return enhanced_img


def average_color():
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
    return avg_img


def add_text(text, font_path):
    draw = ImageDraw.Draw(img)

    # Запросить у пользователя координаты
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
    coordinates = (x, y)

    # Выбрать шрифт и размер текста
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # Нанести текст на изображение
    draw.text(coordinates, text, fill="white", font=font)
    return img


def add_primitive(primitive_type, fill_color):
    draw = ImageDraw.Draw(img)
    try:
        x = int(input("Введите координату X: "))
        y = int(input("Введите координату Y: "))
        x1 = int(input("Введите координату X1: "))
        y1 = int(input("Введите координату Y1: "))
    except ValueError:
        print("Координаты должны быть целыми числами")
        exit()
    coordinates = x, y, x1, y1
    # Запросить у пользователя координаты
    if primitive_type == "ellipse":
        draw.ellipse(coordinates, fill=fill_color)
    elif primitive_type == "rectangle":
        draw.rectangle(coordinates, fill=fill_color)
    elif primitive_type == "line":
        draw.line(coordinates, fill=fill_color, width=3)
    elif primitive_type == "arc":
        draw.arc(coordinates, start=0, end=180, fill=fill_color)

    return img


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
        pic = reflect_vertically()
    elif x == "b":
        pic = reflect_horizontally()
    elif x == "c":
        pic = reflect_diagonally()
    elif x == "d":
        pic = reflect_second_diagonally()
    elif x == "e":
        pic = apply_sepia_filter()
    elif x == "f":
        pic = increase_brightness()
    elif x == "g":
        pic = decrease_brightness()
    elif x == "h":
        pic = average_color()
    elif x == "i":
        pic = add_text("Попа", "arial.ttf")
    elif x == "j":
        pic = add_primitive("ellipse", "red")
    else:
        print("Нет такого варианта")

    pic.show()
    pic.save("new_img.jpg")
    exit()
