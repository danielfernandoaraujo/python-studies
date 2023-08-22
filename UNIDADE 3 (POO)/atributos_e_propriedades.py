"""
Atributos: Atributos são as características ou informações que um objeto possui. 
Eles são representados por variáveis dentro da classe e armazenam os dados 
que pertencem a cada objeto. Por exemplo, em uma classe "Pessoa", 
os atributos poderiam ser "nome", "idade" e "altura".

Métodos: Métodos são as ações que um objeto pode realizar. 
Eles são funções definidas na classe que permitem que os objetos 
executem tarefas específicas ou realizem operações sobre seus atributos. 
Por exemplo, em uma classe "Cachorro", os métodos poderiam ser "latir", "correr"
e "comer".

Aqui está um exemplo simples em Python para ilustrar esses conceitos:
"""

class Pessoa:
    def __init__(self, nome, idade):
        #SELF - Serve para se referir ao próprio objeto atual dentro de um método de uma classe.
        self.nome = nome  # Atributo
        self.idade = idade  # Atributo

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."  # Método

# Criando objetos a partir da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1.nome)  # Saída: João
print(pessoa2.idade)  # Saída: 30

print(pessoa1.cumprimentar())  # Saída: Olá, meu nome é João e tenho 25 anos.
print(pessoa2.cumprimentar())  # Saída: Olá, meu nome é Maria e tenho 30 anos.
