# Calculadora em Python

# Curso Python Fundamentos para Análise de Dados da Data Science Academy
# Desenvolvida em Python a partir do que foi aprendido nos capítulos 2 e 3
# Autora: Karla B S Oliveira
# Data: 26 de março de 2022

print("\n******************* Python Calculator *******************")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print('\nSelecione o número da opção desejada:\n')

print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')

abertura = input('Digite sua opção (1/2/3/4): ')

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if abertura == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif abertura == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif abertura == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif abertura == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("\nOpção Inválida!")