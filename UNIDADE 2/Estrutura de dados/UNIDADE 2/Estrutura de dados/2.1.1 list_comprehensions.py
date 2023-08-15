'''
List Comprehensions são uma maneira curta e poderosa de criar listas em Python. 
Elas são usadas quando você deseja criar uma nova lista 
aplicando uma operação a cada elemento de outra lista (ou sequência) 
ou filtrando os elementos com base em uma condição.
'''

'''
Suponha que você queira criar 
uma lista com os quadrados dos números de 1 a 5 usando uma List Comprehension:
'''

quadrados = [x**2 for x in range(1, 6)]

# A expressão é x**2, que calcula o quadrado de cada número x.
# A iteração percorre x em range(1, 6), ou seja, os números de 1 a 5.
# Não há parte de filtragem aqui, pois estamos pegando todos os números da sequência.
# Então, o resultado será a lista [1, 4, 9, 16, 25], que são os quadrados dos números de 1 a 5.