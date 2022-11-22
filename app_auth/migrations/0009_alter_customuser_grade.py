# Generated by Django 4.0.6 on 2022-09-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0008_alter_customuser_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.TextField(blank=True, choices=[('bts', 'BTS'), ('master', 'Master'), ('licence', 'Licence'), ('doctorat', 'Doctorat'), ('autre', 'Autre')], null=True, verbose_name='Grade'),
        ),
    ]
