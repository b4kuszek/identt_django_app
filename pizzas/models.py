from django.db import models

# Create your models here.

PIZZA_SIZE = (
    ('S', 'mała'),
    ('M', 'średnia'),
    ('L', 'duża'),
    ('XXL', 'ogromna')
)


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    main_topping = models.CharField(max_length=40, default="ser")
    size = models.CharField(choices=PIZZA_SIZE, max_length=30, default='S')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.price} zł'
