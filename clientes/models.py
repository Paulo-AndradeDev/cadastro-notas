from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms



class PessoaTipo(models.TextChoices):
	FISICA = 'PF', _('Pessoa Física')
	JURIDICA = 'PJ', _('Pessoa Jurídica')

class Clientes(models.Model):
	nome = models.CharField('Nome Completo',max_length=100)
	tipo = models.CharField('Tipo',max_length=2,choices=PessoaTipo.choices,default=PessoaTipo.JURIDICA)
	documento = models.CharField('Nº do documento',max_length=20,null=True,blank=True)
	telefone = models.CharField('Telefone',max_length=20,null=True,blank=True)
	email = models.EmailField('Email',max_length=254,null=True,blank=True)
	endereco = models.TextField('Endereço',null=True,blank=True)
	criado = models.DateTimeField(auto_now_add=True,editable=False,null=True)
	atualizado = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name_plural = "Clientes"
		unique_together = ('nome','documento')

	def __str__(self):
		return self.nome
