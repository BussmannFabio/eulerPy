def encontrar_numero_com_maior_sequencia(limite):
    # Dicionário para armazenar o comprimento das sequências já calculadas
    cache = {1: 1}
    
    def calcular_comprimento(n):
        # Se já calculamos este número antes, retornamos o valor armazenado
        if n in cache:
            return cache[n]
        
        # Calcula o próximo termo na sequência
        if n % 2 == 0:
            proximo = n // 2
        else:
            proximo = 3 * n + 1
        
        # Calcula o comprimento e armazena no cache
        comprimento = 1 + calcular_comprimento(proximo)
        cache[n] = comprimento
        return comprimento
    
    numero_maximo = 1
    comprimento_maximo = 1
    
    # Testa números abaixo do limite
    for numero in range(2, limite):
        comprimento = calcular_comprimento(numero)
        if comprimento > comprimento_maximo:
            comprimento_maximo = comprimento
            numero_maximo = numero
    
    return numero_maximo

# Encontra o número com a sequência mais longa abaixo de 1 milhão
resultado = encontrar_numero_com_maior_sequencia(1000000)
print(f"O número abaixo de um milhão com a maior sequência de Collatz é: {resultado}")