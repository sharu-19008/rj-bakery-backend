from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('breads-and-buns', 'Breads & Buns'),
        ('cakes-and-pastries', 'Cakes & Pastries'),
        ('cupcakes', 'Cupcakes'),
        ('biscuits-and-cookies', 'Biscuits & Cookies'),
        ('sweets', 'Sweets'),
        ('snacks', 'Snacks & Namkeen'),
        ('hot-beverages', 'Hot Beverages'),
        ('cold-beverages', 'Cold Beverages'),
        ('ice-creams','Ice Creams'),
    ]

    FOOD_TYPE_CHOICES = [
        ('veg', 'Pure Veg'),
        ('non-veg', 'Non-Veg'),
        ('egg', 'Contains Egg'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    food_type = models.CharField(max_length=15, choices=FOOD_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_no_of_ratings = models.IntegerField(default=0)
    sum_ratings = models.IntegerField(default=0)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.total_no_of_ratings > 0:
            self.average_rating = round(self.sum_ratings / self.total_no_of_ratings, 1)
        else:
            self.total_no_of_ratings = 0.0
        super().save(*args, **kwargs)

    def clean(self):
        if self.price < 0.0:
            raise ValidationError("Price cannot be negative")
        if self.total_no_of_ratings < 0:
            raise ValidationError("Total Ratings cannot be negative")
        if self.sum_ratings < 0:
            raise ValidationError("Sum Ratings cannot be negative")


        
    def __str__(self):
        return self.name

