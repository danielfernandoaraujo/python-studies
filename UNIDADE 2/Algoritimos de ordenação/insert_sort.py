"""
O algoritmo de ordenação Insertion Sort (ordenação por inserção)
 é um método simples de ordenar uma lista de elementos. 
 Ele funciona construindo uma parte ordenada da lista à medida que percorre os elementos 
 não ordenados, inserindo cada um deles na posição correta na parte ordenada.
"""

# 1.  A primeira etapa do algoritmo começa considerando o primeiro 
#     elemento da lista como uma parte ordenada de um único elemento.

# 2.  Em seguida, o algoritmo avança para o próximo elemento não ordenado.

# 3 . Para cada elemento não ordenado, o algoritmo compara esse elemento com os elementos na parte ordenada da lista, começando pelo último elemento.

# 4 . Enquanto o elemento na parte ordenada for maior do que o elemento não ordenado, o elemento na parte ordenada é deslocado uma posição à frente.

# 5 . Quando é encontrado um elemento na parte ordenada que é menor ou igual ao elemento não ordenado, o elemento não ordenado é inserido na posição imediatamente após esse elemento.

# 6 . Esse processo continua até que todos os elementos não ordenados sejam inseridos na parte ordenada da lista, resultando na lista completamente ordenada.

def insert_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1 
        lista[j+1] = chave

lista_teste1 = [1, 132, 1323, 123, 324, 2, 4, 12, 4, 51, 412, 41, 221, 14, 12, 532, 243, 12, 93]

insert_sort(lista_teste1)

print(f"\nLista desordenada = {lista_teste1}")