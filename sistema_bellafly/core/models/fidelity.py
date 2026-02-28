from django.db import models

from django.utils import timezone

class CheckboxSell(models.Model):
    nome = models.CharField(max_length=200, default="Cliente")
    email = models.EmailField(unique=False, null=True, blank=True)
    
    checkbox_1 = models.BooleanField(default=False, verbose_name="Venda 1")
    data_checkbox_1 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 1")
    
    checkbox_2 = models.BooleanField(default=False, verbose_name="Venda 2")
    data_checkbox_2 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 2")
    
    checkbox_3 = models.BooleanField(default=False, verbose_name="Venda 3")
    data_checkbox_3 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 3")
    
    checkbox_4 = models.BooleanField(default=False, verbose_name="Venda 4")
    data_checkbox_4 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 4")
    
    checkbox_5 = models.BooleanField(default=False, verbose_name="Venda 5")
    data_checkbox_5 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 5")
    
    checkbox_6 = models.BooleanField(default=False, verbose_name="Venda 6")
    data_checkbox_6 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 6")
    
    checkbox_7 = models.BooleanField(default=False, verbose_name="Venda 7")
    data_checkbox_7 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 7")
    
    checkbox_8 = models.BooleanField(default=False, verbose_name="Venda 8")
    data_checkbox_8 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 8")
    
    checkbox_9 = models.BooleanField(default=False, verbose_name="Venda 9")
    data_checkbox_9 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 9")
    
    checkbox_10 = models.BooleanField(default=False, verbose_name="Venda 10")
    data_checkbox_10 = models.DateTimeField(null=True, blank=True, verbose_name="Data Venda 10")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nome} - {self.created_at.strftime('%d/%m/%Y')}"
    
    def save(self, *args, **kwargs):
        # Verifica quais checkboxes foram marcados e atualiza as datas
        for i in range(1, 11):
            checkbox_field = f'checkbox_{i}'
            data_field = f'data_checkbox_{i}'
            
            # Se o checkbox foi marcado e não tinha data ainda
            if getattr(self, checkbox_field) and not getattr(self, data_field):
                setattr(self, data_field, timezone.now())
                print(f"✅ CHECKPOINT {i} CONCLUÍDO! Data: {timezone.now().strftime('%d/%m/%Y %H:%M:%S')}")
            
            # Se o checkbox foi desmarcado, remove a data
            elif not getattr(self, checkbox_field) and getattr(self, data_field):
                setattr(self, data_field, None)
                print(f"❌ CHECKPOINT {i} DESMARCADO!")
        
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'fidelity'
        verbose_name = "Cartão Fidelidade"
        verbose_name_plural = "Cartão Fidelidade"

