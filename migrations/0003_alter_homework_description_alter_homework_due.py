# Generated by Django 5.0.1 on 2024-01-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(),
        ),
    ]