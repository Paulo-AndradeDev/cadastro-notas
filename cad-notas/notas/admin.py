from django.contrib import admin
from clientes.models import Clientes
from notas.models import Notas
import csv
from django.http import HttpResponse



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

@admin.register(Notas)
class NotasAdmin(admin.ModelAdmin,ExportCsvMixin):
    date_hierarchy = 'data'
    list_display = ("cliente","nota","lancado","data")
    list_filter = ("cliente", "nota", "lancado", "data")
    search_fields = ("nota","data")
    raw_id_fields = ("cliente",)
    ordering = ("data","nota","cliente",)



    actions = ["nota_emitida","export_as_csv"]

    def nota_emitida(self, request, queryset):
        queryset.update(lancado=True)

    nota_emitida.short_description = "Registrar Emissão de Nota"
