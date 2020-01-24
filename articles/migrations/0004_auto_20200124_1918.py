# Generated by Django 3.0.2 on 2020-01-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200124_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='articles.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.Article'),
        ),
    ]
