# Generated by Django 3.2.9 on 2021-11-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.SmallIntegerField(blank=True, help_text="Please use this format 'yyyy'", null=True),
        ),
    ]
