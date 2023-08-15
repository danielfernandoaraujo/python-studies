"""
Um set (conjunto) em Python é uma coleção desordenada de elementos únicos.
Isso significa que um conjunto não permite duplicatas 
e não mantém uma ordem específica dos elementos.
"""

# Criação: Sets são definidos usando chaves {} ou usando a função set(). Exemplo: 
numeros = {1, 2, 3, 4, 5}
letras = set(['a', 'b', 'c'])

"""
Elementos Únicos: Os sets não podem conter elementos duplicados. 
Se você adicionar um elemento repetido, ele será ignorado.

Sem Ordem: Os elementos de um set não têm uma ordem específica, 
o que significa que você não pode acessá-los por índice.

Operações de Conjuntos: Sets suportam operações de conjunto, 
como união, interseção e diferença.
"""

A = {1, 2, 3}
B = {3, 4, 5}
uniao = A | B              # União: {1, 2, 3, 4, 5}
intersecao = A & B         # Interseção: {3}
diferenca = A - B          # Diferença: {1, 2}

#Métodos de Conjunto: Sets têm métodos para adicionar, remover e verificar elementos.

conjunto = {1, 2, 3}
conjunto.add(4)             # Adiciona o elemento 4
conjunto.remove(2)          # Remove o elemento 2
contem = 3 in conjunto     # Verifica se o conjunto contém 3

"""
Uso Comum: Sets são frequentemente usados para remover duplicatas de listas
e para verificar associações únicas entre elementos.

Iteração: Você pode iterar através dos elementos de um set usando um loop for.

Imutabilidade dos Elementos: Os elementos em um set devem ser imutáveis, 
o que significa que você não pode ter listas ou outros sets como elementos de um set.
"""
   