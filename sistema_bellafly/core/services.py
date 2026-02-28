from itertools import chain
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from core.models.products import (
    Roupa,
    Acessorio,
    KitBeleza,
    Perfumaria,
    Produto,
    ConjuntoRoupa
)


CATEGORY_MODEL_MAP = {
    "roupas": Roupa,
    "acessorios": Acessorio,
    "kits": KitBeleza,
    "perfumaria": Perfumaria,
    "diversos": Produto,
}


def get_products_by_category(categoria: str):
    model = CATEGORY_MODEL_MAP.get(categoria, Perfumaria)
    return model.objects.filter(ativo=True).order_by("nome")


def search_all_products(query: str):
    roupas = Roupa.objects.filter(ativo=True, nome__icontains=query)
    conjuntos = ConjuntoRoupa.objects.filter(ativo=True, nome__icontains=query)
    kits = KitBeleza.objects.filter(ativo=True, nome__icontains=query)
    perfumaria = Perfumaria.objects.filter(ativo=True, nome__icontains=query)
    diversos = Produto.objects.filter(ativo=True, nome__icontains=query)

    return sorted(
        list(chain(roupas, conjuntos, kits, perfumaria, diversos)),
        key=lambda x: x.nome.lower()
    )


def paginate_queryset(queryset, page_number, per_page=8):
    paginator = Paginator(queryset, per_page)

    try:
        produtos = paginator.page(page_number)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return produtos, paginator


def build_page_range(produtos, paginator):
    current_page = produtos.number
    total_pages = paginator.num_pages

    if total_pages <= 7:
        return list(range(1, total_pages + 1))

    if current_page <= 4:
        return list(range(1, 6)) + ["...", total_pages]

    if current_page >= total_pages - 3:
        return [1, "..."] + list(range(total_pages - 4, total_pages + 1))

    return [1, "..."] + list(range(current_page - 2, current_page + 3)) + ["...", total_pages]