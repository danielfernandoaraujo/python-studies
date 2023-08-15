"""
O Bubble Sort é um algoritmo de ordenação simples, porém ineficiente para listas grandes. 
Ele funciona comparando pares de elementos adjacentes na lista e trocando-os se estiverem fora de ordem.
Esse processo é repetido várias vezes até que nenhum par de elementos precise ser trocado, 
indicando que a lista está ordenada.
"""

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                #troca de lementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
        
lista_teste1 = [1, 132, 1323, 123, 324, 2, 4, 12, 4, 51, 412, 41, 221, 14, 12, 532, 243, 12, 93]

bubble_sort(lista_teste1)

print(f"\nLista desordenada = {lista_teste1}")