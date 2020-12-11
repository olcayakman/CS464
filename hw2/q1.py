
# read images
import PIL 
from PIL import Image 
import os, os.path
import numpy as np

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
X = []
path = "datasets/van_gogh"
valid_images = [".jpg"]
i = 1
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    cur_img = Image.open(os.path.join(path,f))
    # if len(cur_img.size) < 3:
    #     print(i, ": ", cur_img.size)
    cur_img_data = np.asarray(cur_img)
    if len(cur_img_data.shape) < 3:
        print(i, ": ", cur_img_data.shape, f)
        # rgbimg = Image.new("RGBA", cur_img.size)
        # rgbimg.paste(cur_img)
        rgbimg = cur_img.convert('RGB')
        rgbimg_data = np.asarray(rgbimg)
        print("its shape", rgbimg_data.shape)
        imgs.append(rgbimg_data)
        continue
    X.append(cur_img_data.flatten().reshape(4096, 3))
    if is_grey_scale(os.path.join(path,f)):
        print(i, "grayscale", f)
    imgs.append(cur_img_data)
    i = i + 1

print(X[3].shape)

##q1 preprocessing complete




