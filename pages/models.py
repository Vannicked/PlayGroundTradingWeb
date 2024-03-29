from django.db import models

# Create your models here.
class Portfolio(models.Model):
    stock_name = models.CharField(max_length=10)
    num_shares = models.IntegerField()

    def __str__(self):
        return f"{self.stock_name - self.num_shares}"