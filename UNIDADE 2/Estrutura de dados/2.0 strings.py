'''
O que é uma String?
Uma string é uma sequência de caracteres. 
Ela pode conter letras, números, símbolos e espaços. 
Em Python, as strings são representadas entre aspas simples (' ') ou aspas duplas (" "). Por exemplo:
'''
nome = 'João'
frase = "Olá, mundo!"

'''
Indexação e Fatiamento:
Assim como outras sequências, as strings podem ser indexadas e fatiadas. 
A indexação começa em 0 para o primeiro caractere e aumenta à medida que você avança na string. 
Você também pode usar índices negativos para contar a partir do final da string. Exemplo:
'''
texto = "Python é incrível"
primeiro_caractere = texto[0]       # 'P'
ultimo_caractere = texto[-1]        # 'l'

'''
O fatiamento permite extrair partes específicas da string:
'''
parte = texto[7:10]                 # 'é '

'''
Métodos de String:
Python fornece uma variedade de métodos embutidos para manipular strings. 
Alguns exemplos úteis incluem:
'''
texto = "python é divertido"
maiusculo = texto.upper()           # 'PYTHON É DIVERTIDO'
minusculo = texto.lower()           # 'python é divertido'
capitalizado = texto.capitalize()   # 'Python é divertido'

'''
Métodos de String:
Python fornece uma variedade de métodos embutidos para manipular strings. 
Alguns exemplos úteis incluem:
'''
saudacao = "Olá"
nome = "Maria"
mensagem = saudacao + ", " + nome + "!"  # 'Olá, Maria!'
repeticao = saudacao * 3              # 'OláOláOlá'
formatado = "Meu nome é {}".format(nome)  # 'Meu nome é Maria'

'''
A partir do Python 3.6, você pode usar f-strings para formatar strings de maneira mais conveniente:
'''
formatado_f = f"Meu nome é {nome}"   # 'Meu nome é Maria'

'''
Escapando Caracteres:
Alguns caracteres têm significados especiais em strings, como as aspas. 
Para incluí-los em uma string, você pode usar a barra invertida () para escapar o caractere:
'''
texto_com_aspas = "Ele disse, \"Olá!\"" 

'''
Comprimento da String:
O comprimento de uma string pode ser obtido usando a função len():
'''
comprimento = len("Python")          # 6

'''
Divisão e Junção de Strings:
Você pode dividir uma string em substrings com base em um caractere específico usando o método split()
 e, em seguida, unir essas substrings usando o método join():
'''
frase = "Python é uma linguagem de programação"
palavras = frase.split()          # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação'] #cria uma lista
nova_frase = " ".join(palavras)   # 'Python é uma linguagem de programação'


