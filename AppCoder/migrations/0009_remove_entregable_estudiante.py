# Generated by Django 4.2.4 on 2023-08-29 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_alter_profesor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='estudiante',
        ),
    ]
