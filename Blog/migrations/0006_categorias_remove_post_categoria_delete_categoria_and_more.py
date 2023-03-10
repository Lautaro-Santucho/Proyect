# Generated by Django 4.1.7 on 2023-03-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_categoria_remove_post_cates_delete_categorias_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='cates',
            field=models.ManyToManyField(to='Blog.categorias'),
        ),
    ]
