from django.contrib import admin
from django.contrib.auth.models import User, Group
from clientes.models import Clientes
import csv
from django.http import HttpResponse


admin.site.unregister(User)
admin.site.unregister(Group)

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
    list_display = ("nome","tipo","documento","telefone","email","criado")
    search_fields = ("nome","documento","email","telefone",)
    list_filter = ("nome", "tipo",)
    ordering = ("nome","criado")
    list_per_page = 30

    actions = ["export_as_csv"]
