# Generated by Django 4.1.5 on 2023-04-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_orderitems_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorders',
            name='address',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
