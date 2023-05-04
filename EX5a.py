import numpy as np

def output():
    str = "Exemplodetransmissaointerleaving"
    arr = list(str)
    print(arr)
    collums = 4
    lines = 8
    mz = matriz(arr,lines,collums)
    #interleaving= []
    #for i in range(0,collums):
     #   interleaving = np.array([mz[:,i]])
     #   print(interleaving)

def matriz(arr,lines,collums):
    list = np.array(arr).reshape(lines,collums)
    print(list)
    return list