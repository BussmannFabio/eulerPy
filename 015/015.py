import math

def contar_caminhos_grade(n):
    """
    Calcula o número de caminhos em uma grade n x n usando coeficientes binomiais.
    """
    return math.comb(2 * n, n)

# Calcular para uma grade 20x20
resultado = contar_caminhos_grade(20)
print(f"O número de caminhos em uma grade 20x20 é: {resultado}")