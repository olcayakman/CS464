
# read images
import PIL 
from PIL import Image 
import os, os.path

def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b: return False
    return True

# open the image and put into list.
imgs = []
path = "datasets/van_gogh"
valid_images = [".jpg"]
i = 1
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    cur_img = Image.open(os.path.join(path,f))
    if is_grey_scale(os.path.join(path,f)):
        print(i, "grayscale")
    imgs.append(cur_img)
    i = i + 1

print(imgs[len(imgs)-1].mode) ## making sure we got the images right.



