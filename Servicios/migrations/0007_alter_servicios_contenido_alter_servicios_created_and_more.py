# Generated by Django 4.1.7 on 2023-03-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0006_alter_servicios_created_alter_servicios_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='contenido',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
