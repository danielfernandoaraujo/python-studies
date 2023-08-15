"""
Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor, 
permitindo que você associe valores a chaves únicas. Isso é extremamente útil 
quando você deseja armazenar e recuperar informações relacionadas a partir de uma chave específica.
"""

"""
Sintaxe: Dicionários são definidos usando chaves {}. 
Cada par chave-valor é separado por dois pontos : e os pares são separados por vírgulas. Exemplo:
"""
aluno = {
    "nome": "Alice",
    "idade": 25,
    "nota": 90
}

#Acesso a Valores: Você pode acessar os valores de um dicionário usando a chave correspondente:
nome = aluno["nome"]      # Acessa o valor associado à chave "nome"
idade = aluno["idade"]    # Acessa o valor associado à chave "idade"

"""
Adição e Modificação: Você pode adicionar novos pares chave-valor
ou modificar valores existentes em um dicionário:
"""
aluno["curso"] = "Engenharia"   # Adiciona um novo par chave-valor
aluno["idade"] = 26            # Modifica o valor associado à chave "idade"

"""
Remoção: Você pode remover um par chave-valor de um dicionário usando o operador del:
"""
del aluno["nota"]             # Remove o par chave-valor associado à chave "nota"

"""
Métodos de Dicionário: Dicionários possuem métodos úteis, como keys() para obter as chaves, 
values() para obter os valores e items() para obter os pares chave-valor como tuplas.

Iteração: Você pode iterar pelas chaves,
valores ou pares chave-valor de um dicionário usando loops for.

Chaves Imutáveis: As chaves de um dicionário devem ser imutáveis, 
o que significa que você pode usar strings, números, tuplas (contendo valores imutáveis)
 como chaves, mas não listas ou outros dicionários
"""

