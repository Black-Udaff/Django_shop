# Generated by Django 5.0.6 on 2024-06-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Картинка'),
        ),
    ]
