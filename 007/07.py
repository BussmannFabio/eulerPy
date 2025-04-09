def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    max_divisor = int(numero**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if numero % divisor == 0:
            return False
    return True

def encontrar_enesimo_primo(n):
    contador = 0
    candidato = 2
    while True:
        if eh_primo(candidato):
            contador += 1
            if contador == n:
                return candidato
        candidato += 1

numero_primo = encontrar_enesimo_primo(10001)
print(f"O 10001º número primo é: {numero_primo}")