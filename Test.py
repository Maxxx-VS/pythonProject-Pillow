from PIL import Image

img = Image.open("cat.jpeg").convert("L")

# Обрезаем изображение
# im.crop((left, upper, right, lower))
# left, upper - координаты верхнего левого угла
# right, lower - координаты нижнего правого угла

img.crop((40, 30, 60, 50))  # обрежет изображение по координатам углов (40, 30) и (60, 50)
img.crop((40, 30, 60, 50)).resize((200, 200)).show()

# Рисуем на изображении
from PIL import ImageDraw

draw = ImageDraw.Draw(img)

# Рисуем линию
# ImageDraw.Draw.line(xy, fill=None, width=0, joint=None)
# xy – координаты начала и конца линии
# fill – цвет линии
# width – толщина линии
# joint – тип соединения линий. Возможные значения: “curve”, “none”, “miter”, “round”, “bevel”.

w, h = img.size
draw.line((0, 0, w, h), fill=0)
draw.line((0, h, w, 0), fill=255, width=5)
img.show()

# Рисуем прямоугольник
# ImageDraw.Draw.rectangle(xy, fill=None, outline=None, width=0)
# xy – координаты верхнего левого и нижнего правого угла прямоугольника
# fill – цвет заливки
# outline – цвет границы
# width – толщина границы
img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, w, h), fill=0)
draw.rectangle((40, 30, 60, 50), outline=128, width=2)
img.show()

# # Рисуем круг
img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.ellipse((40, 30, 60, 50), fill=0)
img.show()

# Рисуем текст

# ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left",
#                     language=None, stroke_width=0, stroke_fill=None)
# xy – координаты верхнего левого угла текста
# text – текст
# fill – цвет текста
# font – шрифт
# anchor – определяет как координаты xy будут интерпретироваться. Если anchor = None, то координаты xy будут интерпретироваться как координаты левого верхнего угла текста. Если anchor = “mm”, то координаты xy будут интерпретироваться как координаты центра текста.
# spacing – межстрочный интервал
# align – выравнивание текста. Возможные значения: “left”, “center”, “right”
# language – язык текста (например, “ru”)
# stroke_width – толщина обводки текста
# stroke_fill – цвет обводки текста
img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.text((20, 10), "Hello world!", fill=0)
img.show()

# можно загрузить шрифт из файла
from PIL import ImageFont
font = ImageFont.truetype("YesevaOne-Regular.ttf", size=10)

img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.text((20, 10), "Hello world!", fill=0, font=font)
img.show()

# можно нарисовать текст с обводкой
img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.text((20, 10), "Hello world!", fill=0, font=font, stroke_width=2, stroke_fill=255)
img.show()

# можно написать текст в несколько строк
img = Image.open("image_1.png").convert("L")
draw = ImageDraw.Draw(img)
draw.multiline_text((20, 10), "Hello world!\nHello world!", fill=0, font=font)
img.show()

# Задание 2
# Подпиши мем и сохрани его
meme = Image.open("hlebushek.png")
w, h = meme.size
text = "Всем хлебушек\nза мой счёт"
font = ImageFont.truetype("YesevaOne-Regular.ttf", size=50)

draw = ImageDraw.Draw(meme)
draw.multiline_text((100, 2 * h // 3), text, stroke_width=3, stroke_fill="black", fill="white", font=font, align="center")
meme.save("hlebushek_with_text.png")
meme.show()

# _________________________________________________________________
# Попиксельное изменение изображения
# _________________________________________________________________

# получение цвета пикселя по координатам
# Image.getpixel((x, y))
# x, y – координаты пикселя
print(img.getpixel((0, 0)))

# изменение цвета пикселя по координатам
# Image.putpixel((x, y), color)
# x, y – координаты пикселя
# color – цвет пикселя
img.putpixel((0, 0), 255)
img.show()


# Поменяем цвета на изображении

img = Image.open("cat.jpeg").convert("L")

for i in range(img.width):
    for j in range(img.height):
        # получаем цвет
        pixel = img.getpixel((i, j))

        # как-либо меняем цвет
        new_pixel = max(100, pixel)

        # сохраняем пиксель обратно
        img.putpixel((i, j), new_pixel)

img.show()
