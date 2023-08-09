print('Bem vindo a calculador magica!')

def somar (num1, num2, resultado):
    resultado = num1 + num2
    print(resultado)

def diminuir (num1, num2, resultado):
    resultado = num1 - num2
    print(resultado)

def dividir (num1, num2, resultado):
    resultado = num1 / num2
    print(resultado)

def multiplicar (num1, num2, resultado):
    resultado = num1 * num2
    print(resultado)

def calcular(num1, num2, resultado):
    if operacao == 'somar':
        somar(num1, num2, resultado)
    elif operacao == 'diminuir':
        diminuir(num1, num2, resultado)
    elif operacao == 'dividir':
        dividir(num1, num2, resultado)   
    elif operacao == 'multiplicar':
        multiplicar(num1, num2, resultado)
    else:
        print('Você escreveu errado, tente novamente!') 
        
    
num1 = int(input('Qual o primeiro numero que deseja calcular? '))
num2 = int(input('Qual o segundo numero que deseja calcular? '))
operacao = input('Escreva qual operação vai usar: (ex: somar, diminuir, dividir, multiplicar) ')       

calcular(num1, num2, operacao)
       



