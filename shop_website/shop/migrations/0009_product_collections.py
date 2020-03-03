# Generated by Django 3.0.3 on 2020-03-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200302_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='shop.Collection'),
            preserve_default=False,
        ),
    ]
