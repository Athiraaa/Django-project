# Generated by Django 2.2 on 2022-09-30 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220930_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ['id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
