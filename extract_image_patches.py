from PIL import Image
from sklearn.feature_extraction import image as sk_image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio
import os,glob,sys

def open_image(path):
    print("about to open " + path)
    img = imageio.imread(path)
    imgplot = plt.imshow(img)
    #plt.show()
    return img

def main():
    data_dir = os.getenv("DATA_DIR")
    if data_dir == None:
      print("Error: Please supply the data root directory using env var DATA_DIR")
      sys.exit(1)
    image_paths = glob.glob(os.path.join(data_dir, "*.tiff"))
    for image_path in image_paths:
      img = open_image(image_path)
      patches = sk_image.extract_patches_2d(img, (50, 50))
      print(img.shape[0], img.shape[1])
      print(img.shape)
      print(patches.shape)
      print(patches[0])
      print(patches[1])
    return
    print("hello")
    one_image = np.arange(16).reshape((4, 4))
    print(one_image)
    print(patches.shape)
    print(patches[0])
    print(patches[1])
    print(patches[8])


if __name__ == "__main__":
    main()
