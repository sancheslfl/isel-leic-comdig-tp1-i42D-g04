import random
import os

dirpath = os.path.dirname(__file__)
file= (dirpath+"/TestFilesCD/alice29.txt")
outputfile = (dirpath+"/TestFilesCD/BOB.txt")

def bsc(input_bits, ber):
    output_bits = []
    for bit in input_bits:
        if random.random() < ber:
            output_bits.append(int(not bit)) # bit flip
        else:
            output_bits.append(bit)
    return output_bits

# Teste 1 - Com sequecia inserida pelo utilizador
input_bits = [0, 1, 0, 1, 0, 1, 0, 1]
ber = 0.1

# Transmitir a sequência pelo canal
output_bits = bsc(input_bits, ber)

# Calcular o BER real
num_errors = sum([input_bits[i] != output_bits[i] for i in range(len(input_bits))])
real_ber = num_errors / len(input_bits)
print("BER pretendido:", ber)
print("BER real:", real_ber)


# Teste 2 - Com sequencia inserida através de um ficheiro
# Ler o arquivo de entrada (ponto A)
with open(file, "rb") as f:
    input_data = f.read()

# Converter os dados para uma lista de bits
input_bits = []
for byte in input_data:
    for i in range(8):
        input_bits.append((byte >> i) & 1)

# Transmitir os dados pelo canal BSC
ber = 0.1
output_bits = bsc(input_bits, ber)

# Converter a lista de bits de saída de volta para bytes
output_data = bytearray()
for i in range(0, len(output_bits), 8):
    byte = 0
    for j in range(8):
        byte |= output_bits[i+j] << j
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

print("Número de bytes diferentes:", num_errors)
