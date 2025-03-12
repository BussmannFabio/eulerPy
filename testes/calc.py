def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        resultado = "Operação inválida!"

    print(f"Resultado: {resultado}")

calculadora()