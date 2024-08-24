from .models import Pedido, ItensPedido, Categoria, Tipo


def carrinho(request):
    quantidade_produtos_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente

    else:
        return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}
    
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)

    # Quantos produtos tem no pedido do usuário
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_produtos_carrinho += item.quantidade
        
    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}


def categorias_tipos(request):
    categorias_navegacao = Categoria.objects.all()
    tipos_navegacao = Tipo.objects.all()
    return {"categorias_navegacao": categorias_navegacao, "tipos_navegacao": tipos_navegacao}