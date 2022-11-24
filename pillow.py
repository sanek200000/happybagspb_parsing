from PIL import Image


#im = Image.open("img/748591006131/000001.jpg")
with Image.open("img\129477444971\000002.jpg") as im:
    out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    out.save("img\129477444971\000002_izm.jpg")  # Транспонирование изображения
    print(im)

