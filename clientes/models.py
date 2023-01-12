from django.db import models
from django.utils.translation import gettext_lazy as _

class PessoaTipo(models.TextChoices):
	FISICA = 'PF', _('Pessoa Física')
	JURIDICA = 'PJ', _('Pessoa Jurídica')

class Clientes(models.Model):

	nome = models.CharField(max_length=100)
   	# tipo = models.CharField(max_length=2,choices=PessoaTipo.choices,default=PessoaTipo.JURIDICA)
   	documento = models.CharField(max_length=20)
   	telefone = models.CharField(max_length=20)
   	endereco = models.TextField()
    
   	class Meta:
       	verbose_name_plural = "Clientes"

   	def __str__(self):
    	return self.nome
