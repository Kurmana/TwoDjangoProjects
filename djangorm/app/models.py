from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_date']
