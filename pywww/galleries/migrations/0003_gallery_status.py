# Generated by Django 3.2.9 on 2022-02-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20220222_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='status',
            field=models.CharField(choices=[('HIDE', 'hide'), ('PUBLISHED', 'published'), ('NEW', 'new')], default='NEW', max_length=50),
        ),
    ]
