# Generated by Django 4.2.4 on 2023-08-28 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_entregable_entregado_entregable_fechadeentrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='estudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.estudiante'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entregable',
            name='entregado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='fechaDeEntrega',
            field=models.DateField(),
        ),
    ]
