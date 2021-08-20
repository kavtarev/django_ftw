# Generated by Django 3.2.6 on 2021-08-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_model',
            options={'verbose_name': 'tsatsaev', 'verbose_name_plural': 'kaki'},
        ),
        migrations.AlterField(
            model_name='news_model',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, verbose_name='изменен'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='header',
            field=models.CharField(max_length=151, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='news_model',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
    ]