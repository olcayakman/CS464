
# read images
import PIL 
from PIL import Image 
import os, os.path
import numpy as np

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
    cur_img_data = np.asarray(cur_img)
    if len(cur_img_data.shape) < 3:
        print(i, ": ", cur_img_data.shape, f)
        rgbimg = cur_img.convert('RGB')
        rgbimg_data = np.asarray(rgbimg)
        # print("its shape", rgbimg_data.shape)
        X.append(rgbimg_data.flatten().reshape(4096,3))
        imgs.append(rgbimg_data)
        i += 1
        continue
    X.append(cur_img_data.flatten().reshape(4096, 3))
    imgs.append(cur_img_data)
    i = i + 1

print(X[500])
print(X[3].shape)

##q1 preprocessing complete

# for Xi in X:
#     for i in range(3):
#         Xi_tmp = Xi[:,:,i]
#         n, p = Xi_tmp.shape
#         Xi_tmp = Xi_tmp.astype('float64')
#         Xi_tmp -= Xi_tmp.mean(axis=0)

#         u, sigma, vt = np.linalg.svd(Xi_tmp, full_matrices=False)
#         principal_components = Xi_tmp @ vt.T 
#         eigenvalues = (sigma**2) / (n - 1)
#         print(principal_components, eigenvalues)
X = np.array(X)
for i in range(3):
    Xtmp = X[:,:,i]
    n, p = Xtmp.shape
    Xtmp = Xtmp.astype('float64')
    Xtmp -= Xtmp.mean(axis=0)

    u, sigma, vt = np.linalg.svd(Xtmp, full_matrices=False)
    principal_components = Xtmp @ vt.T 
    eigenvalues = (sigma**2) / (n - 1)
    print(principal_components)
    pca_sorted = np.sort(principal_components)
    print(pca_sorted[:,100])




