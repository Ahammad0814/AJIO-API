# Generated by Django 5.0.2 on 2024-04-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AJIO', '0003_ordersdata_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindata',
            name='Security',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
