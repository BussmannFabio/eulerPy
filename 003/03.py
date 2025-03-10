import math

def crivo_de_eratosthenes(limite):
    
    crivo = [True] * (limite + 1)
    crivo[0], crivo[1] = False, False
    for numero in range(2, int(math.sqrt(limite)) + 1):
        if crivo[numero]:
            for multiplo in range(numero * numero, limite + 1, numero):
                crivo[multiplo] = False
    primos = [numero for numero, e_primo in enumerate(crivo) if e_primo]
    return primos

def maior_fator_primo(n):
    limite = math.isqrt(n) 
    primos = crivo_de_eratosthenes(limite)  
    
    maior_primo = 1
    
    for primo in primos:
        while n % primo == 0:
            maior_primo = primo
            n //= primo
    
    if n > 2:
        maior_primo = n
    
    return maior_primo

numero = 600851475143
print(maior_fator_primo(numero))
