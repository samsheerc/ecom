# Generated by Django 5.0.1 on 2024-02-07 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]