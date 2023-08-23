"""
A herança é um conceito que permite criar uma nova classe (chamada de classe derivada ou subclasse)
com base em uma classe existente (chamada de classe base ou superclasse). 
A classe derivada herda os atributos e métodos da classe base e pode adicionar novos atributos e
métodos ou modificar os existentes.

A herança ajuda a promover a reutilização de código, permitindo que você defina uma estrutura 
geral na classe base e crie variações mais específicas nas classes derivadas.

Aqui está um exemplo de herança em Python:
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Criando objetos a partir das classes derivadas
cachorro = Cachorro("Rex")
gato = Gato("Felix")

# Chamando o método fazer_som nas classes derivadas
print(cachorro.fazer_som())  # Saída: Au au!
print(gato.fazer_som())  # Saída: Miau!

"""
No exemplo acima, a classe Animal é a classe base, e as classes Cachorro e Gato 
são classes derivadas que herdam da classe base. As classes derivadas implementam o método 
fazer_som de maneira específica, mas também herdam o atributo nome da classe base.
"""