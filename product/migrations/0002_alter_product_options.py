# Generated by Django 3.2.8 on 2021-10-28 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_added',)},
        ),
    ]
