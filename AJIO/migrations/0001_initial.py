# Generated by Django 5.0.2 on 2024-04-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KidsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Src', models.CharField(max_length=255)),
                ('Brand_Name', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Stars', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Actual_Price', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Value', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MensData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Src', models.CharField(max_length=255)),
                ('Brand_Name', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Stars', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Actual_Price', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Value', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WomensData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Src', models.CharField(max_length=255)),
                ('Brand_Name', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Stars', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Actual_Price', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Value', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
