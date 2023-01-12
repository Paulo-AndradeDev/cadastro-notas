# Generated by Django 3.2.9 on 2023-01-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='atualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='clientes',
            unique_together={('nome', 'documento')},
        ),
    ]
