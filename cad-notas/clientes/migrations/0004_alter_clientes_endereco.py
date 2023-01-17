import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_clientes_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='endereco',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Endereço completo'),
        ),
    ]
