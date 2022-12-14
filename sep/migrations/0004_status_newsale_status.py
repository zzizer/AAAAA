# Generated by Django 4.1.1 on 2022-09-15 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sep', '0003_alter_measured_in_name_alter_product_measuredin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAvailable', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='newsale',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sep.status'),
        ),
    ]
