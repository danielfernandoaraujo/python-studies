'''
O que é uma Lista?
Uma lista é uma estrutura de dados que pode conter uma coleção ordenada de itens. 
Esses itens podem ser de tipos diferentes, como números inteiros, números de ponto flutuante, 
strings e até outras listas. As listas em Python são mutáveis, 
o que significa que você pode adicionar, remover e modificar elementos após a criação.
'''

'''
Criando uma Lista:
Para criar uma lista, você pode utilizar colchetes [] e separar os elementos por vírgulas. 
Exemplo:
'''

numeros = [1, 2, 3, 4, 5]
nomes = ["Alice", "Bob", "Charlie"]
misturada = [1, "texto", 3.14, True]

'''
Acessando Elementos:
Os elementos de uma lista são acessados através de indexação, 
assim como em strings. A indexação começa em 0 para o primeiro elemento. 
Exemplo:
'''
primeiro_elemento = numeros[0]    # 1
ultimo_elemento = numeros[-1]      # 5

'''
Métodos de Lista:
Python fornece diversos métodos para manipular listas. 
Alguns exemplos úteis incluem:
'''
numeros.append(6)                 # Adiciona 6 no final da lista
nomes.insert(1, "David")          # Insere "David" na posição 1
misturada.remove("texto")         # Remove o elemento "texto"
tamanho = len(numeros)            # Retorna o tamanho da lista

''' 
Fatiamento de Listas:
Assim como strings, você pode fatiar listas para obter subconjuntos de elementos:
'''
sublista = numeros[1:4]           # [2, 3, 4]

'''
Concatenação e Repetição:
Você pode usar o operador de adição (+) para concatenar listas 
e o operador de multiplicação (*) para repeti-las:
'''
outra_lista = [7, 8, 9]
concatenada = numeros + outra_lista   # [1, 2, 3, 4, 5, 7, 8, 9]
repetida = numeros * 2                # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

'''
Ordenação e Reversão:
As listas podem ser ordenadas usando o método sort() e revertidas com o método reverse():
'''
numeros.sort()                 # Ordena a lista em ordem crescente
outra_lista.reverse()          # Inverte a ordem dos elementos

'''
Copiando Listas:
Ao atribuir uma lista a outra variável, 
você está apenas criando uma referência para a mesma lista. 
Para criar uma cópia independente, use o método copy() ou a operação de fatiamento completo:
'''
copia_lista = numeros.copy()    # Cria uma cópia independente
copia_fatiamento = numeros[:]   # Outra forma de criar cópia

'''
Iteração em Listas:
Você pode usar loops, como o loop for, para iterar através dos elementos de uma lista:
'''
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

'''
Operador in e not in:
O operador in verifica se um elemento está presente em uma lista, 
enquanto o operador not in verifica se um elemento não está presente:
'''
if "maçã" in frutas:
    print("Maçã está na lista")
if "uva" not in frutas:
    print("Uva não está na lista")

'''
Método extend():
O método extend() é usado para adicionar os elementos de outra lista à lista atual:
'''
primeira = [1, 2, 3]
segunda = [4, 5, 6]
primeira.extend(segunda)     # primeira agora é [1, 2, 3, 4, 5, 6]

'''
Método pop():
O método pop() remove e retorna um elemento específico da lista com base em seu índice. 
Se nenhum índice for fornecido, ele remove e retorna o último elemento:
'''
numeros = [10, 20, 30, 40]
valor = numeros.pop(1)       # Remove o elemento no índice 1 (20) e retorna-o

'''
Método count():
O método count() conta quantas vezes um determinado elemento aparece na lista:
'''
ocorrencias = numeros.count(10)   # Conta quantas vezes o número 10 aparece

'''
Limpeza de Listas:
Para esvaziar completamente uma lista, você pode usar o método clear():
'''
numeros.clear()             # Esvazia a lista numeros





