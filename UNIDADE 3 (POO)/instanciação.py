"""
A instanciação é o processo de criar um objeto a partir de uma classe. 
Quando você instancia uma classe, você cria uma instância específica dessa classe, 
com seus próprios atributos e métodos.

Em outras palavras, a instanciação envolve criar um objeto concreto que segue as 
definições e comportamentos especificados pela classe.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objetos a partir da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Acessando os atributos dos objetos
print(pessoa1.nome, pessoa1.idade)  # Saída: João 25
print(pessoa2.nome, pessoa2.idade)  # Saída: Maria 30
"""
No exemplo acima, a classe Pessoa possui um construtor __init__ que é chamado durante 
a instanciação e inicializa os atributos nome e idade. Os objetos pessoa1 e pessoa2 são 
criados a partir da classe Pessoa com valores específicos para seus atributos.
"""