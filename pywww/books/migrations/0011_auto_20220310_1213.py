# Generated by Django 3.2.9 on 2022-03-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autorzy'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Książka', 'verbose_name_plural': 'Książki'},
        ),
    ]
