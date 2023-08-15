"""
O Selection Sort é um algoritmo de ordenação simples e de complexidade quadrática. 
Ele funciona selecionando repetidamente o menor elemento da lista não ordenada e 
trocando-o com o primeiro elemento não ordenado. Esse processo é repetido até que toda 
a lista esteja ordenada.
"""

def selection_sort(lista):
    n = len(lista)
    for j in range(n):
        min_index = j
        for i in range(j,n):
                if lista[i] < lista[min_index]:
                    min_index = i
        if lista[j] > lista[min_index]:
            lista[j], lista[min_index] = lista[min_index], lista[j]

lista_teste1 = [1, 132, 1323, 123, 324, 2, 4, 12, 4, 51, 412, 41, 221, 14, 12, 532, 243, 12, 93]

selection_sort(lista_teste1)

print(f"\nLista desordenada = {lista_teste1}")