# pip install pillow
from PIL import Image
imgs=["1.jpg", "2.jpg", "3.jpg"]

pil_imgs=[Image.open(image).convert("RGB") for image in imgs]

img_list=pil_imgs[1:]
pil_imgs[0].save("m.pdf" ,save_all=True, append_images=img_list)