from PIL import Image as im
from PIL import ImageOps as io

shirt = im.open("shirt.png")
muppet = im.open("before1.jpg")

with im.open("after1.jpg") as after:
    print(after.size)
with im.open("before1.jpg") as muppet:
    shirt = im.open("shirt.png").convert("RGBA")
    pre_paste = io.fit(image=muppet, size=after.size).convert("RGBA")
    pre_paste.paste(box=shirt, im=shirt)
    pre_paste.save("test.png")
