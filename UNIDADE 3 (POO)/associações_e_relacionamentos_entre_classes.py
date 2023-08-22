"""

Associações e relacionamentos entre classes referem-se à maneira como as classes interagem 
e se conectam umas com as outras em um sistema orientado a objetos. Isso envolve a criação 
de conexões significativas entre diferentes classes para representar a colaboração e a 
dependência entre objetos.

Existem vários tipos de relacionamentos, incluindo:

Associação: É um relacionamento geral onde uma classe está associada a outra de alguma forma. 
sso pode ser uma associação simples ou mais complexa, onde uma classe depende da outra para cumprir 
uma função.

Agregação: Representa uma associação em que uma classe contém ou "agrega" outras classes como 
parte de sua estrutura, mas as classes agregadas podem existir independentemente.

Composição: Semelhante à agregação, mas as classes agregadas não podem existir independentemente 
e estão intrinsicamente ligadas à classe principal.
"""

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ensinar(self):
        return "Ensinando a matéria."

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor  # Associação com a classe Professor

    def apresentar(self):
        return f"A disciplina {self.nome} é ministrada por {self.professor.nome}."

# Criando objetos a partir das classes Professor e Disciplina
professor = Professor("João")
disciplina = Disciplina("Matemática", professor)

# Chamando métodos nos objetos
print(professor.ensinar())  # Saída: Ensinando a matéria.
print(disciplina.apresentar())  # Saída: A disciplina Matemática é ministrada por João.
"""
No exemplo acima, a classe Disciplina tem uma associação com a classe Professor. 
Um objeto da classe Professor é passado como um atributo para a classe Disciplina. 
Isso reflete um relacionamento onde uma disciplina é ministrada por um professor.

Observe que esse é um exemplo simples de associação. Em cenários mais complexos, 
as associações podem envolver várias classes interagindo para formar um sistema mais abrangente.
"""