# Generated by Django 3.2 on 2021-04-12 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='desciption',
        ),
        migrations.RemoveField(
            model_name='product',
            name='carats',
        ),
        migrations.RemoveField(
            model_name='product',
            name='poids',
        ),
    ]
