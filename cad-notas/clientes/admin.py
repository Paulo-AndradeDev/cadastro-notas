from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from clientes.models import Clientes
from notas.models import Notas
import csv
from django.http import HttpResponse


admin.site.unregister(User)
admin.site.unregister(Group)


class NotasInline(admin.TabularInline):
    model = Notas

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Gerar CSV"

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin,ExportCsvMixin):
<<<<<<< HEAD
    icon_name = 'people'
    
    list_display = ("nome","tipo","documento","telefone","email","criado")
=======
    list_display = ("nome","tipo","documento","telefone","email","criado",)
>>>>>>> a88faa461f0e1cc1829e8ebe1d98a6b6839ec192
    search_fields = ("nome","documento","email","telefone",)
    list_filter = ("nome", "tipo",)
    ordering = ("nome","criado")
    list_per_page = 30


    actions = ["export_as_csv"]

    # def total_notas_cliente(self, obj):
    #     parent = Clientes.objects.get(id=self.id)
    #     child_count = parent.Notas_set.count()
    #     print(child_count)

    inlines = [NotasInline]
