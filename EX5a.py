import numpy as np

def interleaving(matrizs):
    output = ''
    mz = matriz(matrizs,lines,collums)
    for i in range(0,collums):
        for j in range(0,lines):
            output += mz[j,i]
    return output

def matriz(arr,lines,collums):
    list = np.array(arr).reshape(lines,collums)
    print("Matriz:")
    print(list)
    return list

#Exemplo 1
str = "ExemploDeTransmissaoInterleaving"
print("String:", str)
arr = list(str)
#print("array:", arr)
collums = 4
lines = 8
print("NºLinhas: {} e NºColunas: {}".format(lines, collums))
print("Interleaving:", interleaving(arr))