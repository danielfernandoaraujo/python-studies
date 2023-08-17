"""
O Quick Sort é outro algoritmo de ordenação eficiente que utiliza a estratégia 
"dividir para conquistar". Ele seleciona um elemento da lista como um "pivô", 
reorganiza os elementos de forma que os elementos menores que o pivô estejam à 
sua esquerda e os elementos maiores estejam à sua direita. 
Em seguida, o algoritmo é aplicado recursivamente nas sub-listas à esquerda e à direita do pivô.
"""

#1.   Escolha do Pivô: Um elemento é escolhido da lista como o pivô. 
#     Isso pode ser feito de várias maneiras, como escolher o primeiro, o último ou um elemento     
#     aleatório.

#2.   Particionamento: Os elementos da lista são reorganizados de forma que todos os elementos 
#     menores que o pivô estejam à sua esquerda e todos os elementos maiores estejam à sua direita. 
#     O pivô está agora em sua posição final.

#3.   Recursão: O Quick Sort é aplicado recursivamente nas sub-listas à esquerda e 
#     à direita do pivô. Isso é feito até que todas as sub-listas contenham apenas um elemento, 
#     o que significa que a lista está totalmente ordenada.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Escolhendo o pivô como o elemento do meio
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Exemplo de uso
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print(sorted_arr)
