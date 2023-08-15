"""
A busca linear é um método simples de encontrar um elemento específico em uma lista ou array em Python.
Nesse método, cada elemento da lista é verificado sequencialmente até que o elemento 
desejado seja encontrado ou até que toda a lista seja percorrida. 
"""
# exemplo:


def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna o índice onde o elemento foi encontrado
    return -1  # Retorna -1 se o elemento não for encontrado na lista


# Exemplo de uso
minha_lista = [10, 5, 8, 2, 15, 7]
elemento_procurado = 15

indice = busca_linear(minha_lista, elemento_procurado)

if indice != -1:
    print(
        f"O elemento {elemento_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {elemento_procurado} não foi encontrado na lista.")


"""
Nesse exemplo, a função `busca_linear` percorre cada elemento da lista até encontrar o 
elemento desejado ou percorrer toda a lista. 
Se o elemento for encontrado, o índice onde ele está é retornado; 
caso contrário, é retornado -1 para indicar que o elemento não está na lista.
"""

"""
É importante notar que a busca linear pode ser ineficiente para listas muito grandes, 
pois precisa percorrer todos os elementos, resultando em uma complexidade de tempo linear O(n), 
onde 'n' é o tamanho da lista. Para listas ordenadas, a busca binária é uma alternativa mais eficiente.
"""
