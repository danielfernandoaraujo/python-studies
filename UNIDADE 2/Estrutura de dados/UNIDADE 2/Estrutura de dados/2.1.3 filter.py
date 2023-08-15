precos_produtos = [
    400,
    312,
    623, 
    10032,
    2304,
]

def aplicar_aumento(preco):
    if preco > 600:
        return True
    else:
        return False
    
precos_produtos = list( #transforma em lista
    filter(
        aplicar_aumento, precos_produtos 
        #mapeia toda a lista e diferente de map, ele não adiciona nada! Apenas filtra TRUE or FALSE e 
        #coloca na variavel 
    )
)
print(precos_produtos)

