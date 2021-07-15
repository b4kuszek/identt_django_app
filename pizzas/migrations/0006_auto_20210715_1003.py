# Generated by Django 3.2.5 on 2021-07-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_pizza_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='text',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('S', 'mała'), ('M', 'średnia'), ('L', 'duża'), ('XXL', 'ogromna')], default='S', max_length=30),
        ),
    ]