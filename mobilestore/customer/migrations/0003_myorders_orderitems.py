# Generated by Django 4.1.5 on 2023-04-07 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_alter_cartitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.myorders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.mobile')),
            ],
        ),
    ]
