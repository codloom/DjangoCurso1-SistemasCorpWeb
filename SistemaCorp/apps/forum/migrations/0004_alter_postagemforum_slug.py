# Generated by Django 4.2.2 on 2023-08-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_postagemforum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagemforum',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]