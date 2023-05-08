import os
import pathlib
from PY import histograma
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

dirpath = os.path.dirname(__file__)
files= os.listdir(dirpath+"/TestFilesCD")
print(files)
name = ""

def ex2(file):
    if file == ((dirpath+"/TestFilesCD")+ "/" + "lena.bmp"):
        # Open the BMP file
        bmp_image = Image.open(file)

        # Convert the BMP image to a NumPy array
        bmp_array = np.array(bmp_image)

        # Create a histogram of the pixel intensities
        plt.hist(bmp_array.ravel(), bins=256, range=(0, 255))
        # bins = 256 to create 256 bins (one for each possible pixel intensity value)
        # Range= 256 to limit the range of the histogram to the valid pixel intensity range.
        plt.title("Histogram for Lena.bmp file")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.show()
    else:
        histograma(file)


def main():
    for file in files:
        name = file
        plt.title(f"Histogram for {name} file")
        ex2((dirpath+"/TestFilesCD")+ "/" + file)

main()
