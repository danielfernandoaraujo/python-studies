#ESTRUTURAS LÓGICAS EM PYTHON: AND, OR, NOT
'''And - Retorna verdadeiro (True) se ambos os operandos forem verdadeiros. 
se um dos operandos for falso (False), o resultado será falso (False).'''
'''Or - Retorna verdadeiro (True) se pelo menos um dos operandos for verdadeiro. 
Se ambos os operandos forem falsos (False), o resultado será falso (False).'''
'''Not - Inverte o valor do operando. Se o operando for verdadeiro (True), o resultado será falso (False).
 Se o operando for falso (False), o resultado será verdadeiro (True).'''

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")