from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Produto, Roupa, ConjuntoRoupa, KitBeleza, Perfumaria, Acessorio
from itertools import chain


from django.http import HttpResponse
from django.conf import settings
import os

def service_worker(request):
    sw_path = os.path.join(settings.BASE_DIR, 'global/static/service-worker.js')
    with open(sw_path, 'r') as f:
        return HttpResponse(f.read(), content_type='application/javascript')


from .services import (
    get_products_by_category,
    search_all_products,
    paginate_queryset,
    build_page_range
)


def product_list(request):
    categoria = request.GET.get("categoria", "perfumaria")
    page_number = request.GET.get("page", 1)

    queryset = get_products_by_category(categoria)
    produtos, paginator = paginate_queryset(queryset, page_number)
    page_range = build_page_range(produtos, paginator)

    context = {
        "produtos": produtos,
        "categoria": categoria,
        "query": "",
        "page_range": page_range,
        "current_page": produtos.number,
        "total_pages": paginator.num_pages,
    }

    return render(request, "blog/products.html", context)


def product_search(request):
    query = request.GET.get("q", "")
    page_number = request.GET.get("page", 1)

    if not query:
        return product_list(request)

    queryset = search_all_products(query)
    produtos, paginator = paginate_queryset(queryset, page_number)
    page_range = build_page_range(produtos, paginator)

    context = {
        "produtos": produtos,
        "categoria": "",
        "query": query,
        "page_range": page_range,
        "current_page": produtos.number,
        "total_pages": paginator.num_pages,
    }

    return render(request, "blog/products.html", context)