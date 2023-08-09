'''
WHILE - deve ser utilizado para construir e controlar a estrutura decisão,
sempre que o número de repetições não seja conhecido.
'''

numero = 1
while numero != 0:
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        print('Número par!')
    else:
        print('Número impar!')

'''
FOR - uma forma de percorrer uma lista (ou coleção de itens) e executar uma ação para cada item da lista.
É como se você tivesse uma lista de coisas, e quisesse fazer algo com cada uma delas, uma após a outra.
'''

numeros = [1, 2, 3, 4, 5]

soma = 0  # Inicializa a variável "soma" com o valor zero

for numero in numeros:
    soma += numero
    # A cada iteração, o número atual da lista é adicionado à variável "soma"

print("A soma dos números é:", soma)


