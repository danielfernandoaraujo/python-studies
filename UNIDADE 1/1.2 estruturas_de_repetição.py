'''
Em Python, o while é uma estrutura de controle que permite executar um bloco de código 
repetidamente enquanto uma determinada condição for verdadeira. 
Em outras palavras, ele cria um loop que executa as instruções dentro do bloco de código 
enquanto a expressão booleana especificada for avaliada como verdadeira. 
Assim que a condição se torna falsa, a execução do loop é interrompida e o 
programa continua com o código após o bloco while.
'''
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1


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


