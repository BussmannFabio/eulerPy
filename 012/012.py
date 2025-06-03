import math

def numero_divisores(n):
    if n == 1:
        return 1
    count = 2 
    sqrt_n = int(math.sqrt(n)) + 1
    
    for i in range(2, sqrt_n):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
    return count

def primeiro_triangular_com_divisores(min_divisores):
    n = 1
    triangular = 1  
    
    while True:
        if n > 1:
            triangular += n
        
        if triangular % 2 == 0 or n == 1:
            divisores = numero_divisores(triangular)
            if divisores > min_divisores:
                return triangular
        
        n += 1

# Encontrar o primeiro número triangular com mais de 500 divisores
resultado = primeiro_triangular_com_divisores(500)
print(f"O primeiro número triangular com mais de 500 divisores é: {resultado}")