# pip install pillow
from PIL import Image
image=Image.open("logo.eps").convert("RGB")
image.save("1.png" ,"png")