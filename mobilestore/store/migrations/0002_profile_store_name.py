# Generated by Django 4.1.5 on 2023-03-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='store_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
