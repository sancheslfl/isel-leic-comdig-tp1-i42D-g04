import random
import string

# Gerar cada palavra passe aleatoriamente com todas as letras, numeros e carateres especiais
def generate_password(size):
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(symbols) for _ in range(size))
    return password

# Gerar 5 exemplos de palavras-passe
for i in range(5):
    size = random.randint(8, 12)
    palavra_passe = generate_password(size)
    print(palavra_passe)