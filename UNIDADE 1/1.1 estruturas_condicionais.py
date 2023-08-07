#ESTRUTURAS CONDICIONAIS EM PYTHON: IF, ELIF, ELSE

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:   
    print("Código não cadastrado")

'''Em Python, não existe o comando switch. 
Para construir uma estrutura encadeada, devemos usar o comando "elif", 
que é uma abreviação de else if.'''