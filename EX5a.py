import numpy as np

def matriz(string,lines,collums):
    array = list(string)
    list = np.arange(array).reshape(lines,collums)
    print(list)

matriz("Exemplodetransmissaointerleaving",8,4)