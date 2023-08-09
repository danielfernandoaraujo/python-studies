'''
rage() - é uma função que gera uma sequência de números.
 Ele pode ser usado em loops "for" para iterar sobre uma sequência específica de valores.
'''

 # Imprimir os números de 0 a 4
for num in range(5):
    print(num)

'''
BREAK - A instrução break é usada para sair de um loop "for" ou "while" de forma antecipada,
antes que o loop seja concluído.
 '''

numeros = [1, 2, 3, 4, 5]

for num in numeros:
    if num == 3:
        print("Número encontrado!")
        break

'''
A instrução continue é usada para pular a iteração atual de um loop "for" ou "while" e continuar 
com a próxima iteração. É útil quando queremos ignorar um elemento específico da iteração 
sem interromper completamente o loop.
'''

# Imprimir apenas os números pares da lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numeros:
    if num % 2 == 1:  # Se o número for ímpar
        continue
    print(num)

