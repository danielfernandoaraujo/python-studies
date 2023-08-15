"""
 Um array NumPy é uma estrutura de dados usada em Python 
 para armazenar e manipular arrays multidimensionais de elementos, como números. 
 Ele é fornecido pela biblioteca NumPy, 
 que é amplamente utilizada para computação científica e análise de dados.
"""

"""
O que é um Array NumPy? Um array NumPy é uma grade retangular de elementos do mesmo tipo.
Pode ter uma ou várias dimensões, como um vetor (1D), uma matriz (2D) 
ou até mesmo arrays com mais dimensões.

Vantagens: Os arrays NumPy oferecem vantagens em relação às listas padrão do Python, 
como melhor desempenho e recursos de operações matemáticas mais avançadas.

Criação: Você pode criar um array NumPy passando uma sequência (como uma lista) para a função 
numpy.array(). Exemplo:
"""
import numpy as np

numeros = np.array([1, 2, 3, 4, 5])

"""
Indexação: A indexação em arrays NumPy é semelhante a listas, 
mas você pode ter várias dimensões. Por exemplo, para acessar o elemento em uma matriz 2D:
"""
matriz = np.array([[1, 2, 3], [4, 5, 6]])
elemento = matriz[1, 2]  # Acessa o elemento da segunda linha e terceira coluna (valor 6)

"""
Operações: Os arrays NumPy suportam operações elementares, 
como adição, multiplicação, etc., que são aplicadas a cada elemento do array.

Funções NumPy: A biblioteca NumPy oferece muitas funções úteis para realizar 
operações matemáticas em arrays, como np.sum(), np.mean(), np.max(), entre outras.

Broadcasting: NumPy permite que você realize operações entre arrays
de diferentes formas de maneira eficiente, usando o conceito de broadcasting.
"""
