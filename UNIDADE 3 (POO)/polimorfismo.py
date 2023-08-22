"""
O polimorfismo é um conceito que permite que diferentes classes compartilhem uma mesma interface ou comportamento, mas implementem esse comportamento de maneira diferente. Isso permite tratar objetos de diferentes classes de maneira uniforme, simplificando o código e promovendo a flexibilidade.

Em outras palavras, o polimorfismo permite que objetos de classes diferentes possam ser tratados como objetos de uma classe mais genérica (como uma classe base) e ainda assim executar métodos específicos de suas próprias classes.

Aqui está um exemplo de polimorfismo em Python:
"""
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Função que recebe um objeto Animal e chama o método fazer_som
def fazer_barulho(animal):
    return animal.fazer_som()

# Criando objetos a partir das classes derivadas
cachorro = Cachorro()
gato = Gato()

# Usando a função fazer_barulho com diferentes objetos
print(fazer_barulho(cachorro))  # Saída: Au au!
print(fazer_barulho(gato))  # Saída: Miau!
"""
No exemplo acima, as classes Cachorro e Gato herdam da classe Animal e 
implementam o método fazer_som de maneira diferente.
A função fazer_barulho recebe um objeto Animal como parâmetro e chama o 
método fazer_som do objeto passado. Isso ilustra o polimorfismo, onde diferentes 
tipos de objetos podem ser tratados de maneira uniforme.
 """