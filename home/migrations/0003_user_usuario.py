# Generated by Django 4.1.5 on 2023-02-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_nome_alter_user_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usuario',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]