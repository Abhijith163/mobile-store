# Generated by Django 4.1.5 on 2023-04-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_remove_orderitems_date_added_myorders_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorders',
            name='review',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
