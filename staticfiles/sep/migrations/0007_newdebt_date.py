# Generated by Django 4.1.1 on 2022-09-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sep', '0006_newdebt_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='newdebt',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]