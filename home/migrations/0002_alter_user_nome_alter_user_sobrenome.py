# Generated by Django 4.1.5 on 2023-02-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]