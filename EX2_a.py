import os
import pathlib
from PY import histograma

dirpath = os.path.dirname(__file__)
files= os.listdir(dirpath+"/TestFilesCD")
print(files)

def ex2(file):
    histograma(file)


def main():
    for file in files:
        ex2((dirpath+"/TestFilesCD")+ "/" + file)

main()
