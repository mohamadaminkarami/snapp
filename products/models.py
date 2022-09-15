from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):

    def __str__(self) -> str:
        return str(self.pk)
    pass


class ProductScore(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"product={self.product.id}:customer={self.customer.id}:score={self.score}"
