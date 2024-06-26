# Generated by Django 5.0.3 on 2024-03-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('post', '0002_post_categoria_post_imagem_post_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='criarPostagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=100)),
                ('mensagem', models.TextField()),
                ('autor', models.CharField(default='', max_length=100)),
                ('data_postagem', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(to='categorias.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
