# Generated by Django 4.2.11 on 2024-06-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
