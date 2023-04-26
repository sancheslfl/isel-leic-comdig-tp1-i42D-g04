import collections
import math

## Calcula a entropia de um ficheiro
# Abrir o ficheiro em modo read
with open('ListaPalavrasPT.txt', 'r') as file:
    content = file.read()

# Variável que guarda as ocorrências de cada símbolo
counter = collections.Counter(content)

total_symbols = sum(counter.values())

# Dicionário que guarda as probabilidades de cada símbolo
probabilities = {symbol: count / total_symbols for symbol, count in counter.items()}

entropy = -sum(probability * math.log2(probability) for probability in probabilities.values())

print(f"Entropia: {entropy:.2f} bits por simbolo")