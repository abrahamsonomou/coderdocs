# Generated by Django 4.1 on 2022-08-05 09:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategorie',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('nom_categorie', models.CharField(max_length=100, verbose_name='Libelle')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Categorie',
            },
        ),
    ]