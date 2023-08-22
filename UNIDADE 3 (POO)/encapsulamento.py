"""
O encapsulamento é um conceito que envolve a proteção e o 
controle do acesso aos atributos e métodos de uma classe. 
Ele ajuda a garantir que os detalhes internos da implementação da classe sejam ocultados e 
que o acesso aos membros da classe seja feito de forma controlada.

Em Python, você pode usar convenções de nomenclatura para indicar a 
visibilidade dos membros da classe:

Atributos e métodos com nomes que começam com um único sublinhado (_):
    São considerados "privados" e devem ser acessados apenas dentro da classe ou de subclasses.
Atributos e métodos com nomes que começam com dois sublinhados (__):
    Têm seu nome "manglado" para evitar conflitos de nomes em subclasses, mas ainda podem ser acessados.
Aqui está um exemplo que ilustra o encapsulamento em Python:
"""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo

# Criando um objeto a partir da classe ContaBancaria
conta = ContaBancaria("João", 1000)

# Tentando acessar diretamente o atributo privado (__saldo)
# Isso não é recomendado, pois __saldo é privado
print(conta.__saldo)  # Isso resultará em um erro de atributo

# Acessando o saldo por meio de um método público
print(conta.get_saldo())  # Saída: 1000

# Depositando dinheiro na conta
conta.depositar(500)
print(conta.get_saldo())  # Saída: 1500

# Sacando dinheiro da conta
conta.sacar(200)
print(conta.get_saldo())  # Saída: 1300

"""
No exemplo acima, os atributos __titular e __saldo são encapsulados, tornando-os privados. O acesso a esses atributos é feito por meio dos métodos públicos get_saldo, depositar e sacar.
"""