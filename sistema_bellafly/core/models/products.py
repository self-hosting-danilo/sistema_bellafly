from django.db import models

class ProdutoBase(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        app_label = 'products'
        abstract = True

    def __str__(self):
        return self.nome

class Roupa(ProdutoBase):
    TAMANHO_CHOICES = [
        ('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG'),
    ]
    tamanho = models.CharField(max_length=2, choices=TAMANHO_CHOICES)
    cor = models.CharField(max_length=50)

    class Meta:
        app_label = 'products'

class ConjuntoRoupa(ProdutoBase):
    roupas = models.ManyToManyField(Roupa, related_name='conjuntos')

    class Meta:
        app_label = 'products'

class KitBeleza(ProdutoBase):
    produtos = models.ManyToManyField('Produto', related_name='kits_beleza')

    class Meta:
        app_label = 'products'

class Perfumaria(ProdutoBase):
    fragrancia = models.CharField(max_length=100)
    volume_ml = models.PositiveIntegerField()

    class Meta:
        app_label = 'products'

class Acessorio(ProdutoBase):
    pass

class Produto(ProdutoBase):
    pass
