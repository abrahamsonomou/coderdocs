# Generated by Django 4.0.6 on 2022-09-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0011_alter_customuser_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.TextField(blank=True, choices=[('autre', 'Autre'), ('master', 'Master'), ('licence', 'Licence'), ('bts', 'BTS'), ('doctorat', 'Doctorat')], null=True, verbose_name='Grade'),
        ),
    ]
