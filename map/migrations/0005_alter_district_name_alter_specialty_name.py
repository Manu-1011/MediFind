# Generated by Django 5.1.6 on 2025-03-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_alter_specialty_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
