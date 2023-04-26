import random
import numpy as np

def gerar_simbolos(n, p):
    simbolos = np.random.choice(len(p), n, p=p)
    return simbolos.tolist()