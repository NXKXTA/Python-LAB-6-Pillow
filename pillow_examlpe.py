# для установки pip install pillow
from PIL import Image, ImageDraw, ImageFilter

# # шаблон для работы с изображением
# im = Image.open("img.jpg")  # открытие изображения
# pixels = im.load()  # загрузка пикселей
# x, y = im.size  # получение ширины и высоты изображения
#
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # получение компанент для каждого пикселя
#         # ...   # выполнение преобразования
#
# im.save("new_img.jpg")

# простейшие преобразования
# негатив
im = Image.open("_huge.jpg")
pixels = im.load()
x, y = im.size

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = 255 - r, 255 - g, 255 - b

im.save("new_huge_1.jpg")

# чб
im = Image.open("_huge.jpg")
pixels = im.load()
x, y = im.size

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels_sum = r + g + b
        pixels[i, j] = pixels_sum // 3, pixels_sum // 3, pixels_sum // 3

im.save("new_huge_2.jpg")

# готовые фильтры
im = Image.open("_huge.jpg")

# radius отвечает за степень размытия изображения
im = im.filter(ImageFilter.GaussianBlur(radius=5))

# чем меньше radius, тем больше будет подчёркнуто мелких деталей
# percent определяет, насколько сильно затемняются или осветляются участки изображения, находящиеся на границах контура.
# percent=100 означает, что разница в тоне на границе более светлого и более тёмного участков усилится в два раза.
# treshhold определяет минимальную разницу тона, при которой осуществляется нерезкое маскирование.
# Если изображение шумное или зернистое (содержит нежелательные детали), значение параметра увеличивают
# для предотвращения подчёркивания нежелательных деталей.
im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=100, threshold=1))

im.save('new_huge_3.jpg')

# геометрические преобразования
im = Image.open("_huge.jpg")
# im = im.resize((128, 128))  # изменение размера изображения
# im = im.crop((0, 0, 128, 128))  # обрезка изображения
# im = im.rotate(45)  # поворот изображения
# im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# im = im.transpose(Image.Transpose.ROTATE_90)
im.save("new_huge_4.jpg")

# создание изображений
im = Image.new("RGB", (700, 700), (208, 240, 192))  # создание изображения
draw = ImageDraw.Draw(im)  # создаём холст поверх изображения

draw.ellipse((200, 300, 500, 550), fill=(255, 255, 255))  # рисуем эллипс

draw.ellipse((290, 370, 320, 400), fill=(0, 191, 255), outline='blue', width=2)  # рисуем эллипс
draw.ellipse((380, 370, 410, 400), fill=(0, 191, 255), outline='blue', width=2)  # рисуем эллипс

draw.line((60, 380, 260, 410), fill=(150, 153, 146), width=3)  # рисуем линию
draw.line((50, 440, 250, 440), fill=(150, 153, 146), width=3)  # рисуем линию
draw.line((60, 500, 260, 470), fill=(150, 153, 146), width=3)  # рисуем линию

draw.line((440, 410, 640, 380), fill=(150, 153, 146), width=3)  # рисуем линию
draw.line((450, 440, 650, 440), fill=(150, 153, 146), width=3)  # рисуем линию
draw.line((440, 470, 640, 500), fill=(150, 153, 146), width=3)  # рисуем линию

draw.ellipse((200, 150, 300, 350), fill=(255, 255, 255))  # рисуем эллипс
draw.ellipse((400, 150, 500, 350), fill=(255, 255, 255))  # рисуем эллипс

draw.arc((320, 450, 380, 500), start=0, end=180, fill=(241, 156, 187), width=5)  # рисуем дугу

im.save("img.jpg")
