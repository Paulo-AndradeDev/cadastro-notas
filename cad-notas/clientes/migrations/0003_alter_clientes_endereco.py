# Generated by Django 3.2.16 on 2023-01-12 13:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20230112_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='endereco',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
