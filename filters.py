from PIL import Image

# img = Image.open("dog.jpeg").convert("L")
# width, height = img.size
def DarkFilter(pixel: int) -> int:
    if pixel >= 170 and pixel <= 255:
        pixel -= 75
    elif pixel >= 75 and pixel <= 169:
        pixel -= 25
    else:
        pixel = 0
    return pixel



def apply_filter(img: Image.Image, filt) -> Image.Image:
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            new_pixel = filt(pixel)
            img.putpixel((i, j), new_pixel)
    return img


def BrightFilter():
    pass

def InverseFilter():
    pass