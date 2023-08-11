precos_produtos = [
    400,
    312,
    623, 
    10032,
    2304,
]

def aplicar_aumento(preco):
    if preco > 600:
        return preco * 1.5
    else:
        return preco
    
precos_produtos = list( #transforma em lista
    map(
        aplicar_aumento, precos_produtos #mapeia toda a lista e executa a função
    )
)
print(precos_produtos)

