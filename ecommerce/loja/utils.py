from django.db.models import Max, Min

def filtrar_produtos(produtos, filtro):
    if filtro:
        if "-" in filtro:
            categoria, tipo = filtro.split("-")
            produtos = produtos.filter(
                tipo__slug=tipo, categoria__slug=categoria)
        else:
            produtos = produtos.filter(categoria__slug=filtro)

    return produtos


def preco_minimo_maximo(produtos):
    maximo = 0
    minimo = 0
    if len(produtos) > 0:
        maximo = list(produtos.aggregate(Max("preco")).values())[0]
        maximo = round(maximo, 2)
        minimo = list(produtos.aggregate(Min("preco")).values())[0]
        minimo = round(minimo, 2)

    return minimo, maximo