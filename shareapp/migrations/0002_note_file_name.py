# Generated by Django 4.1.3 on 2023-06-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='file_name',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
