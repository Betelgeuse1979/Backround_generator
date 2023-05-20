from PIL import Image, ImageFilter


img = Image.open('./sample/mclaren1.jpeg')
img.thumbnail((400, 400))
img.save('thumbnail.jpeg')


