# Generated by Django 3.2.5 on 2021-07-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]