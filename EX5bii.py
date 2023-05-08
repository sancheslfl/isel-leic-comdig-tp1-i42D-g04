import random
import numpy as np
import os

dirpath = os.path.dirname(__file__)
file= (dirpath+"/TestFilesCD/alice29.txt")
outputfile = (dirpath+"/TestFilesCD/BOB.txt")

def matriz(arr,lines,collums):
    list = np.array(arr).reshape(lines,collums)
    return list

def interleaving(matrizs,lines,collums):
    output = ''
    mz = matriz(matrizs,lines,collums)
    for i in range(0,collums):
        for j in range(0,lines):
            output += mz[j,i]
    return output

def bsc(input_bits, ber):
    output_bits = []
    for bit in input_bits:
        if random.random() < ber:
            output_bits.append(int(not bit)) # bit flip
        else:
            output_bits.append(bit)
    return output_bits

def deinterleaver(input_bits, rows, cols):
    input_array = np.array(input_bits)
    input_matrix = input_array.reshape(rows, cols, order='F')
    output_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            output_matrix[(i + j) % rows][j] = input_matrix[i][j]
    output_array = output_matrix.flatten(order='F')
    return list(output_array)

# Ler o arquivo de entrada (ponto A)
with open(file, "rb") as f:
    input_data = f.read()

# Converter os dados para uma lista de bits
input_bits = []
for byte in input_data:
    for i in range(8):
        input_bits.append((byte >> i) & 1)

# Definir a taxa de erro e a dimensão da matriz de interleaving
ber = 0.1
rows = int(100000.0)
cols = int((len(input_bits) / rows) + 1)
print(cols)
# Embaralhar os dados com a matriz de interleaving
interleaved_bits = interleaving(input_bits, rows, cols)

# Transmitir os dados pelo canal BSC
output_bits = bsc(interleaved_bits, ber)

# Desembaralhar os dados com a matriz de interleaving
deinterleaved_bits = deinterleaver(output_bits, rows, cols)

# Converter a lista de bits de saída de volta para bytes
output_data = bytearray()
for i in range(0, len(deinterleaved_bits), 8):
    byte = 0
    for j in range(8):
        byte |= deinterleaved_bits[i+j] << j
    output_data.append(byte)

# Salvar o arquivo de saída (ponto B)
with open(outputfile, "wb") as f:
    f.write(output_data)

# Comparar os dois arquivos
with open(file, "rb") as f1, open(outputfile, "rb") as f2:
    input_data = f1.read()
    output_data = f2.read()

num_errors = 0
for i in range(len(input_data)):
    if input_data[i] != output_data[i]:
        num_errors += 1

print("Número de bytes errados:", num_errors)
print("BER:", num_errors / len(input_data))
