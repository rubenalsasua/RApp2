# Generated by Django 5.1.6 on 2025-02-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RApp2", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="etiqueta",
            name="proyecto",
        ),
        migrations.AddField(
            model_name="proyecto",
            name="etiqueta",
            field=models.ManyToManyField(related_name="etiquetas", to="RApp2.etiqueta"),
        ),
    ]
