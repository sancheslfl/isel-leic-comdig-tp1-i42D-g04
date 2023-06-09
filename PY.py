import math
import matplotlib.pyplot as plt
import os

def progressao_geometrica(N, u, r):
    termos = [u] # começa com o primeiro termo u
    for i in range(1, N):
        termo_atual = termos[i-1] * r # calcula o próximo termo
        termos.append(termo_atual) # adiciona o próximo termo à lista de termos
    return termos


def mdc(a,b):
    if(a != 0 and b != 0):
        if(a > b):
            dividendo = a
            divisor = b
        else:
            dividendo = b
            divisor = a
        while(dividendo % divisor != 0):
            resto = dividendo % divisor
            dividendo = divisor
            divisor = resto
        return divisor
    else:
        print("Os números não podem ser nulos") 

def freq_symbols(file_path):
        with open(file_path, 'r') as file:
            # Lê todo o conteúdo do arquivo
            content = file.read()

            # Conta o número de ocorrências de cada símbolo
            counter = {}
            for c in content:
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1
        
            # Guarda o simbulo mais e menos frequente para depois dar return 
            most_frequent_symbol = max(counter)
            less_frequent_symbol = min(counter)

            most_frequent = counter[most_frequent_symbol]
            less_frequent = counter[less_frequent_symbol]

            # Dá return dos simbolos
            print("Símbolo mais frequente: {} ({} ocorrências)".format(most_frequent_symbol, most_frequent))
            print("Símbolo menos frequente: {} ({} ocorrências)".format(less_frequent_symbol, less_frequent))

            return (most_frequent_symbol, most_frequent, less_frequent_symbol, less_frequent)

# Testes das Funções
#freq_symbols('ListaPalavrasEN.txt')
#freq_symbols('ListaPalavrasPT.txt')


#Função que apresenta o histograma de um ficheiro, o valor da informação própria de cada símbolo e a entropia do ficheiro

def histograma(file_name):
    entropia = 0.0000
    symbol = None
    
    with open(file_name, 'r') as file:
        data = file.read()

# Conta o número de ocorrências de cada símbolo
    histogram = {}
    for symbol in data:
        if symbol in histogram:
            histogram[symbol] += 1
        else:
            histogram[symbol] = 1
    
# Valor da informação própria de cada simbolo
    info = {}
    for symbol, freq in histogram.items():
        info[symbol] = -(math.log((freq/len(data)),2))
        print(f'Informação própria do símbolo: {info[symbol]}')
        
# Valor da entropia do ficheiro
    for symbol, freq in histogram.items():
        prob = (freq/len(data))
        i = prob*info[symbol]
        entropia += i

    plt.bar(histogram.keys(),histogram.values())
    plt.xlabel("Symbol")
    plt.ylabel("Frequency")    
    plt.show() 

    print(f"Entropia do arquivo: {entropia}")

#histograma('ListaPalavrasEN.tx')
#histograma('ListaPalavrasPt.txt')