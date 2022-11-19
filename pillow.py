from PIL import Image


#im = Image.open("img/748591006131/000001.jpg")
with Image.open("img/748591006131/000001.jpg") as im:
    out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    out.save("img/748591006131/000001_2.jpg")  # Транспонирование изображения
    print(im)
