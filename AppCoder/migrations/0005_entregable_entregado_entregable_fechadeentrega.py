# Generated by Django 4.2.4 on 2023-08-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_entregable_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='entregado',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='entregable',
            name='fechaDeEntrega',
            field=models.DateField(null=True),
        ),
    ]
