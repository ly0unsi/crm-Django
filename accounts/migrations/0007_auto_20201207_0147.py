# Generated by Django 3.1.3 on 2020-12-07 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_order_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('out of delivery', 'out of delivery'), ('Delivred', 'Delivred')], max_length=200),
        ),
    ]