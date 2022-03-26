# Calculadora em Python

# Curso Python Fundamentos para Análise de Dados da Data Science Academy
# Desenvolvida em Python a partir do que foi aprendido nos capítulos 2 e 3
# Autora: Karla B S Oliveira
# Data: 26 de março de 2022

#Inicio do script
print("\n******************* Python Calculator *******************")

#Funções usadas na culcuradora: soma, subtração, multiplicação e divisão, respectivamente.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#Aviso para escolha da operação desejada
print('\nSelecione o número da opção desejada:\n')

print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')

#Input da opção desejada
abertura = input('Digite sua opção (1/2/3/4): ')

#Input dos números
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

#O que acontecerá após a inserção dos números e escolha da operação 
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

#Em caso de inserção de opção de operação inválida
else:
    print("\nOpção Inválida!")