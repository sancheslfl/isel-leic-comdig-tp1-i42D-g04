import numpy as np
import math
from EX3a import gerar_simbolos

def calcular_entropia(p):
    p = np.array(p)
    return -np.sum(p*np.log2(p))


M = 4 # Alfabeto de 4 símbolos
p = [0.25, 0.25, 0.25, 0.25] # FMP uniforme
N = 1000 # Sequência de 1000 símbolos
simbolos = gerar_simbolos(N, p)
entropia = calcular_entropia(p)
entropia_estimada = calcular_entropia(np.bincount(simbolos)/N)
print("Teste 1")
print(f"Entropia real: {entropia:.3f}")
print(f"Entropia estimada: {entropia_estimada:.3f}")

M = 6 # Alfabeto de 6 símbolos
p = [0.30, 0.25, 0.20, 0.10, 0.10, 0.05] # FMP uniforme
N = 1000 # Sequência de 1000 símbolos
simbolos = gerar_simbolos(N, p)
entropia = calcular_entropia(p)
entropia_estimada = calcular_entropia(np.bincount(simbolos)/N)
print("Teste 2")
print(f"Entropia real: {entropia:.3f}")
print(f"Entropia estimada: {entropia_estimada:.3f}")

M = 6 # Alfabeto de 6 símbolos
p = [0.30, 0.25, 0.20, 0.10, 0.10, 0.05] # FMP uniforme # FMP uniforme
N = 500 # Sequência de 500 símbolos
simbolos = gerar_simbolos(N, p)
entropia = calcular_entropia(p)
entropia_estimada = calcular_entropia(np.bincount(simbolos)/N)
print("Teste 3")
print(f"Entropia real: {entropia:.3f}")
print(f"Entropia estimada: {entropia_estimada:.3f}")

M = 6 # Alfabeto de 6 símbolos
p = [0.30, 0.25, 0.20, 0.10, 0.10, 0.05] # FMP uniforme # FMP uniforme
N = 2000 # Sequência de 2000 símbolos
simbolos = gerar_simbolos(N, p)
entropia = calcular_entropia(p)
entropia_estimada = calcular_entropia(np.bincount(simbolos)/N)
print("Teste 4")
print(f"Entropia real: {entropia:.3f}")
print(f"Entropia estimada: {entropia_estimada:.3f}")

#Os resultados obtidos para a entropia estimada devem se aproximar da entropia real à medida que o número de 
# símbolos N aumenta. Para valores pequenos de N, a entropia estimada pode variar significativamente em relação 
# à entropia real devido ao efeito de flutuações estatísticas. Para valores grandes de N, a entropia estimada deve 
# se aproximar da entropia real, independentemente do valor de M.
#Em geral, quanto maior o valor de M, maior é a complexidade da fonte e, portanto, maior é a entropia real. 
#No entanto, se a FMP for muito desigual, a entropia pode ser menor do que o esperado. 
#Por outro lado, quanto maior o valor de N, maior é a precisão da estimativa da entropia e 
# menor é o efeito de flutuações estatísticas.