# Generated by Django 4.1.7 on 2023-03-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0007_alter_servicios_contenido_alter_servicios_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]