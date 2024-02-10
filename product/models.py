from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_category')
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='media/images')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
