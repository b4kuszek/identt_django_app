# Generated by Django 3.2.5 on 2021-07-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_pizza_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='main_topping',
            field=models.CharField(default='ser', max_length=40),
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
