import time

numero = int(input("Digite um número para iniciar a contagem regressiva: "))
tempo_espera = float(input("Digite o tempo de espera (em segundos) entre cada número: "))

while numero >= 0:
    print(numero)
    numero -= 1
    time.sleep(tempo_espera)  

print("BUM!") 