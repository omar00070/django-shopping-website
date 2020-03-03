# Generated by Django 3.0.3 on 2020-03-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200302_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
    ]
