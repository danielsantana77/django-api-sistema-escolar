# Generated by Django 4.2.4 on 2023-08-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='numero',
            field=models.IntegerField(auto_created=True),
        ),
    ]
