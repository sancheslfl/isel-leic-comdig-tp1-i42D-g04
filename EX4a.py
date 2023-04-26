def makeVernamCypher(plainText, theKey):
    # Garante que a chave seja pelo menos tão longa quanto o texto em claro
    key = theKey[:len(plainText)]
    
    # Faz a operação XOR bit a bit de cada caractere do texto em claro com o caractere correspondente na chave
    cipherText = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plainText, key))
    
    return cipherText

plaintext = "abcabcd"
key = "3333333"

# Faz a cifra
ciphertext = makeVernamCypher(plaintext, key)
print("Texto cifrado:", ciphertext)

# Faz a decifra
decryptedText = makeVernamCypher(ciphertext, key)
print("Texto decifrado:", decryptedText)
