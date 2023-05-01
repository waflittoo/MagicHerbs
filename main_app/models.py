from django.db import models

# Create your models here.

class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    image_alt = models.CharField(max_length=100)
    available = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})

class Travel(models.Model):
    class Meta:
        verbose_name = "Travel"
        verbose_name_plural = "Travels"
    
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    extended_description = models.TextField()
    image = models.ImageField(upload_to='travel')
    image_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Travel_detail", kwargs={"pk": self.pk})