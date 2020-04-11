# Generated by Django 3.0.4 on 2020-04-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Adress', models.CharField(max_length=200)),
                ('Phone', models.PositiveIntegerField()),
                ('Discount', models.PositiveIntegerField()),
                ('Email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(max_length=200)),
                ('Item', models.CharField(max_length=200)),
                ('Rate', models.PositiveIntegerField()),
                ('Medicine_Packets', models.PositiveIntegerField()),
                ('Tax_Name', models.CharField(max_length=200)),
                ('Tax_Rate', models.PositiveIntegerField()),
            ],
        ),
    ]
