import collections
import math

## Calcula percentagem das ocorrências de cada simbolo de um ficheiro
# Abrir o ficheiro em modo read
with open('ListaPalavrasPT.txt', 'r') as file:
    content = file.read()

# Variável que guarda as ocorrências de cada símbolo
counter = collections.Counter(content)

total_symbols = sum(counter.values())

symbols = sorted(counter.keys())

# Dicionário que guarda as percentagens de cada símbolo
percentages = {symbol: count / total_symbols * 100 for symbol, count in counter.items()}

for symbol in symbols:
    percentage = percentages[symbol]
    print(f"{symbol}: {percentage:.5f}%")