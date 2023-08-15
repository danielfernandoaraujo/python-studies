"""
A busca binária é um algoritmo de busca eficiente utilizado para encontrar um elemento específico 
em uma lista ordenada. Ao contrário da busca linear, que percorre os elementos sequencialmente, 
a busca binária divide repetidamente a lista ao meio e compara o elemento desejado com o elemento do 
meio. Com base nessa comparação, a busca é direcionada para a metade superior ou inferior da lista, 
reduzindo pela metade o número de elementos a serem verificados a cada iteração. 
Aqui está um resumo sobre como implementar a busca binária em Python:
"""

def busca_binaria(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == elemento:
            return meio  # Retorna o índice onde o elemento foi encontrado
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1  # Retorna -1 se o elemento não for encontrado na lista

# Exemplo de uso
minha_lista = [2, 5, 7, 8, 10, 15]
elemento_procurado = 8

indice = busca_binaria(minha_lista, elemento_procurado)

if indice != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {elemento_procurado} não foi encontrado na lista.")


"""
Nesse exemplo, a função `busca_binaria` mantém uma janela delimitada pelos índices 
`esquerda` e `direita`, e o elemento médio entre esses índices é comparado com o elemento desejado. 
Com base na comparação, a janela é ajustada para a metade superior ou inferior da lista. 
Esse processo é repetido até que o elemento seja encontrado ou até que a janela se torne 
vazia (nesse caso, o elemento não está na lista).
"""

"""
A busca binária é altamente eficiente, pois a cada iteração a quantidade de elementos a 
serem verificados é reduzida pela metade. Isso resulta em uma complexidade de tempo de O(log n),
onde 'n' é o tamanho da lista. No entanto, é importante observar que a busca binária só é aplicável 
a listas ordenadas.
"""