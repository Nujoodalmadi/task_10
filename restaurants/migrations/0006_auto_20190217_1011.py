# Generated by Django 2.1.5 on 2019-02-17 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20190217_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.Restaurant'),
        ),
    ]
