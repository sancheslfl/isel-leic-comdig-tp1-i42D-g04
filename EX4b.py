import secrets
import math
import os
from EX4a import makeVernamCypher

dirpath = os.path.dirname(__file__)
file= (dirpath+"/TestFilesCD/alice29.txt")

# Carrega o conteúdo do arquivo alice29.txt em uma string
with open(file, "r", encoding="utf-8") as f:
    plaintext = f.read()

# Cifra o texto em claro usando uma chave constante
key = "3333333"
ciphertext_const_key = makeVernamCypher(plaintext, key)

# Cifra o texto em claro usando uma chave aleatória
random_key = secrets.token_hex(len(plaintext))
ciphertext_random_key = makeVernamCypher(plaintext, random_key)

# Calcula o histograma e a entropia do texto em claro
freqs_plain = {c: plaintext.count(c) for c in set(plaintext)}
total_chars = sum(freqs_plain.values())
probs_plain = {c: freqs_plain[c] / total_chars for c in freqs_plain}
entropy_plain = -sum(p * math.log2(p) for p in probs_plain.values())

# Calcula o histograma e a entropia do texto cifrado com chave constante
freqs_cipher_const_key = {c: ciphertext_const_key.count(c) for c in set(ciphertext_const_key)}
total_chars = sum(freqs_cipher_const_key.values())
probs_cipher_const_key = {c: freqs_cipher_const_key[c] / total_chars for c in freqs_cipher_const_key}
entropy_cipher_const_key = -sum(p * math.log2(p) for p in probs_cipher_const_key.values())

# Calcula o histograma e a entropia do texto cifrado com chave aleatória
freqs_cipher_random_key = {c: ciphertext_random_key.count(c) for c in set(ciphertext_random_key)}
total_chars = sum(freqs_cipher_random_key.values())
probs_cipher_random_key = {c: freqs_cipher_random_key[c] / total_chars for c in freqs_cipher_random_key}
entropy_cipher_random_key = -sum(p * math.log2(p) for p in probs_cipher_random_key.values())

# Imprime os resultados
print("Entropia do texto em claro:", entropy_plain)
print("Entropia do texto cifrado com chave constante:", entropy_cipher_const_key)
print("Entropia do texto cifrado com chave aleatória:", entropy_cipher_random_key)
