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





    

   