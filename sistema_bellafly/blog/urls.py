from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('buscar/', views.product_search),
    path('service-worker.js', views.service_worker, name='service-worker'),
]