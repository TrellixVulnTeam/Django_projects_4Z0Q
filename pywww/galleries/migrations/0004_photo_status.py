# Generated by Django 3.2.9 on 2022-02-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_gallery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='status',
            field=models.CharField(choices=[('HIDE', 'hide'), ('PUBLISHED', 'published'), ('NEW', 'new')], default='NEW', max_length=50),
        ),
    ]
