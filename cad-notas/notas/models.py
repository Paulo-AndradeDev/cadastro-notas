from django.db import models
from django.utils.translation import gettext_lazy as _
from clientes.models import Clientes


class Notas(models.Model):
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	nota = models.CharField('Número',max_length=22,null=True)
	lancado = models.BooleanField('Emitida?',default=False,null=False)
	data = models.DateField('Data de Emissão',null=True)
	criado = models.DateTimeField(auto_now_add=True,editable=False)
	atualizado = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = "Nota Fiscal"
		verbose_name_plural = "Notas Fiscais"

	def __str__(self):
		return self.nota
