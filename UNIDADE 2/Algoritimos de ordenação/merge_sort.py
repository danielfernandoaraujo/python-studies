'''
O Merge Sort é um algoritmo de ordenação eficiente que utiliza a abordagem de 
"dividir para conquistar". Ele divide a lista não ordenada em sublistas menores, 
ordena essas sublistas e, em seguida, combina as sublistas ordenadas para obter a lista final ordenada. 
Esse processo de divisão, ordenação e mesclagem é repetido até que toda a lista esteja ordenada.
'''

#1. Divisão: A lista original é dividida recursivamente em duas sublistas até que cada sublista 
#   contenha apenas um elemento. Isso é feito dividindo repetidamente a lista ao meio.

#2. Ordenação: Uma vez que as sublistas tenham sido reduzidas a um único elemento, 
#   elas já estão ordenadas por definição.

#3. Mesclagem: Agora, as sublistas ordenadas são mescladas. 
#   Nesse processo de mesclagem, duas sublistas ordenadas são combinadas para formar uma 
#   única lista ordenada. Isso é feito comparando o primeiro elemento de cada sublista e 
#   escolhendo o menor entre eles para adicionar à lista final. O processo de 
#   comparação e adição continua até que todas as sublistas tenham sido completamente mescladas.

def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

    
def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada


lista = [10, 9, 5, 8, 11, -1, 3]
executar_merge_sort(lista)
