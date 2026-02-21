from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Produto, Roupa, ConjuntoRoupa, KitBeleza, Perfumaria, Acessorio
from itertools import chain


from django.http import HttpResponse
from django.conf import settings
import os

def service_worker(request):
    sw_path = os.path.join(settings.BASE_DIR, 'static/service-worker.js')
    with open(sw_path, 'r') as f:
        return HttpResponse(f.read(), content_type='application/javascript')


def index(request):
    categoria = request.GET.get('categoria', 'perfumaria')
    query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    
    if query:  
       
        roupas = Roupa.objects.filter(ativo=True, nome__icontains=query)
        conjuntos = ConjuntoRoupa.objects.filter(ativo=True, nome__icontains=query)
        kits = KitBeleza.objects.filter(ativo=True, nome__icontains=query)
        perfumaria = Perfumaria.objects.filter(ativo=True, nome__icontains=query)
        diversos = Produto.objects.filter(ativo=True, nome__icontains=query)
        
        produtos_list = sorted(
            list(chain(roupas, conjuntos, kits, perfumaria, diversos)),
            key=lambda x: x.nome.lower()
        )
    else:
       
        if categoria == 'roupas':
            produtos_list = list(Roupa.objects.filter(ativo=True).order_by('nome'))
        elif categoria == 'acessorios':
            produtos_list = list(Acessorio.objects.filter(ativo=True).order_by('nome'))
        elif categoria == 'kits':
            produtos_list = list(KitBeleza.objects.filter(ativo=True).order_by('nome'))
        elif categoria == 'perfumaria':
            produtos_list = list(Perfumaria.objects.filter(ativo=True).order_by('nome'))
        elif categoria == 'diversos':
            produtos_list = list(Produto.objects.filter(ativo=True).order_by('nome'))
        else:
            produtos_list = list(Perfumaria.objects.filter(ativo=True).order_by('nome'))
    
    paginator = Paginator(produtos_list, 9)  # 10 produtos por página
    
    try:
        produtos = paginator.page(page_number)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)
    
    page_range = []
    current_page = produtos.number
    total_pages = paginator.num_pages
    
    if total_pages <= 7:
        page_range = list(range(1, total_pages + 1))
    else:
        if current_page <= 4:
            page_range = list(range(1, 6)) + ['...', total_pages]
        elif current_page >= total_pages - 3:
            page_range = [1, '...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = [1, '...'] + list(range(current_page - 2, current_page + 3)) + ['...', total_pages]
    
    context = {
        'produtos': produtos,
        'categoria': categoria,
        'query': query if query else '',
        'page_range': page_range,
        'current_page': current_page,
        'total_pages': total_pages,
    }
    return render(request, 'index.html', context)