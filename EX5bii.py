import random
import numpy as np

# Definir a Função de interleaving
def matriz(arr,lines,collums):
    list = np.array(arr)
    array = list.reshape(lines,collums)
    return array

def interleaving(matrizs,lines,collums):
    output = ''
    mz = matriz(matrizs,lines,collums)
    for i in range(0,collums):
        for j in range(0,lines):
            output += mz[j,i]
    return output

# Definir a Função BSC
def bsc(input_bits, ber):
    output_bits = []
    for bit in input_bits:
        if random.random() < ber:
            output_bits.append(int(not bit)) # bit flip
        else:
            output_bits.append(bit)
    return output_bits

# Definir a Função de-interleaving
def deinterleaver(input_bits, rows, cols):
    input_array = np.array(input_bits)
    input_matrix = input_array.reshape(rows, cols, order='F')
    output_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            output_matrix[(i + j) % rows][j] = input_matrix[i][j]
    output_array = output_matrix.flatten(order='F')
    return list(output_array)

# Definir a Função de conversão simbolos em binaria
def simconvbin(sim):
    simbolos = sim
    binary_str = ''.join([bin(ord(char))[2:] for char in simbolos])
    return binary_str

# Definir a Função de conversão binaria em simbolos
def binconvsim(bits):
    #str_binaria = ''.join(bits)
    simbolos = ''.join([chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)])
    return simbolos

# Teste 1
# Definir as variaveis para o Teste
str = "ExemploDeTransmissaoInterleaving"
print("String:", str)
arr = list(str)
ber = 0.1
rows = 8
cols = 4
A = interleaving(arr,rows,cols)
print("NºLinhas: {} e NºColunas: {}".format(rows, cols))
print("Interleaving:", A)
converter_output_A = simconvbin(A)
print("conversor simbolo-binario:", converter_output_A)
BSC = bsc(converter_output_A ,ber)
print("BSC:", BSC)
converter_output_B = binconvsim(BSC)
print("conversor binario-simbolo:", converter_output_B)
output = deinterleaver(converter_output_B,rows,cols)
print("de-interleaving:", output)

# Comparar os pontos A e B
# Ponto A - saida da função de interleaving
# Ponto B - saida da conversão binario-simbolo
    
num_errors = 0
for i in range(len(converter_output_A)):
    if converter_output_A[i] != converter_output_B[i]:
        num_errors += 1

print("Número de bytes errados:", num_errors)
print("BER:", num_errors / len(converter_output_A))